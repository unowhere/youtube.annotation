import sqlite3
import os

# Determine the absolute path for the database file
# Assuming this file (database.py) is in HabitFlow/src/
# So, ../data/ will be HabitFlow/data/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, '..', 'data', 'habitflow.db')

def get_db_connection():
    """Establishes a connection to the SQLite database."""
    # Ensure the data directory exists
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    conn = sqlite3.connect(DATABASE_PATH)
    # Optional: Enable foreign key constraint enforcement (good for development)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def create_tables():
    """Creates the necessary tables in the database if they don't already exist."""
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS habit_categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                color TEXT,
                icon_path TEXT,
                description TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS habits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                category_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES habit_categories (id)
                    ON DELETE SET NULL ON UPDATE CASCADE
            )
        ''')
        # Added ON DELETE SET NULL and ON UPDATE CASCADE for better FK handling

        conn.commit()
        print("Database tables created or already exist.")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")
    finally:
        if conn:
            conn.close()

def add_default_habit_categories():
    """Adds predefined habit categories to the database if they don't already exist."""
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        default_categories = [
            ("Health & Fitness", "red", None, "Habits related to physical well-being"),
            ("Productivity", "blue", None, "Habits related to efficiency and work"),
            ("Learning", "green", None, "Habits related to acquiring knowledge"),
            ("Mindfulness", "purple", None, "Habits related to mental peace and awareness")
        ]

        # Use INSERT OR IGNORE to avoid errors if categories already exist
        cursor.executemany('''
            INSERT OR IGNORE INTO habit_categories (name, color, icon_path, description)
            VALUES (?, ?, ?, ?)
        ''', default_categories)

        conn.commit()
        print(f"{cursor.rowcount} default categories processed/added.")
    except sqlite3.Error as e:
        print(f"Error adding default habit categories: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    # For direct testing of this module
    print(f"Database path: {DATABASE_PATH}")
    create_tables()
    add_default_habit_categories()

    # Example: Querying the categories to verify
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM habit_categories")
    rows = cursor.fetchall()
    print("\nHabit Categories in DB:")
    for row in rows:
        print(row)
    conn.close()
