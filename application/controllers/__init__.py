import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>hola mamor</h1><p>soy un srvicio web.</p>"

app.run(debug=True,host='0.0.0.0')

