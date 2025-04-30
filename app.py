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
        list_id = request.form.get("list")
        priority = request.form.get("priority")


        if text:
            # Insert the text into the database
            connection = get_db_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO tasks (title, list_id, priority) VALUES (%s, %s, %s)", (text, list_id, priority))
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

@app.route("/create_list", methods=["POST"])
def create_list():
    list_name = request.form.get("list_name")
    if list_name:
        # Insert the new list into the database
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO lists (name) VALUES (%s)", (list_name,))
        connection.commit()
        connection.close()
        return redirect(url_for("index"))

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    # Slett oppgaven fra databasen
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    connection.commit()
    connection.close()
    return redirect(url_for("index"))

@app.route("/update_status/<int:task_id>", methods=["POST"])
def update_status(task_id):
    data = request.get_json()
    completed = data.get("completed", False)
    if completed == True:
        completed = 0
    elif completed == False:
        completed = 1


    # Update the task status in the database
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE tasks SET status = %s WHERE id = %s", (completed, task_id))
        connection.commit()
        print(f"Task {task_id} status updated to {completed}.")
    except Exception as e:
        print(f"An error occurred while updating the task status: {e}")
        connection.rollback()
    finally:
        connection.close()

    return '', 204  # Return a no-content response

if __name__ == "__main__":
    app.run(debug=True)