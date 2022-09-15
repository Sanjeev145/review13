from flask import Flask
app = Flask(__name__)
@app.route('/sum')
def sum():
    a = 1
    b = 2
    return a+b
if __name__=='__main__':
    app.run()
