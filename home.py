from flask import Flask,render_template ,request,redirect,url_for   #Flask  (classname)
app = Flask(__name__)
import sqlite3

con=sqlite3.connect('database.db')
try:
    con.execute('create table contact (name TEXT , email TEXT , phone TEXT , message TEXT)')
except:
    pass

@app.route('/')
def fun1():
    return render_template("index.html")


@app.route('/',methods=['POST','GET'])
def fun2():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        phone=request.form['number']
        message=request.form['message']
        con=sqlite3.connect('database.db')
        con.execute("insert into contact(name,email,phone,message)values(?,?,?,?)",(name,email,phone,message))
        con.commit()
        print(name,email,phone,message)
        return redirect(url_for('fun1'))
    else:
        return render_template('index.html')


app.run()