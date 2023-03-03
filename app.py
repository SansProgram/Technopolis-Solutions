# Import flask
from flask import Flask

# Call the object app to create the app
app = Flask(__name__)

# Register a route
@app.route("/")

# define a function
def hello_world():
  return "Hello World"

# Starting the app
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
