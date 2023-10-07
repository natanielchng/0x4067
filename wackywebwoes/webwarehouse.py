from flask import Flask, render_template_string, redirect, url_for, request, Response
from urllib.parse import urlparse
import requests
import base64
import json
import sqlite3

app = Flask(__name__)

# import logging
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)
# app.logger.disabled = True
# log.disabled = True

html_head = """
  <head>
      <title>Wacky Web Warehouse</title>
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css">
    </head>
"""

@app.route("/")
def index():
  return redirect(url_for('room_0'))

##### Room 0 (Inspector Tools) #####
@app.route('/8e1b44b0a5beed915c846ea667142617dd51b6ee246ba930965c6e331f57b34c')
def room_0():
  message = 'Browser inspector tools are essential for uncovering hidden elements and vulnerabilities in web applications, enabling the inspection of webpage source code, which can reveal concealed information, and their usage underscores their importance in identifying security flaws and debugging web applications.'
  html_content = html_head + f"""
    <body>
      <main class="container">
        <h1>Room 0</h1>
        <p>{message}</p>
        <a href="/f99f55aeda8d7d6198c0bfae1350875f8a173c1f1c6ba2a5f2a18f73e674a9e0" 
           style="display: none;"
           role="button">Proceed to Room 1
        </a>
      </main>
    </body>
  """

  return render_template_string(html_content)
  
##### Room 1 (Directory Enumeration) #####
@app.route('/f99f55aeda8d7d6198c0bfae1350875f8a173c1f1c6ba2a5f2a18f73e674a9e0')
def room_1():
  message = 'Wordlists like <code>SecLists</code> and directory enumeration tools such as <code>dirb</code> are essential for uncovering hidden webpage content, but their misuse can pose security risks, emphasizing the need for responsible usage and robust cybersecurity measures.'
  html_content = html_head + f"""
    <body>
      <main class="container">
        <h1>Room 1</h1>
        <p>{message}</p>
      </main>
    </body>
  """

  return render_template_string(html_content)

@app.route('/autodiscover')
def autodiscover():
  html_content = html_head + f"""
    <body>
      <main class="container">
        <h1>Room 1</h1>
        <a href="/98347f2b2ba9f3430dee8c1cc9fb4b64407154af4edcc279c6950833a1a66a88" 
           role="button">Proceed to Room 2
        </a>
      </main>
    </body>
  """
  
  response = Response(html_content)
  response.set_cookie('pantry', 'eyJpc19hbGxvd2VkX3RvX2VudGVyIjogMH0=')
  
  return response
  

##### Room 2 (Cookie Tampering) #####
@app.route('/98347f2b2ba9f3430dee8c1cc9fb4b64407154af4edcc279c6950833a1a66a88')
def room_2():
  
  decoded_bytes = base64.b64decode(request.cookies['pantry'])
  decoded_dict = json.loads(decoded_bytes.decode('utf-8'))

  message = 'Cookie tampering can have significant cybersecurity implications where manipulating cookies can grant unauthorized access to web resources, highlighting the importance of securing cookies and implementing proper authentication mechanisms.'
  
  if decoded_dict['is_allowed_to_enter']:
    html_content = html_head + """
      <body>
        <main class="container">
          <h1>Room 2</h1>
          <a href="/5f106379cbda5f75215d54ed15ec26e0712c2262a9abe8b1b249980a0f2107df?url=https://raw.githubusercontent.com/0x4067/UCv059SX/main/UCv059SX.txt" 
             role="button">Proceed to Room 3
          </a>
        </main>
      </body>
    """
  else:
    html_content = html_head + f"""
      <body>
        <main class="container">
          <h1>Room 2</h1>
          <p>{message}</p>
        </main>
      </body>
    """

  return render_template_string(html_content)

###### Room 3 (SSRF) #####

room_3_secret_access = False
@app.route('/5f106379cbda5f75215d54ed15ec26e0712c2262a9abe8b1b249980a0f2107df')
def room_3():
  
  global room_3_secret_access

  url = request.args.get('url')
  message = ''
  path = ''
  if url is not None:
    message = requests.get(url).text
    path = urlparse(url).path

  print(path)

  if path == '/room-3-secret':
    room_3_secret_access = True
  else:
    room_3_secret_access = False
     
  html_content = html_head + f"""
    <body>
      <main class="container">
        <h1>Room 3</h1>
        <p>{message}</p>
      </main>
    </body>
  """

  return render_template_string(html_content)

@app.route('/room-3-secret')
def room_3_secret():

  global room_3_secret_access
  
  if room_3_secret_access:
    room_3_secret_access = False
    return '<a href="/d4688e416c8a6424a5c83090526a4a09985b6f2b5cc3f5918360130826626bf3" role="button">Proceed to Room 4</a>'
  else:
    return redirect(url_for('room_3'))

##### Room 4 (XSS) #####

room_4_admin_messages = []
room_4_server_history = []
room_4_last_path = ''
room_4_navbar = """
  <p>Cross-Site Scripting (XSS) is where an attacker can inject malicious scripts into a web application, potentially compromising user data and security.</p>
  <p>In this room, you are able to send messages to an Admin via the Message Panel. The messages received by the Admin can be viewed in the Admin Panel. Your task is to "force" the Admin to send a POST request containing the webpage cookies to the Malicious server in order to receive the path to the next room. The requests made to the malicious server can be viewed in the Malicious Server panel.</p>
  <grid>
    <a href="/d4688e416c8a6424a5c83090526a4a09985b6f2b5cc3f5918360130826626bf3" role="button">View Message panel</a>
    <a href="/room-4-admin" role="button">View Admin panel</a>
    <a href="/room-4-attackserver" role="button">View Malicious Server</a>
  </grid>
  <br><br>
"""

