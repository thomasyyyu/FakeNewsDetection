from flask import Flask, render_template
from flask import request
import model

app = Flask(__name__)

@app.route('/')
# @app.route('/home', methods=['GET','POST'])
def upload():
    # if request.method == 'POST':
    #     title = request.form.get('title-text')
    #     body = request.form.get('message-text')
    #     result = model.classification(title, body)
    #     if result == 0:
    #         return render_template('home.html', answer = 0)
    #     else:
    #         return render_template('home.html', answer = 1)

    return render_template('home.html')

@app.route('/ajaxcall', methods=['GET','POST'])
def ajaxCall():
    if request.method == 'POST':
        title = request.form.get("title")
        msg = request.form.get("msg")
        result = model.classification(title, msg)
        if result == 0:
            return {"res":"This is Fake!"}
        else:
            return {"res":"This is Real!"}
    return "done"

if __name__ == '__main__':
    app.run(debug=True)