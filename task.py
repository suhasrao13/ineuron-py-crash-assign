#functionality goes here

class DatabaseManage(object):

        def  __init__(self):
            global con
            try:
              con=lite.connect('course.db')
              cur=con.cursor()
              cur.execute("create table if not exists course(ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,description TEXT,Price TEXT,IS_private BOOLEAN NOT NULL DEFAULT 1)")
            except Exception:
              print("Unable to create DB !")
