from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    os.system('gcc -fno-stack-protector -o titanium titanium.c')
    return 'api up'

# Route for 'titanium' buffer overflow challenge
@app.route('/titanium')
def titanium():
  flag = os.environ['FLAG']
  os.system(f'export FLAG={flag}')
  secret_key = os.environ['SECRET_KEY']
  os.system(f'export SECRET_KEY={secret_key}')
  arg1 = request.args.get('arg1')
  try:
    output = subprocess.check_output(['./titanium', arg1])
    return output.decode('utf-8')
  except:
    return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0')
