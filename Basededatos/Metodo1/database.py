import sqlite3

conn = sqlite3.connect('database.db')
print "Opened database successfully";

conn.execute('CREATE TABLE tareas (numtar INTEGER, destar TEXT, temtar TEXT, fectar TEXT, hortar TEXT, lintar TEXT)')
print "Table created successfully";
conn.close()
