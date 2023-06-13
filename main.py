from flask import Flask, jsonify, request, json

app = Flask(__name__)

@app.route('/ola')
def teste():
    
    return 'ola'

if __name__ == '__main__':
    app.run(debug=True)