from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'admin_sftp'
app.config['MYSQL_DATABASE_PASSWORD'] = '89Qftp_sql'
app.config['MYSQL_DATABASE_DB'] = 'transferencia_sise'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


@app.route('/', methods=['GET'])
def home():
 conn = mysql.connect()
 cursor =conn.cursor()
 cursor.execute('SELECT * FROM servidor')
 rv = cursor.fetchall()
 row_headers=[x[0] for x in cursor.description]
 json_data=[]
 for result in rv:
  json_data.append(dict(zip(row_headers,result)))
 return json.dumps(json_data)


app.run(debug=True,host='0.0.0.0')

