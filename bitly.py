#all imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for,\
                  abort, render_template, flash

#configuration
DATABASE = '/tmp/bitly.db'
DEBUG = TRUE
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


app = Flask(__name__)

@app.route('/')
def bitly():
    return 'starting my bit.ly clone'

if __name__ == '__main__':
#make externally visable-- Turn off degugger!
    #app.run(host='0.0.0.0')
#development mode
    app.run(debug= True)

@app.route('/getaddress', methods = ['POST', 'GET'])
def getaddress():
    error = None
    if request.method == 'POST':
        if valid_address(request.form['web_address']):
            return log_address(request.form['web_address'])
        else:
            error = 'Valid web adress'
    return render_template('getaddress.html', error=error)
