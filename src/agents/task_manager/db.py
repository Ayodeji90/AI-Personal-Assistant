import sqlite3

class TaskDatabase:
    def __init__(self, db_name="tasks.db"):
        """Initialize database connection and create tasks table if not exists."""
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_table()

    def create_table(self):
        """Create the tasks table."""
        query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            priority TEXT CHECK(priority IN ('Urgent', 'High', 'Medium', 'Low')) NOT NULL,
            due_date TEXT NOT NULL,
            status TEXT CHECK(status IN ('Pending', 'Completed')) DEFAULT 'Pending'
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_task(self, title, category, priority, due_date):
        """Insert a new task into the database."""
        query = """
        INSERT INTO tasks (title, category, priority, due_date, status)
        VALUES (?, ?, ?, ?, 'Pending');
        """
        self.conn.execute(query, (title, category, priority, due_date))
        self.conn.commit()

    def get_tasks(self, status=None):
        """Retrieve tasks from the database, optionally filtered by status."""
        query = "SELECT * FROM tasks"
        if status:
            query += " WHERE status = ?"
            return self.conn.execute(query, (status,)).fetchall()
        return self.conn.execute(query).fetchall()

    def update_task(self, task_id, title=None, category=None, priority=None, due_date=None):
        """Update an existing task's details."""
        query = "UPDATE tasks SET "
        updates = []
        params = []

        if title:
            updates.append("title = ?")
            params.append(title)
        if category:
            updates.append("category = ?")
            params.append(category)
        if priority:
            updates.append("priority = ?")
            params.append(priority)
        if due_date:
            updates.append("due_date = ?")
            params.append(due_date)

        if not updates:
            return  # Nothing to update

        query += ", ".join(updates) + " WHERE id = ?"
        params.append(task_id)

        self.conn.execute(query, tuple(params))
        self.conn.commit()

    def mark_completed(self, task_id):
        """Mark a task as completed."""
        query = "UPDATE tasks SET status = 'Completed' WHERE id = ?"
        self.conn.execute(query, (task_id,))
        self.conn.commit()

    def delete_task(self, task_id):
        """Delete a task by ID."""
        query = "DELETE FROM tasks WHERE id = ?"
        self.conn.execute(query, (task_id,))
        self.conn.commit()

    def close(self):
        """Close the database connection."""
        self.conn.close()
