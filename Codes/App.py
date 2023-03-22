from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Kanlayakorn!'

@app.route('/Id')
def Id():
    return '654272101'

@app.route('/name')
def name():
    return 'Kanlayakorn Jongjaemsai'

@app.route('/university')
def university():
    return 'Phetchaburi Rajabhat University'

if __name__ == '__main__':
    app.run(debug=True)