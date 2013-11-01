from flask import Flask

app = Flask(__name__)

@app.route('/')
def bite():
    return 'starting my bit.ly clone'

if __name__ == '__main__':
    app.run()
