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

         def insert_data(self, data):
          try:
            with con:
              cur=con.cursor()
              cur.execute("INSERT INTO COURSE(name,descrption,price,is_private) VALUES(?,?,?,?)",data)
            return True
          except Exception:
            return False
      #read data
        def fetch_adata(self):
          try:
            with con:
              cur=con.cursor()
              cur.execute('SELECT * FROM COURSES')
              return cur.fetchall()
          except Exception:
            False
        
        def delete_data(self,id):
          try:
            with con:
              cur=con.cursor()
              cur.execute()
              sql="DELETE FROM course WHERE id=?"
              cur.execute(sql,[id])
              return True
          except Exception:
            return False        
