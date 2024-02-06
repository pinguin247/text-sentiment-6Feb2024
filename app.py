from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__) 

@app.route("/",methods=["GET","POST"]) #declarator
def index():
        return(render_template("index.html"))

    
@app.route("/result",methods=["GET","POST"]) #declarator
def result():
        t = request.form.get("t")
        result = TextBlob(t).sentiment
        return(render_template("result.html",result=result))

    
#jupyter by default use port 8888
#flask by default use port 5000
    
if __name__ == "__main__":
    app.run()