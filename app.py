from flask import Flask, render_template,request


app = Flask(__name__)

@app.route("/name",methods =['GET', 'POST'])

def home():
    if request.method == "POST":
        input1 = request.form.get('name')
        input2 = request.form.get('message')
        
        return render_template('name.html', Result=input1,name=input2)
    
    return render_template('homepage.html',name="GreetingU")



if __name__ == "__main__":
    app.run(debug=True)