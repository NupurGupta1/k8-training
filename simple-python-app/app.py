from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is from Training session'

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8000)