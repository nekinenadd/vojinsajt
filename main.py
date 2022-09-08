from flask import Flask,render_template,request
import smtplib



app = Flask(__name__)
mail = Mail(app)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config["MAIL_USERNAME"] = "rsautomobili02@gmail.com"
app.config["MAIL_PASSWORD"] = "gutbjibjoxhkorvp"
app.config["MAIL_USE_SSL"] = True
mail = Mail(app)

@app.route('/', methods=['POST','GET'])
def home():
    return render_template('index.html')



@app.route('/send',methods=['POST','GET'])
def send():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)