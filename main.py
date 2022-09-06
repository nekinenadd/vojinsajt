from flask import Flask,render_template,request



app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def home():
    return render_template('index.html')



@app.route('/send',methods=['POST','GET'])
def send():
    title = "Odgovoricemo vam u najkracem roku! Hvala"
    if request.method == "POST":
        Email = request.form.get('email')
        Message = request.form.get('message')
        print(Email,Message)
    return render_template('sent-mail.html',title=title)



if __name__ == "__main__":
    app.run(debug=True)