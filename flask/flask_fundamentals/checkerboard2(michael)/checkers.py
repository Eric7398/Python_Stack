from flask import Flask, render_template
app = Flask(__name__)   

@app.route('/')
def addbox(num):
    return render_template("index.html", num =(8))








if __name__=="__main__":  
    app.run(debug=True)   
    
