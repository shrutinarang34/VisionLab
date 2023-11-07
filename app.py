from flask import Flask, render_template, request, redirect, url_for
import sqlite3


app = Flask(__name__)
conn = sqlite3.connect("STUDENT.db")

@app.route('/student', methods=['POST', 'GET'])
def student():
    if request.method == 'POST':
        try:
            First_Name = request.form['First_Name']
            Last_Name = request.form['Last_Name']
            Email = request.form['Email']
            Mobile_Number = request.form['Mobile_Number']

            with sqlite3.connect("STUDENT.db") as conn:
                cur = conn.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS STU_LIST (First_Name TEXT, Last_Name TEXT, Email TEXT PRIMARY KEY, Mobile_Number INTEGER)')
                cur.execute("INSERT INTO STU_LIST (First_Name, Last_Name, Email, Mobile_Number) VALUES (?, ?, ?, ?)", (First_Name, Last_Name, Email, Mobile_Number))
                conn.commit()

            return redirect(url_for('index'))
        except Exception as e:
            return f"An error occurred: {str(e)}"
    else:
        return "Invalid request method."




@app.route('/')
def index():
    conn = sqlite3.connect("STUDENT.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM STU_LIST")
    rows = cur.fetchall()
    return render_template("index.html", data=rows)



if __name__ == '__main__':
    app.run()


