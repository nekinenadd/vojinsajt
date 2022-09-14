from flask import Flask,render_template,request
from redmail import outlook



app = Flask(__name__)



@app.route('/home')
@app.route('/', methods=['POST','GET'])
def home():
    return render_template('index.html')



@app.route('/send',methods=['POST','GET'])
def send():
    sender_email = request.form.get('email')
    mess = request.form.get('message')

    outlook.username = "nenaddjurdjevic2002@outlook.com"
    outlook.password = "Fender12002"

    outlook.send(
    receivers=["rsautomobili02@gmail.com"],
    subject=sender_email,
    text=mess
    )


    return render_template('success.html')




if __name__ == "__main__":
    app.run(debug=True)