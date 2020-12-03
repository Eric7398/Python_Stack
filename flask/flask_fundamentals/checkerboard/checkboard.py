from flask import Flask, render_template
app = Flask(__name__)   


@app.route('/')
def first():
    return render_template("index.html", ver= 8, hor=8)

@app.route('/4')
def second():
    return render_template("index.html", ver= 4, hor=5)


@app.route('/<int:x>/<int:y>')
def third(x,y):
    return render_template("index.html", ver=y, hor=x)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def fourth(x,y,color1,color2):
    return render_template("index.html", ver=y, hor=x, check_color1 = color1, check_color = color2)


if __name__=="__main__":  
    app.run(debug=True)   
    
