from flask import Flask, request 
app = Flask(__name__)
@app.route("/hello") 
def hello(): 
    return "hello world" 

@app.route("/method", methods=['GET','POST'])
def method():
    if request.method == 'GET':
        return "GET으로 전달"
    else :
        return "POST로 전달"


if __name__ == "__main__": 
    app.run(debug = True) # host주소와 port number 선언

