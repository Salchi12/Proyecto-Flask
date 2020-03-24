from flask import Flask, render_template, request, redirect, url_for,flash
from flaskext.mysql import MySQL

app = Flask(__name__)


#MySQL config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'contactos'
mysql = MySQL()
mysql.init_app(app)

#Settings

#app.secret_key = 'mysecretkey'

@app.route('/')
def login():
	cur = mysql.get_db().cursor()
	cur.execute('SELECT email FROM contacs')
	data = cur.fetchall()
	print(data)
	return render_template('login.html')

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/datos', methods=['POST'])
def datos():
	if request.method =='POST':
		fullname = request.form['fullname']
		phone = request.form['phone']
		email = request.form['email']
		password = request.form['password']
		cur = mysql.connection.cursor()
		cur.execute('INSERT INTO contacs (fullname, phone, email, password) VALUES (%s, %s, %s, %s)', 
			(fullname, phone, email, password))
		mysql.connection.commit()
		flash('CONTACTO CREADO')
		return redirect(url_for('login'))


@app.route('/validar', methods=['POST'])
def validar():
	if request.method == 'POST':
		usuario = request.form['user']
		contraseña = request.form['password']
	if (usuario == "salchi") and (contraseña == "123456"):
		return home()
	else:
		return login()

@app.route('/home')
def home():
	return render_template('home.html')
	
@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == '__main__':
	app.run(port = 5000,debug=True)
