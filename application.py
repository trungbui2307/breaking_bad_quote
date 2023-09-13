from flask import Flask, jsonify
from quote import breaking_quote

app = Flask(__name__)


#homepage endpoint
@app.route("/")
def index():
    return "<h1> Welcome to the home page </h1>"


#quote endpoint
@app.route("/quote")
def quote():
  random_quote = breaking_quote()
  return jsonify({"quote": random_quote})


#this part is executed when the module is called directly - "pipenv run python app.py"
if __name__ == "__main__":
    app.run(debug=True)
