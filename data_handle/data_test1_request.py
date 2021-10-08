import requests
from bs4 import BeautifulSoup
from config import user


def login(log,pwd):
    s = requests.Session()
    payload = {
        'log': log,
        'pwd': pwd
    }
    r = s.post('http://45.79.43.178/source_carts/wordpress/wp-login.php', data=payload)

    with open('index2.html', 'w') as f:
        f.write(r.text)
    return s

session = login(user.user_login,user.user_pass)
response = session.get('http://45.79.43.178/source_carts/wordpress/wp-admin/')

soup = BeautifulSoup(response.content,'lxml')
# with open('index.html','w') as f:
#     f.write(response.text)

user_name = soup.find('span', {'class': 'display-name'})
if user_name.text == 'Ban Duong':
    print(user_name.text)