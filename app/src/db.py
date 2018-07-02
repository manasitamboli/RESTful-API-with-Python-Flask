#import MySQLdb
import sqlite3 as sql

def get_connector():
    db = sql.connect("users.db" )
    return db

def close_db(db):
    db.close()

def get_users_from_db():
    db = get_connector()
    cursor = db.cursor()
    cursor.execute("SELECT * from users")
    data = cursor.fetchall()
    close_db(db)
    return data

def get_single_user_from_db(username):
    db = get_connector()
    cursor = db.cursor()
    cursor.execute("SELECT * from users where username='" + username + "'")
    data = cursor.fetchone()
    close_db(db)
    return data

def add_user_to_db(user):
    db = get_connector()
    cursor = db.cursor()
    flag = True
    try:
        cursor.execute("INSERT into users (username, displayname, department) values ('" + user['username']+ "', '" + user['displayName']+ "', '" + user['department'] + "')")
        db.commit()
    except:
        db.rollback()
        flag = False
    close_db(db)
    return flag

def delete_user_from_db(username):
    db = get_connector()
    cursor = db.cursor()
    flag = True
    try:
        cursor.execute("DELETE from users where username='" + username + "'")
        db.commit()
    except:
        db.rollback()
        flag = False
    close_db(db)
    return flag

