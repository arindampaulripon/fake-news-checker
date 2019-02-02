#!C:/Users/i7/Anaconda3/python.exe
import cgi, cgitb
import string
import requests 
from bs4 import BeautifulSoup 

form = cgi.FieldStorage()


print("Content-Type: text/html; charset=utf-8")

print("")
print("<!DOCTYPE html>")
print("<html>")
print("<head>")

print("<link rel='stylesheet' type='text/css' href='../EasterSS.css'/></head>")
print("<body>")

print ("Hello.")

q = form.getvalue('search')
escaped_search_term = q

number_results = 100
language_code = 'en'


URL = "https://www.google.com/search?q={}&num={}&hl={}".format(escaped_search_term, number_results, language_code)
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')


for node in soup.findAll('h3'):
    rs1 =  (''.join(node.findAll(text=True))).encode("utf-8")
   
    
    
    print(rs1)
    print("</br>")

url3 = ('https://www.youtube.com/results?search_query='+q)
r3 = requests.get(url3)
soup3 = BeautifulSoup(r3.content, 'html.parser') 
    
for node in soup3.find_all("h3"):

    
    print (''.join(node.findAll(text=True)))
    print("<br\>")
    
    


print("</body>")
print("</html>")


