# webpage.py
import git
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__) # Here's your 'app' instance

# ... (rest of your code)

@app.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/ProjectWebsite/ProjectWebsite')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400