from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'todo_user',
    'password': 'todo_password',  # Use the password you set in db.sql
    'db': 'todo_app',
    'cursorclass': pymysql.cursors.DictCursor
}

# Helper function to get a database connection
def get_db_connection():
    return pymysql.connect(**db_config)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get text from the input field
        text = request.form.get("text_input")
        if text:
            # Insert the text into the database
            connection = get_db_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO tasks (title) VALUES (%s)", (text,))
            connection.commit()
            connection.close()

    # Fetch all tasks from the database
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        cursor.execute("SELECT * FROM lists")
        lists = cursor.fetchall()
    connection.close()

    # Pass the tasks to the template
    return render_template("index.html", text_list=tasks, lists=lists)

if __name__ == "__main__":
    app.run(debug=True)