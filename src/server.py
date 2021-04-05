from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    print("running")
    return "Hello My Name is Karan"

if __name__ == "__main__":
    app.run()




