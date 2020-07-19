from flask import Flask, request,render_template
import requests
from bs4 import BeautifulSoup as b
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found, pip install google") 

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/get_college_details', methods=["GET", "POST"])
def clg_details():
   if request.method == 'POST': 
    text = request.form['mail']
    text = text.split("@")
    query = text[1].split(".")[0] + "college"
    print(query)
    url=[]
    #query = "cit college"
    for j in search(query, tld="co.in", num=2,stop=2, pause=2): 
        url.append(j)
    for i in url:
        html=requests.get(i)
        soup=b(html.content,"html.parser")
        r = soup.find("title")
        print(r.text)
        for q in['Technology','University','Institutions','College','Engineering']:
            if q in r.text:
                return render_template("index.html",data = r.text)
        return render_template("index.html",data = "No such college was found")

@app.route('/get_author_details', methods=["GET", "POST"])
def author_books():
   if request.method == 'POST': 
    text = request.form['author']
    print(text)
    text = text + "books"
    link = ""
    for i in search(text,tld="co.in",num=1,stop=1,pause=2):
      link = i
    return render_template("index.html",book_url = link)

if __name__ == '__main__':
        app.run(host="127.0.0.1",debug=True)   
