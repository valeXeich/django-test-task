import csv
import json
import os

from datetime import datetime

from django.contrib.auth.hashers import make_password
from bs4 import BeautifulSoup



def delete_bad_users(path):
    data = []
    with open(path, 'r') as f:
        xml_data = f.read()
    soup = BeautifulSoup(xml_data, 'xml')
    users_tag = soup.find('users')
    users = users_tag.find_all('user')
    for user in users:
        first_name = user.first_name.text
        last_name = user.last_name.text
        avatar = user.avatar.text
        if first_name == '' or last_name == '':
            continue
        if any(name in "()[]" for name in first_name) or any(name in "()[]" for name in last_name):
            continue
        data.append({'first_name': first_name, 'last_name': last_name, 'avatar': avatar})
    return data
    

def comparison_data(path, data):
    result = []
    with open(path, 'r') as f:
        csv_data = csv.DictReader(f)
        for csv_ in csv_data:
            try:
                fisrt_latter = csv_['username'][0]
                last_name = csv_['username'].split('.')[-1]
            except IndexError:
                continue
            for xml in data:
                if fisrt_latter == xml['first_name'][0] and last_name == xml['last_name']:
                    csv_['date_joined'] = datetime.utcfromtimestamp(int(csv_['date_joined'])).strftime('%Y-%m-%d %H:%M:%S')
                    csv_['password'] = make_password(csv_['password'])
                    xml.update(csv_)
    for info in data:
        result.append({'model': "user.CustomUser", 'fields': info})
    return result
            
    
    
def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    data = delete_bad_users('data/test_task.xml')
    result = comparison_data('data/test_task.csv', data)
    with open('db_data.json', 'w') as f:
        f.write(json.dumps(result, indent=4))
    


if __name__ == '__main__':
    main()