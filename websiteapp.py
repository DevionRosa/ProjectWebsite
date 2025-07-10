# webpage.py
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__) # Here's your 'app' instance

# ... (rest of your code)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")