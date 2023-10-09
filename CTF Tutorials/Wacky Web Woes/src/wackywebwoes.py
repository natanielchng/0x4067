from flask import Flask, render_template, render_template_string, redirect, url_for, request, Response
from urllib.parse import urlparse
import routes
import requests
import base64
import json
import sqlite3
import subprocess
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app.logger.disabled = True
log.disabled = True


@app.route("/")
def index():
  return redirect(url_for('room_0'))


####################################
##### Room 0 (Inspector Tools) #####
####################################


@app.route(routes.room_0)
def room_0():
  return render_template('room_0.html', href=routes.room_1)


##########################################
##### Room 1 (Directory Enumeration) #####
##########################################
@app.route(routes.room_1)
def room_1():
  return render_template('room_1.html')


@app.route('/autodiscover')
def autodiscover():
  response = Response(render_template('autodiscover.html', href=routes.room_2))
  response.set_cookie('pantry', 'eyJpc19hbGxvd2VkX3RvX2VudGVyIjogMH0=')
  return response


#####################################
##### Room 2 (Cookie Tampering) #####
#####################################
@app.route(routes.room_2)
def room_2():
  decoded_bytes = base64.b64decode(request.cookies['pantry'])
  decoded_dict = json.loads(decoded_bytes.decode('utf-8'))

  if decoded_dict['is_allowed_to_enter']:
    return render_template(
        'room_2_2.html',
        href=f'{routes.room_3}?apiPath={routes.room_3_message}')
  else:
    return render_template('room_2_1.html')


##########################
###### Room 3 (SSRF) #####
##########################
room_3_secret_access = False


@app.route(routes.room_3, methods=['GET', 'POST'])
def room_3():

  if request.method == 'POST':
      if 'Give-Room-3-Flag' in request.headers:
        return '0x4067{WWW_FOXY_PROXY}'
      return 'Give-Room-3-Flag header not found!'
  
  global room_3_secret_access
  api_path = request.args.get('apiPath')

  if api_path == routes.room_3_secret:
    room_3_secret_access = True
  else:
    room_3_secret_access = False

  if api_path is not None:
    if request.is_secure:
      url = f'https://{request.host}{api_path}'
    else:
      url = f'http://{request.host}{api_path}'
    description = requests.get(url).text
  else:
    description = ''
    api_path = ''

  return render_template('room_3.html', description=description)


@app.route(routes.room_3_secret)
def room_3_secret():
  global room_3_secret_access
  if room_3_secret_access:
    room_3_secret_access = False
    return f'<a href="{routes.room_4}" role="button">Proceed to Room 4</a>'
  else:
    return redirect(url_for('room_3'))


@app.route(routes.room_3_message)
def room_3_message():
  return "Server-Side Request Forgery (SSRF) is where an attacker can manipulate URLs to make unauthorised requests to internal or external resources, potentially compromising security by exploiting the server's trust in the request source. In this room, try to force the webpage to access the '/room-3-secret' path."


########################
##### Room 4 (XSS) #####
########################

room_4_admin_messages = []
room_4_server_history = []
room_4_last_path = ''
room_4_cookie = {'name': 'room_4_cookie', 'value': 'doNotDelete'}


@app.route(routes.room_4, methods=['GET', 'POST'])
def room_4():
  global room_4_navbar
  global room_4_admin_messages

  if request.method == 'POST':
    room_4_admin_messages.insert(0, request.form.get('message'))

  global room_4_last_path
  room_4_last_path = routes.room_4

  return render_template('room_4.html',
                         admin_path=routes.room_4_admin,
                         server_path=routes.room_4_server,
                         main_path=routes.room_4)


@app.route(routes.room_4_admin)
def room_4_admin():
  response = Response(
      render_template('room_4_admin.html',
                      messages=room_4_admin_messages,
                      admin_path=routes.room_4_admin,
                      server_path=routes.room_4_server,
                      main_path=routes.room_4))
  response.set_cookie(room_4_cookie['name'], room_4_cookie['value'])

  global room_4_last_path
  room_4_last_path = routes.room_4_admin

  return response


