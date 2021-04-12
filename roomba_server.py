from flask import Flask
from flask import request 

app = Flask(__name__)

@app.route('/')
def Zoomba():
    return 'Zoomba server is running!'

if __name__ == '__main__':
    app.run(host= '192.168.0.58', port=9000, debug=False)

