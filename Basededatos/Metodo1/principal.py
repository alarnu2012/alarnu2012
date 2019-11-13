from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('tareas.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         numtar = request.form['numtar']
         destar = request.form['destar']
         temtar = request.form['temtar']
         fectar = request.form['fectar']
         hortar = request.form['hortar']
         lintar = request.form['lintar']

         with sql.connect("database.db") as con:
            cur = con.cursor()

            cur.execute("INSERT INTO tareas (numtar,destar,temtar,fectar,hortar,lintar) VALUES (?,?,?,?,?,?)",(numtar,destar,temtar,fectar,hortar,lintar) )

            con.commit()
            msg = "Tarea fue Agreagado Correctamente"
      except:
         con.rollback()
         msg = "error in insert operation"

      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from tareas")

   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

@app.route("/delete")
def delete():
    return render_template("delete.html")


@app.route("/deleterecord",methods = ["POST"])
def deleterecord():
    numtar2 = request.form["numtar"]

    with sql.connect("database.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from tareas where numtar = ?",(numtar2,))
            print "borrando " + numtar2
            con.commit()
            msg = "record successfully deleted"
        except:
            con.rollback()
            msg = "can't be deleted"
        finally:
            return render_template("delete_record.html",msg = msg)

@app.route("/update")
def update():
    return render_template("update.html")

@app.route("/updaterecord",methods = ["POST"])
def updaterecord():
    numtar2 = request.form["numtar"]

    with sql.connect("database.db") as con:
       cur = con.cursor()
       cur.execute("select * from tareas where numtar = ?",(numtar2,))
       row = cur.fetchone();
       print row
    return render_template("update_record.html",row = row)

@app.route("/update_record",methods = ["POST"])
def update_record():
    numtar2 = request.form["oldname"]
    numtar1 = request.form["name"]
    destar  = request.form["destar"]

    with sql.connect("database.db") as con:
       cur = con.cursor()
       cur.execute("update tareas set numtar = ?, destar = ? where numtar = ?",(numtar1,numtar2,destar))

    return redirect(url_for('list'))
   

if __name__ == '__main__':
   app.run(debug = True)
