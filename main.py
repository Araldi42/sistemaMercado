from flask import Flask, jsonify, request, json

app = Flask(__name__)

@app.route('/')
def teste():
    return print('ola')

if __name__ == '__main__':
    app.run()