import os
from flask import Flask
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world"


# to tell app where and how to run the application
if __name__ == "__main__": 
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True) 
# needs to be updated to debug = False prior to submission