@app.route('/d4688e416c8a6424a5c83090526a4a09985b6f2b5cc3f5918360130826626bf3', methods=['GET', 'POST'])
def room_4():
  global room_4_navbar
  global room_4_last_path
  global room_4_admin_messages
  html_content = html_head + f"""
      <body>
        <main class="container">
          <h1>Room 4</h1>
          {room_4_navbar}
          <form method="POST">
            <input type="text" id="message" name="message" placeholder="Write your message here...">
            <button type="submit">Send message to Admin</button>
          </form>
        </main>
      </body>
    """
  if request.method == 'POST':
    room_4_admin_messages.insert(0, request.form.get('message'))
  room_4_last_path = '/d4688e416c8a6424a5c83090526a4a09985b6f2b5cc3f5918360130826626bf3'
  return render_template_string(html_content)


@app.route('/room-4-admin')
def room_4_admin():
  global room_4_admin_messages
  global room_4_navbar
  global room_4_last_path
  messages_string = ''
  for index, message in enumerate(room_4_admin_messages):
    messages_string += f'<em>Message {len(room_4_admin_messages) - index}</em><br><p>{message}</p><hr>'
  html_content = html_head + f"""
    <body>
      <main class="container">
        <h1>Room 4</h1>
        {room_4_navbar}
        {messages_string}
      </main>
    </body>
  """
  room_4_last_path = '/room-4-admin'
  response = Response(html_content)
  response.set_cookie('room-4-cookie', 'DO NOT DELETE')
  return response

@app.route('/room-4-attackserver', methods=['GET', 'POST'])
def room_4_attackserver():
  global room_4_navbar
  global room_4_server_history
  global room_4_admin_messages
  global room_4_last_path
  server_request_string = ''
  next_room = '/2a30d440ee2e6c26d703a956e78d1b5fdb70ec9d6ae5dd0fb363d0097b6018dc'
  
  if room_4_last_path == '/room-4-admin' and request.method == 'POST' and 'room-4-cookie' in request.data.decode("utf-8"):
    room_4_server_history.insert(0, f'{request.headers}<br><br>{request.data.decode("utf-8")}<br><br>The path to room five is {next_room}')
  else:
    room_4_server_history.insert(0, f'{request.headers}<br><br>{request.data.decode("utf-8")}')
    
  for index, server_request in enumerate(room_4_server_history):
    server_request_string += f'<em>Request {len(room_4_server_history) - index}</em><br><code>{str(server_request)}</code><hr>'
  
  html_content = html_head + f"""
    <body>
      <main class="container">
        <h1>Room 4</h1>
        {room_4_navbar}
        {server_request_string}
      </main>
    </body>
  """
  room_4_last_path = '/room-4-attackserver'
  return render_template_string(html_content)

##### Room 5 (SQL Injection) #####

admin_username = 'room5'
admin_password = '1657dc58c499236122837e44eb423dfd51d646ada1ee177945c822fdcf2baef4'
connect = sqlite3.connect('room5.db')
connect.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')
connect.execute('CREATE TABLE IF NOT EXISTS paths (username TEXT, next_path TEXT)')
with sqlite3.connect("room5.db") as users:
  cursor = users.cursor()
  cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", (admin_username, admin_password))
  cursor.execute("INSERT INTO paths (username, next_path) VALUES (?,?)", ('room5', '/somepath'))
  users.commit()

@app.route('/2a30d440ee2e6c26d703a956e78d1b5fdb70ec9d6ae5dd0fb363d0097b6018dc', methods=['GET', 'POST'])
def room_5():
  
  return_message = ''
  message = 'SQL Injection (SQLi) can have significant cybersecurity impacts because it allows attackers to manipulate SQL queries in a way that can lead to unauthorized access, data leakage, or even data manipulation in a database. This vulnerability emphasises the importance of input validation, parameterized queries, and secure coding practices in web application security.'
  
  if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')
    query = 'SELECT * FROM users WHERE username="' + username + '" AND PASSWORD="' + password + '";'
    with sqlite3.connect("room5.db") as users:
      print(query)
      cursor = users.cursor()
      try:
        cursor.execute(query)
        result = cursor.fetchone()
      except:
        result = None
      print(result)
    if result is not None:
      return_message = '<a href="/d4688e416c8a6424a5c83090526a4a09985b6f2b5cc3f5918360130826626bf3" role="button">Proceed to Room 6</a>'

  html_content = html_head + f"""
    <body>
      <main class="container">
        <h1>Room 5</h1>
        <p>{message}</p>
        <!--usernames: room5-->
        <form method="POST">
          <input type="text" id="username" name="username" placeholder="Enter username">
          <input type="text" id="password" name="password" placeholder="Enter password">
          <button type="submit">Login</button>
        </form>
        {return_message}
      </main>
    </body>
  """

  return render_template_string(html_content)

if __name__ == '__main__':
  print("""                                                                         
       ___     _                ___ _            ___     ___ _   ___     ___ ___ 
 _ _ _| | |___| |_ _ _    _ _ _|_  | |_    _ _ _| | |___|_  | |_|   |_ _|  _|_  |
| | | |_  |  _| '_| | |  | | | |_  | . |  | | | |_  |  _|_  |   | | | | |_  |_  |
|_____| |_|___|_,_|_  |  |_____|___|___|  |_____| |_|_| |___|_|_|___|___|___|___|
                  |___|                                                          
    """)
  print("Running on http://0.0.0.0:5000")
  print("\n\n")
  app.run(host='0.0.0.0') 