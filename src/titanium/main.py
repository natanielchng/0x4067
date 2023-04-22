from flask import Flask, request, render_template, redirect, url_for, session
import subprocess
import os

sessions_key = os.environ['SESSIONS_KEY']

app = Flask(__name__)
app.secret_key = sessions_key

@app.route('/')
def index():
    if session.get('response'):
      response = session.get('response')
    else:
      response = ''
      session['response'] = response
    return render_template('index.html', RESPONSE=response)

@app.route('/titanium', methods=['POST'])
def titanium():
  arg1 = request.form['arg1']
  try:
    output = subprocess.check_output(['./titanium', arg1])
    session['response'] = output.decode('utf-8')
  except:
    session['response'] = ''
  return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
