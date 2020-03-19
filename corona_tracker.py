import requests
from bs4 import BeautifulSoup

r=requests.get("https://www.worldometers.info/coronavirus/#countries")
soup=BeautifulSoup(r.content,'html.parser')

x=requests.get("https://www.boldtuesday.com/pages/alphabetical-list-of-all-countries-and-capitals-shown-on-list-of-countries-poster")
soup_again=BeautifulSoup(x.content,'html.parser')

t=soup.find('tbody')
tb=soup_again.find('tbody')

#List of Overall contries
cont_name_list=[]
for tr in tb.findAll('tr'):
    for td in tr.findAll('td'):
        cont_name_list.append(td.text.title())
contry_names=set(cont_name_list[2::2])

#Listwise data of every infected contry
combined_data=[]
for tr in t.findAll('tr'):
    contry_data=[]
    for td in tr.findAll('td'):
        contry_data.append(td.text)
    combined_data.append(contry_data)
    
#List of the number of total cases of infections
total_inf=[]
inf_cont_names=set()
for i in range(0,len(combined_data)):
        total_inf.append(int(combined_data[i][1].replace(',','')))
        inf_cont_names.add(combined_data[i][0])

#Getting most infected contry        
f2=max(total_inf)
first=total_inf.index(f2)
f1=combined_data[first][0]

print("THE MOST AFFECTED PLACES ARE:")
print(f1,"\t",f2,"infected")    
total_inf.remove(f2)
total_inf.insert(first,-1)

#second most infected contry
s2=max(total_inf)
second=total_inf.index(s2)
s1=combined_data[second][0]

#third most infected contry
print(s1,"\t",s2,"infected")    
total_inf.remove(s2)
total_inf.insert(second,-1)

t2=max(total_inf)
third=total_inf.index(t2)
t1=combined_data[third][0]

print(t1,"\t",t2,"infected")

#Finding the safest places
print("\nTHE SAFEST PLACES ARE:")

rem=contry_names-inf_cont_names
rem=rem-{'United Kingdom*','United States','Central African Republic','United Arab Emirates','South Korea','Bosnia & Herzegovina','Antigua & Barbuda','Bahamas, The','Congo, Democratic Republic Of The','Saint Vincent & The Grenadines','Gambia, The','Guinea-Bissau','South Sudan','Trinidad & Tobago'}
rem=list(rem)
rem.sort()

if rem:
    for i in rem:
        print(i,end=', ')
    print("\nNOT A SINGLE PERSON IS RECORDED INFECTED IN THESE CONTRIES")    
else:
    #finding minimum number of cases
    for m in total_inf:
        if m>=0:
            minim=m
            break

    for n in total_inf:
        if n<minim and n>=0:
            minim=n

    #printing the least infected contries
    for k in combined_data:
        if int(k[1].replace(',',''))==minim:
            print(k[0],end=', ')

    if minim==1:
        print("\nTHESE ARE THE LEAST INFECTED PLACES WITH ONLY ONE CASE")
    else:
        print("\nTHESE ARE THE LEAST INFECTED PLACES WITH",minim,"CASE ONLY")
    

