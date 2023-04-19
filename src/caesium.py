from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    os.system('gcc -o caesium caesium.c')
    flag = os.environ['FLAG']
    os.system(f'export FLAG={flag}')
    secret_key = os.environ['SECRET_KEY']
    os.system(f'export SECRET_KEY={secret_key}')
    return 'api up'

@app.route('/caesium')
def titanium():
  arg1 = request.args.get('arg1')
  try:
    output = subprocess.check_output(['./caesium', arg1])
    return output.decode('utf-8')
  except:
    return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0')
