import mysql.connector

midb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="prueba"
)

# Cursor: Es el objeto que nos permite interactuar con la base de datos mediante el lenguaje SQL
cursor = midb.cursor()

# Ahora podemos hacer consultas SQL
#Listar datos
#cursor.execute("SELECT * FROM Usuario")
# resultado = cursor.fetchall()
# print(resultado)

# Ver definiciones de tablas
# cursor.execute('show create table Usuario')

# Insertar datos
sql = 'insert into Usuario (email, username, edad) values (%s, %s, %s)'
values = ('cintia@correo.com', 'CintiaU', 27)

cursor.execute(sql, values)

# Guardamos los cambios
midb.commit()

print(cursor.rowcount)

