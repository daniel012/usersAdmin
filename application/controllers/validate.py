def createRecords(jsonValue):
  ambiente = jsonValue.get('ambiente')
  idservidor = jsonValue.get('idservidor')
  ip = jsonValue.get('ip')
  nombre = jsonValue.get('nombre')
  return 'ambiente' in jsonValue and 'idservidor' in jsonValue and 'ip' in jsonValue and 'nombre' in jsonValue
