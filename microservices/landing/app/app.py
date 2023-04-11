from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


def add(n1, n2):
    URL = 'http://addition-service:'
    port = 5051
    add_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    response = requests.get(add_url)
    print(response)
    return response.json()['result']

def minus(n1, n2):
    URL = 'http://subtraction-service:'
    port = 5052
    add_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    response = requests.get(add_url)
    print(response)
    return response.json()['result']

def multiply(n1, n2):
    URL = 'http://multiplication-service:'
    port = 5053
    add_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    response = requests.get(add_url)
    print(response)
    return response.json()['result']

def divide(n1, n2):
    URL = 'http://division-service:'
    port = 5054
    add_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    response = requests.get(add_url)
    print(response)
    return response.json()['result']

@app.route('/', methods=['POST', 'GET'])
def index():
    try:
        number_1 = int(request.form.get("first"))
        number_2 = int(request.form.get('second'))
        operation = request.form.get('operation')
        result = 0
        if operation == 'add':
            result = add(number_1, number_2)
        elif operation == 'minus':
            result =  minus(number_1, number_2)
        elif operation == 'multiply':
            result = multiply(number_1, number_2)
        elif operation == 'divide':
            result = divide(number_1, number_2)

        flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

        return render_template('index.html')
    except:
        flash(f'No input value')
        return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )