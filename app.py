from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    # Do anything in this function and then return the final value to be displayed on the browser
    return "<h1>Hello worlddsfdhg</h1>"

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
    
