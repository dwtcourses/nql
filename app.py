#!/usr/bin/env python3

from flask import Flask, render_template, request, url_for, redirect
import textprocess
import execute

app= Flask(__name__.split('.')[0]) #specify what belongs to application
#app.config.from_envvar('NQL_SETTINGS', silent=True)

s = ''


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    global s

    if request.method == 'POST':
        query = request.form['filename']
        squery = textprocess.query(query)
        s = execute.execi(squery)
        if not s:
            return redirect(url_for('search'))
        else:
            return "ERROR"

    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    global s
    return "i was here"

if __name__ == '__main__':
    app.debug = True
    app.run()
