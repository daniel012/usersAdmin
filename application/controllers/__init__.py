from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'admin_sftp'
app.config['MYSQL_DATABASE_PASSWORD'] = '89Qftp_sql'
app.config['MYSQL_DATABASE_DB'] = 'transferencia_sise'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)
conn = mysql.connect()
cursor =conn.cursor()

@app.route('/', methods=['GET'])
def home(): 
 cursor.execute('SELECT * FROM servidor')
 rv = cursor.fetchall()
 row_headers=[x[0] for x in cursor.description]
 json_data=[]
 for result in rv:
  json_data.append(dict(zip(row_headers,result)))
 return json.dumps(json_data)

@app.route('/insert', methods=['POST'])
def register():
    form = request.form
    jsonValue = request.get_json()
    ambiente = jsonValue.get('ambiente')
    idservidor = jsonValue.get('idservidor')
    ip = jsonValue.get('ip')
    nombre = jsonValue.get('nombre')

    cursor.execute("INSERT INTO servidor(ambiente, idservidor, ip, nombre) VALUES(%s, %s, %s, %s)",
    (ambiente, idservidor, ip,nombre))

    # commit to db
    conn.commit()

    return "record inserted"


app.run(debug=True,host='0.0.0.0')

