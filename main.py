from bs4 import BeautifulSoup 
import requests, csv
no = 0 
def page(url):
    global no
    data = requests.get(url).text
    data = BeautifulSoup(data, 'html.parser')
    for comp in data.find_all('div', class_='listing-summary-featured'):
        print('***********************************************************')
        link = comp.find('a' ,class_='pull-right')
        company_name = comp.find('h4').text
        no += 1
        if str(link) != 'None':
            with open('company.csv', 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([company_name,str(link.get('href'))])

    print(no)

for i in range(1000):
    url = 'https://www.2merkato.com/directory/' + str(i)
    page(url)
    print(url)
