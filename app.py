# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 23:11:00 2024

@author: Dreamer
"""

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    return conn

# Route: Home page
@app.route('/')
def index():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

# Route: Add task
@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        task = request.form['task']
        time = request.form['time']
        responsible = request.form['responsible']

        conn = get_db_connection()
        conn.execute(
            'INSERT INTO tasks (task, time, responsible) VALUES (?, ?, ?)',
            (task, time, responsible)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')

# Route: Update task
@app.route('/update/<int:id>', methods=('GET', 'POST'))
def update(id):
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        new_task = request.form['task']
        new_time = request.form['time']
        new_responsible = request.form['responsible']

        conn.execute(
            'UPDATE tasks SET task = ?, time = ?, responsible = ? WHERE id = ?',
            (new_task, new_time, new_responsible, id)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    conn.close()
    return render_template('update.html', task=task)

# Route: Delete task
@app.route('/delete/<int:id>', methods=('POST',))
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
