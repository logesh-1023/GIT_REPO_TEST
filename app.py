from flask import Flask 

app = Flask(__name__)

@app.route("/")
def start():
    return "hai"

if __name__ == '__main__':
    app.run(debug=False,port=7060)