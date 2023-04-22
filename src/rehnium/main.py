from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return 'api up'

@app.route('/rehnium')
def rehnium():
  return render_template('rehnium.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
