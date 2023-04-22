from flask import Flask, request, render_template, redirect, url_for
import subprocess
import os

flag = os.environ['FLAG']
os.system(f'export FLAG={flag}')
secret_key = os.environ['SECRET_KEY']
os.system(f'export SECRET_KEY={secret_key}')

app = Flask(__name__)

form_placeholder = 'Enter payload here'

response = ''

@app.route('/')
def index():
    return render_template('index.html', RESPONSE=response)

@app.route('/titanium', methods=['POST'])
def titanium():
  global response
  arg1 = request.form['arg1']
  try:
    output = subprocess.check_output(['./titanium', arg1])
    response = output.decode('utf-8')
  except:
    response = ''
  return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
