from flask import Flask, jsonify
from quote import breaking_quote

application = Flask(__name__)


#homepage endpoint
@application.route("/")
def index():
    return "<h1> Welcome to the home page </h1>"


#quote endpoint
@application.route("/quote")
def quote():
  random_quote = breaking_quote()
  return jsonify({"quote": random_quote})


#this part is executed when the module is called directly - "pipenv run python application.py"
if __name__ == "__main__":
    application.run(debug=True)
