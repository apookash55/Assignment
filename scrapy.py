from bs4 import BeautifulSoup
import urllib.request
import lxml
sauce = urllib.request.urlopen('https://karki23.github.io/Weather-Data/assignment.html').read()
srccode = BeautifulSoup(sauce,'lxml')
l=srccode.find_all('a')
links=[]
city_names=[]
for i in l:
    links.append(i.get('href'))
    city_names.append(i.string)
for k in range(len(links)):
        file = '.\\dataset\\' + city_names[k] + '.csv'
        f=open(file,'w')
        sauce = urllib.request.urlopen('https://karki23.github.io/Weather-Data/' + links[k]).read()
        srccode = BeautifulSoup(sauce,'lxml')
        table = srccode.table
        table_data=[]
        for i in table.find_all('tr')[0:1]:
            line = []
            for j in i.find_all('th'):
                line.append(j.string)
            line = ','.join(line)
            table_data.append(line)
        for i in table.find_all('tr')[1:]:
            line = []
            for j in i.find_all('td'):
                line.append(j.string)
            line = ','.join(line)
            table_data.append(line)
        table_data = '\n'.join(table_data)
        f.write(table_data)
        f.flush()
        print(city_names[k] + '.csv','file written')
        f.close()
