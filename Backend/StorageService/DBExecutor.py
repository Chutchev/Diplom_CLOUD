import sqlite3

def create_db():
    with sqlite3.connect("files.db") as conn:
        conn.execute("""CREATE TABLE FILES
        (
            filename VARCHAR(255),
            path VARCHAR(10000),
            username VARCHAR(255),
            filetype VARCHAR(255),
            md5_sum varchar(40)
        );""")


def add_file(filename, path, user, filetype, md5_sum):
    params = (filename, path, user, filetype, md5_sum)
    with sqlite3.connect("files.db") as conn:
        conn.execute("INSERT INTO FILES (filename, path, username, filetype, md5_sum) VALUES (?, ?, ?, ?, ?)", params)


def get_file(username):
    with sqlite3.connect("files.db") as conn:
        cur = conn.cursor()
        data = cur.execute(f"SELECT * FROM FILES WHERE username='{username}'")
        return data.fetchall()

def get_filepath(filename):
    with sqlite3.connect("files.db") as conn:
        cur = conn.cursor()
        data = cur.execute(f"SELECT path FROM FILES WHERE filename='{filename}'")
        return data.fetchone()