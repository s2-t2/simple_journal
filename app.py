#!/usr/bin/python

from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    date = request.form['date']
    title = request.form['title']
    content = request.form['content']

    # Save the journal entry to a SQLite database
    conn = sqlite3.connect('journal.db')
    c = conn.cursor()
    c.execute("INSERT INTO entries (date, title, content) VALUES (?, ?, ?)", (date, title, content))
    conn.commit()
    conn.close()

    return 'Journal entry saved!'

@app.route('/entries')
def entries():
    conn = sqlite3.connect('journal.db')
    c = conn.cursor()
    c.execute("SELECT * FROM entries ORDER BY date DESC")
    entries = c.fetchall()
    conn.close()
    return render_template('entries.html', entries=entries)


app.run()


