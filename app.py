from flask import Flask, render_template,request,redirect,url_for,flash
from flaskext.mysql import MySQL
import app


app = Flask(__name__)

#MYSQL CONNECTION
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='contactos'
mysql = MySQL()
mysql.init_app(app)

#SETTINGS
app.secret_key ='mysecretkey'

@app.route("/")
def login():
    return render_template('login.html')
@app.route("/registro")
def register():
    return render_template('register.html')
@app.route("/add_contact", methods=['POST'])
def add_contact():

    if request.method == 'POST':
        name = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cursor = mysql.get_db().cursor()
        cursor.execute(' INSERT INTO contacs (nombre, telefono, email) VALUES (%s, %s, %s)', (name, phone, email))
        print(name)
        flash('Se guardo el contacto satisfactoriamente')
        return redirect(url_for('login'))

if __name__=='__main__':
    app.run(port=3000, debug=True)