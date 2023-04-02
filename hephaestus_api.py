from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return 'api up'

# Route for 'titanium' buffer overflow challenge
@app.route('/titanium')
def titanium():
  arg1 = request.args.get('arg1')
  try:
    output = subprocess.check_output(['./src/titanium', arg1])
    return output.decode('utf-8')
  except:
    return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
