import csv,json
from pathlib import Path
from datetime import datetime
from collections import Counter
R=Path(__file__).resolve().parents[1]
def read(p):
 with p.open(newline='',encoding='utf-8') as f:return list(csv.DictReader(f))
raw=read(R/'data/raw/transactions_raw.csv'); cust={x['customer_id']:x for x in read(R/'data/reference/customers.csv')}; prod={x['product_id']:x for x in read(R/'data/reference/products.csv')}
issues=[]; clean=[]; seen=set(); counts=Counter(); affected=set()
for x in raw:
 tid=x['transaction_id'].strip(); bad=[]
 def add(code,dim,sev,msg):bad.append({'transaction_id':tid,'rule_code':code,'dimension':dim,'severity':sev,'issue_description':msg})
 if tid in seen:add('DUPLICATE_TRANSACTION_ID','Uniqueness','High','Duplicate transaction ID; first occurrence retained.')
 else:seen.add(tid)
 ci=x['customer_id'].strip(); pi=x['product_id'].strip()
 if not ci:add('MISSING_CUSTOMER_ID','Completeness','High','Customer ID is blank.')
 elif ci not in cust:add('INVALID_CUSTOMER_KEY','Referential Integrity','High','Customer ID not found in reference table.')
 if not x['sales_amount'].strip():add('MISSING_SALES_AMOUNT','Completeness','High','Sales amount is blank.')
 if not x['region'].strip():add('MISSING_REGION','Completeness','Medium','Region is blank.')
 dt=None
 for fmt in ('%Y-%m-%d','%d/%m/%Y'):
  try:dt=datetime.strptime(x['transaction_date'].strip(),fmt).date();break
  except ValueError:pass
 if dt is None:add('INVALID_TRANSACTION_DATE','Validity','High','Transaction date cannot be parsed.')
 try:q=int(x['quantity']);
 except:q=None
 if q is None or q<=0:add('INVALID_QUANTITY','Validity','High','Quantity must be a positive integer.')
 try:u=float(x['unit_price'])
 except:u=None
 if u is None or u<=0:add('INVALID_UNIT_PRICE','Validity','High','Unit price must be positive.')
 if not pi or pi not in prod:add('INVALID_PRODUCT_KEY','Referential Integrity','High','Product ID not found in reference table.')
 cr=cust.get(ci,{}).get('region',''); cp=prod.get(pi,{}).get('category','')
 if cr and x['region'].strip().lower()!=cr.lower():add('NONSTANDARD_REGION','Consistency','Medium','Region differs from customer reference; canonical value applied.')
 if cp and x['category'].strip().lower()!=cp.lower():add('NONSTANDARD_CATEGORY','Consistency','Medium','Category differs from product reference; canonical value applied.')
 try:s=float(x['sales_amount']) if x['sales_amount'].strip() else None
 except:s=None
 if q and q>0 and u and u>0 and s is not None and abs(s-q*u)>.01:add('SALES_AMOUNT_MISMATCH','Accuracy','High','Sales amount differs from quantity multiplied by unit price.')
 for z in bad:issues.append(z);counts[z['rule_code']]+=1;affected.add(tid)
 if not bad:clean.append({'transaction_id':tid,'transaction_date':dt.isoformat(),'customer_id':ci,'product_id':pi,'quantity':q,'unit_price':round(u,2),'sales_amount':round(s,2),'region':cr or x['region'].strip().title(),'category':cp or x['category'].strip().title(),'channel':x['channel'].strip(),'status':x['status'].strip()})
def out(path,data,fields):
 with path.open('w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(data)
C=R/'data/cleaned'; C.mkdir(exist_ok=True)
out(C/'transactions_clean.csv',clean,['transaction_id','transaction_date','customer_id','product_id','quantity','unit_price','sales_amount','region','category','channel','status'])
out(C/'data_quality_issues.csv',issues,['transaction_id','rule_code','dimension','severity','issue_description'])
out(R/'reports/profiling_summary.csv',[{'rule_code':k,'issue_count':v} for k,v in counts.most_common()],['rule_code','issue_count'])
summary={'raw_rows':len(raw),'unique_transaction_ids':len(seen),'duplicate_rows':counts['DUPLICATE_TRANSACTION_ID'],'clean_rows':len(clean),'rows_with_one_or_more_issues':len(affected),'issue_records':len(issues),'quality_score_pct':round(100*len(clean)/max(len(seen),1),2),'rule_counts':dict(counts)}
(R/'docs/data_quality_report.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
