from flask import Flask, render_template
app = Flask(__name__)
@app.route("/",methods =['GET', 'POST'])
def home():
    return render_template('homepage.html')

@app.route("/name",methods =['GET', 'POST'])

def home():
    return render_template('homepage.html',name="GreetingU")

@app.route("/name",methods =['GET', 'POST'])

try:
    def operation():
         first_input=request.form['Name']
         greet=request.form['Greeting']


         input=string(first_input)
         if operation=="1":
              Result="Happy birthday"
         elif operation=="2":
              Result="Happy Christmas"
         else:
              operation="3"
              Result="Happy Newyear"
    
    return render_template(
       'name.html',
       input1=input1,
       result=Result,
       calculation_success=True
    )

except UnknownError:
    return render_template(
       'name.html',
       input1=input1,
       result="Unknown Error",
       calculation_success=False
    )
   
    
    
    
if _name_='_main_':
    Flask_App.debug=True
    Flask_App.run()
