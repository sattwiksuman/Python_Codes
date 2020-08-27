import sqlite3

def connect():
	conn=sqlite3.connect("fixture.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS fixture(id INTEGER PRIMARY KEY, date text, project text, package_code text, model text, test text, shaker text, fixZ text, fixXY text, coordinate text, remarks text)")
	conn.commit()
	conn.close()
	
def insert(date, project, package_code, model, test, shaker, fixZ, fixXY, coordinate, remarks):
	conn=sqlite3.connect("fixture.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO fixture VALUES(NULL,?,?,?,?,?,?,?,?,?,?)",(date, project, package_code, model, test, shaker, fixZ, fixXY, coordinate, remarks))
	conn.commit()
	conn.close()

def view():
	conn=sqlite3.connect("fixture.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM fixture")
	rows=cur.fetchall()
	conn.close()
	return rows

def search(date="", project="", package_code="", model="", test="", shaker="", fixZ="", fixXY="", coordinate="", remarks=""):
	conn=sqlite3.connect("fixture.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM fixture WHERE date=? OR project=? OR package_code=? OR model=? OR test=? OR shaker=? OR fixZ=? OR fixXY=? OR coordinate=? OR remarks=?", (date, project, package_code, model, test, shaker, fixZ, fixXY, coordinate, remarks))
	rows=cur.fetchall()
	conn.close()
	return rows
	
def delete(id):
	conn=sqlite3.connect("fixture.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM fixture WHERE id=?",(id,))
	conn.commit()
	conn.close()

def update(id, date, project, package_code, model, test, shaker, fixZ, fixXY, coordinate, remarks):
	conn=sqlite3.connect("fixture.db")
	cur=conn.cursor()
	cur.execute("UPDATE fixture SET date=?, project=?, package_code=?, model=?, test=?, shaker=?, fixZ=?, fixXY=?, coordinate=?, remarks=? WHERE id=?",(date, project, package_code, model, test, shaker, fixZ, fixXY, coordinate, remarks,id))
	conn.commit()
	conn.close()
	
connect()


