"""
Setup script for the Python Pulse SQLite database used by tests.

This script creates the expected tables and inserts sample data. The tests
expect the database file to live next to this script (project root). To be
robust regardless of working directory when the script is executed, the
database path is built relative to this file.
"""
import os
import sqlite3


# Build path to DB file next to this script (project root)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "python_pulse.db")


def main():
    # Connect to the DB file (will be created if missing)
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    # Drop existing tables if present so tests get a clean schema
    cursor.execute("DROP TABLE IF EXISTS user_workout")
    cursor.execute("DROP TABLE IF EXISTS workouts")
    cursor.execute("DROP TABLE IF EXISTS goals")
    cursor.execute("DROP TABLE IF EXISTS profiles")
    cursor.execute("DROP TABLE IF EXISTS users")

    # Create users table with expected column names
    cursor.execute("""
    CREATE TABLE users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        email TEXT
    )
    """)

    # Create profiles table (notes column name expected by tests)
    cursor.execute("""
    CREATE TABLE profiles (
        profile_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        height INTEGER,
        weight INTEGER,
        age INTEGER,
        notes TEXT,
        FOREIGN KEY(user_id) REFERENCES users(user_id)
    )
    """)

    # Insert sample users
    users_data = [
        ('john_doe', 'password123', 'john_doe@gmail.com'),
        ('jane_smith', 'mypassword', 'jane@gmail.com'),
        ('alice_jones', 'alicepassword', 'ajones@yahoo.com'),
        ('bob_brown', 'bobpassword', 'bobby@yahoo.com'),
        ('rebecca_charles', 'rebeccapassword', 'becky123@gmail.com')
    ]
    cursor.executemany(
        "INSERT INTO users (username, password, email) VALUES (?, ?, ?)", users_data
    )

    # Insert sample profiles (matches tests' expected SELECT order)
    profiles_data = [
        (1, 180, 75, 28, 'Loves hiking and outdoor activities.'),
        (2, 165, 60, 25, 'Enjoys painting and art.'),
        (3, 170, 65, 30, 'Passionate about technology and coding.'),
        (4, 175, 80, 22, 'Avid reader and writer.'),
        (5, 160, 50, 27, 'Fitness enthusiast and gym lover.')
    ]
    cursor.executemany(
        "INSERT INTO profiles (user_id, height, weight, age, notes) VALUES (?, ?, ?, ?, ?)", profiles_data
    )

    # Create goals table with expected column names
    cursor.execute("""
    CREATE TABLE goals (
        goal_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        target_value INTEGER,
        user_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(user_id)
    )
    """)

    goals_data = [
        ('Run 5km', 5, 1),
        ('Lose 10kg', 10, 2),
        ('Lift 100kg 3x', 100, 3),
        ('Meditate daily', 1, 5),
        ('Cycle 100km', 100, 4),
        ('Complete a marathon', 42, 5),
        ('Run 5 km', 5, 5)
    ]
    cursor.executemany(
        "INSERT INTO goals (name, target_value, user_id) VALUES (?, ?, ?)", goals_data
    )

    # Create workouts table with expected column names
    cursor.execute("""
    CREATE TABLE workouts (
        workout_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT,
        duration INTEGER
    )
    """)

    workouts_data = [
        ('Morning Yoga', 'A refreshing morning yoga session.', 30),
        ('HIIT Workout', 'High-Intensity Interval Training.', 45),
        ('Weightlifting', 'Full body weightlifting session.', 60),
        ('Cycling', 'Outdoor cycling for endurance.', 120),
        ('Meditation', 'Guided meditation for relaxation.', 15)
    ]
    cursor.executemany(
        "INSERT INTO workouts (name, description, duration) VALUES (?, ?, ?)", workouts_data
    )

    # Create user_workout junction table (tests expect this exact name and shape)
    cursor.execute("""
    CREATE TABLE user_workout (
        user_id INTEGER,
        workout_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(user_id),
        FOREIGN KEY(workout_id) REFERENCES workouts(workout_id)
    )
    """)

    user_workouts_data = [
        (1, 1),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 1),
        (5, 2)
    ]
    cursor.executemany(
        "INSERT INTO user_workout (user_id, workout_id) VALUES (?, ?)", user_workouts_data
    )

    # Commit and close
    connection.commit()
    connection.close()


if __name__ == "__main__":
    main()