from flask import Flask, render_template
app = Flask(__name__)   


@app.route('/play/<num>/<color>')
def addbox(num, color):
    print("play/num is running")
    return render_template("index.html", number=int(num), acolor = color)








if __name__=="__main__":  
    app.run(debug=True)   
    
