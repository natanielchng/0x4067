from flask import Flask, request
import subprocess
import os

app = Flask(__name__)


@app.route('/')
def index():
  os.system(
    'gcc -o cobalt cobalt.c -Wno-format-security -z noexecstack -no-pie')
  return 'api up'


@app.route('/cobalt')
def cobalt():
  flag = os.environ['FLAG']
  os.system(f'export FLAG={flag}')
  arg1 = request.args.get('arg1')
  try:
    output = subprocess.check_output(['./cobalt', arg1])
    return output.decode('utf-8')
  except:
    return ''


if __name__ == '__main__':
  app.run(host='0.0.0.0')
