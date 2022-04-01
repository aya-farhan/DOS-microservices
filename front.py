from flask import Flask
import requests
import json 

app = Flask(__name__)

#in this microservice all i do is routing the coming rquest to the corresponding responsible server which run on the sam VM ith different ports (192.168.1.4:5000-->order_server, 192.168.1.4:5001-->catalog_server)

#to catalog_server
@app.route('/search/<topic>')
def search(topic):
    result = requests.get('http://192.168.1.4:5001/search/'+topic).json()
    print(result[0]['title'])
    
    return json.dumps(result)


#to catalog_server    
@app.route('/info/<book_id>')
def info(book_id):
    result = requests.get('http://192.168.1.4:5001/info/'+str(book_id)).json()
    
    return result
    

#to order_server    
@app.route('/purchase/<book_id>')
def purchase(book_id):
    result = requests.get('http://192.168.1.4:5000/purchase/'+str(book_id)).json()
    
    return result
