#!C:/Users/i7/Anaconda3/python.exe
import cgi, cgitb
import string
import requests 
from bs4 import BeautifulSoup 

cgitb.enable()

form = cgi.FieldStorage()


print("Content-Type: text/html; charset=utf-8")

print("")
print("<!DOCTYPE html>")
print("<html>")
print("<head>")

print("<link rel='stylesheet' type='text/css' href='../EasterSS.css'/></head>")
print("<body>")
print("<h2>")
print ("Hi, Now you're seeing the top 100 google result at once")
print("</h2>")
print("</br>")
q = form.getvalue('search')
escaped_search_term = q

number_results = 100
language_code = 'en'
print("<h2>")
print ("You Searched For ",q)
print("</h2>")

print("</br>")

URL = "https://search.yahoo.com/search?p={}&num={}&hl={}".format(escaped_search_term, number_results, language_code)
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
print("<h2>")
print("<b>")
print("Google Search Result : ")
print("</b>")
print("</br>")
print("</h2>")
for node in soup.findAll('h3'):
    rs1 =  (''.join(node.findAll(text=True))).encode("utf-8")
   
    
    print("<ul>")
    print("<li>")
    print(rs1)
    print("</li>")
    print("</ul>")
    print("</br>")
    

    
url3 = ('https://www.youtube.com/results?search_query='+q)
r3 = requests.get(url3)
soup3 = BeautifulSoup(r3.content, 'html.parser') 
print("<h2>")
print("<b>")
print("Youtube Video Result : ")
print("</b>")
print("</h2>")
print("</br>")
for node in soup3.find_all("h3"):

    print("<ul>")
    print("<li>")
    print (''.join(node.findAll(text=True)))
    print("</li>")
    print("</ul>")
    print("</br>")
    
    
print("<h2>")
print("<b>")
print("Google Search Result's Links : ")
print("</b>")
print("</br>")
print("</h2>")


for node in soup.findAll('cite'):
    print("<ul>")
    print("<li>")
    print (''.join(node.findAll(text=True))).encode("utf-8")
    print("</li>")
    print("</ul>")
    print("</br>")   
    


print("</body>")
print("</html>")