@app.route(routes.room_4_server, methods=['GET', 'POST'])
def room_4_attackserver():
  global room_4_server_history
  global room_4_admin_messages
  global room_4_last_path
  next_room = routes.room_5
  flag = '0x4067{WWW_YOU_GOT_XSSED}'

  if room_4_last_path == routes.room_4_admin and request.method == 'POST' and room_4_cookie[
      'name'] in request.data.decode("utf-8"):
    room_4_server_history.insert(
        0,
        f'{request.headers}<br><br>{request.data.decode("utf-8")}<br><br>{flag} The path to room five is {next_room}'
    )
  else:
    room_4_server_history.insert(
        0, f'{request.headers}<br><br>{request.data.decode("utf-8")}')

  room_4_last_path = routes.room_4_server

  return render_template('room_4_server.html',
                         server_requests=room_4_server_history,
                         admin_path=routes.room_4_admin,
                         server_path=routes.room_4_server,
                         main_path=routes.room_4)


##################################
##### Room 5 (SQL Injection) #####
##################################

admin_username = 'room5'
admin_password = '1657dc58c499236122837e44eb423dfd51d646ada1ee177945c822fdcf2baef4'
next_room_name = 'room6'
next_room_path = routes.room_6

connect = sqlite3.connect('/tmp/room5.db')
connect.execute(
    'CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, next_room_name TEXT, next_room_path TEXT)'
)
with sqlite3.connect("/tmp/room5.db") as users:
  cursor = users.cursor()
  cursor.execute(
      "INSERT INTO users (username, password, next_room_name, next_room_path) VALUES (?,?, ?, ?)",
      (admin_username, admin_password, next_room_name, next_room_path))
  users.commit()


@app.route(routes.room_5, methods=['GET', 'POST'])
def room_5():
  show_non_working_button = False
  show_working_button = False

  if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')

    query = 'SELECT * FROM users WHERE username="' + username + '" AND PASSWORD="' + password + '";'
    with sqlite3.connect("/tmp/room5.db") as users:
      cursor = users.cursor()

      try:
        cursor.execute(query)
        result = cursor.fetchone()
      except:
        result = None

    if str(
        result
    ) == f"('{admin_username}', '{admin_password}', '{next_room_name}', '{next_room_path}')":
      show_non_working_button = True
      show_working_button = False
    elif str(result) == '(1, 2, 3, 4)':
      show_working_button = True
      show_non_working_button = False

  return render_template('room_5.html',
                         href=routes.room_6,
                         show_non_working_button=show_non_working_button,
                         show_working_button=show_working_button)


######################################
##### Room 6 (Command Injection) #####
######################################

os.system(
    'cd /tmp && echo "Oh, you dropped this: 0x4067{WWW_END_OF_CHALLENGE}" > room_6_flag.txt'
)

@app.route(routes.room_6, methods=['GET', 'POST'])
def room_6():

  show_return_message = False
  echo_message = ''

  if request.method == 'POST':
    feedback = request.form.get('feedback')
    try:
      echo_message = subprocess.run(f'echo {feedback}',
                                    shell=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    text=True).stdout
      show_return_message = True
    except Exception:
      echo_message = ''

  return render_template('room_6.html',
                         show_return_message=show_return_message,
                         echo_message=echo_message)


if __name__ == '__main__':
  print(
      """                                                                    
┬ ┬┌─┐┌─┐┬┌─┬ ┬  ┬ ┬┌─┐┌┐   ┬ ┬┌─┐┌─┐┌─┐
│││├─┤│  ├┴┐└┬┘  │││├┤ ├┴┐  ││││ │├┤ └─┐
└┴┘┴ ┴└─┘┴ ┴ ┴   └┴┘└─┘└─┘  └┴┘└─┘└─┘└─┘                                             
    """)
  print("Running on http://0.0.0.0:5000")
  print("\n\n")
  app.run(host='0.0.0.0')
