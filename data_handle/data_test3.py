import requests
from bs4 import BeautifulSoup
import json

API = '950349a8ab593b4aa694aa0bf87a233e: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'
url = 'https://{}@abctest-shop.myshopify.com/admin/api/2021-10/{}.json'.format(API,'customers')

r = requests.get(url)

# Create csv
csv_headers = 'id,email,accepts_marketing,created_at,updated_at,first_name,last_name,orders_count,state,' \
              'total_spent,last_order_id,note,verified_email,multipass_identifier,tax_exempt,phone,' \
              'tags,last_order_name,currency,accepts_marketing_updated_at,marketing_opt_in_level,' \
              'tax_exemptions,sms_marketing_consent\n'
with open('shopify_customers.csv','w') as f:
    f.write(csv_headers)

# Import data
datas = json.loads(r.text)

with open('shopify_customers.csv','a') as file:
    for i in datas['customers']:
        data = '{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(i['id'],i['email'],i['accepts_marketing'],i['created_at'],i['updated_at'],
                                                                                             i['first_name'],i['last_name'],i['orders_count'],i['state'],i['total_spent'],
                                                                                             i['last_order_id'],i['note'],i['verified_email'],i['multipass_identifier'],i['tax_exempt'],
                                                                                             i['phone'],i['tags'],i['last_order_name'],i['currency'],i['accepts_marketing_updated_at'],
                                                                                             i['marketing_opt_in_level'],i['tax_exemptions'],i['sms_marketing_consent'])
        file.write(data)
        print(data)
