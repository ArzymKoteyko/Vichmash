from ctypes import sizeof
import multiprocessing
from flask import Flask
from flask import render_template, request
from Crypto.Cipher import AES

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/server', methods=['GET', 'POST'])
def server():
    if request.method == 'POST':
        #print(request)
        try:
            print(request.form['foo'])
            print(request.form)
        except:
            print(request.form)
        return 'OK'
    if request.method == 'GET':
        return 'OK'

@app.route('/crypto', methods=['GET', 'POST'])
def crypto():
    if request.method == 'POST':
        return {'string': 'Thats fine'}


def run():
    app.run(host="0.0.0.0", port=5000, threaded=True)

def start():
    number_of_instancies = 1
    threads = [run for i in range(number_of_instancies)]
    jobs = []
    for j in threads:
        p = multiprocessing.Process(target=j)
        jobs.append(p)
        p.start()
    for k in jobs:
        k.join()

if __name__ == '__main__':
    start()
    