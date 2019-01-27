from flask import Flask, request,render_template
app = Flask(__name__)
@app.route('/')
def hello():
    return 'hello world!'
@app.route('/sample')
def sample():
    return render_template('hello.html')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080)
