import os
import pdb
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/candidate")
def candidate():
    for item in request.form:
        print item
    pdb.set_trace()
    return redirect(url_for('index'))

@app.route("/employer")
def employer():
    return redirect(url_for('index'))

@app.route("/other")
def other():
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
