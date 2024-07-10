from flask import Flask, render_template,request


app = Flask(__name__)

@app.route("/",methods =['GET', 'POST'])

def home():
    if request.method == "POST":
        input1 = request.form.get('name')
        input2 = request.form.get('message')
        
        return render_template('name.html', Result=input1,message=input2)
    
    return render_template('homepage.html')



if __name__ == "__main__":
    app.run(debug=True)