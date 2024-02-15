from flask import Flask, request, render_template
import mysql.connector  # Reemplaza esto con el conector de tu base de datos


app = Flask(__name__)

# Configuración de la conexión a la base de datos
db = mysql.connector.connector(
    host='localhost',
    user='root',
    password='',
    database='danza'  # Nombre de tu base de datos
)
if db.is_connected():
    print("Conexión exitosa a la base de datos")
else:
    print("Error al conectarse a la base de datos")
@app.route('/')
def formulario():
    return render_template('academia.html')
@app.route('/guardar_datos', methods=['POST'])
def guardar_datos():
    cursor = db.cursor()

    # Obtener los datos del formulario
    nombre_academia = request.form['nombre_academia']
    direccion = request.form['direccion']
    email = request.form['email']
    telefono = request.form['telefono']

    # Consulta SQL para insertar los datos en la tabla Academia (por ejemplo)
    sql = "INSERT INTO Academia (nombre_Academia, direccion_Academia, email_Academia, telefono_Academia) VALUES (%s, %s, %s, %s)"
    val = (nombre_academia, direccion, email, telefono)

    cursor.execute(sql, val)
    db.commit()
    db.close()
    return 'Datos guardados en la base de datos.'
    
if __name__ == '__main__':
    app.run(debug=True)
