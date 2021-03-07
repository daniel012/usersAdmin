from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
import validate

mysql = MySQL()
app = Flask(__name__)

app.config.from_pyfile('database.cfg')

mysql.init_app(app)
conn = mysql.connect()
cursor =conn.cursor()



@app.route('/', methods=['GET'])
def serverList(): 
 cursor.execute('SELECT * FROM servidor')
 rv = cursor.fetchall()
 row_headers=[x[0] for x in cursor.description]
 json_data=[]
 for result in rv:
  json_data.append(dict(zip(row_headers,result)))
 return json.dumps(json_data)

@app.route('/insert', methods=['POST'])
def serverInsert():
    form = request.form
    jsonValue = request.get_json()
    if validate.createRecords(jsonValue):
        ambiente = jsonValue.get('ambiente')
        idservidor = jsonValue.get('idservidor')
        ip = jsonValue.get('ip')
        nombre = jsonValue.get('nombre')

        try:
            cursor.execute("INSERT INTO servidor(ambiente, idservidor, ip, nombre) VALUES(%s, %s, %s, %s)",
            (ambiente, idservidor, ip,nombre))

            conn.commit()
            return "record inserted"

        except Exception as e:
            return json.dumps({'error':str(e)})
    else:
        return json.dumps({'error':'missing parameters'})


app.run(debug=True,host='0.0.0.0')

