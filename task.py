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


def main():
  print("*"*40)
  print("\n::COURSE MANAGEMENT ::\n")

 
  db = DatabaseManage()

  print("#"*40)
  print("\n::user Manual::\n")
  print('press 1.Insert a new course')
  print('press 2.show all courses')
  print('press 3.Delete a course (ned id of course)')

  choice= input("\nEnter your choice:")
  
  if choice=='1':
    name=input("\n Enetr course name :")
    description=input("\n Enetr description name :")
    price=input("\nEnter the price :")
    private=input("\Is this course private(0/1):")
 
    if db.insert_data([name,description,price,private]):
      print("Course inserted successfully")
    else:
      print("OOPS something error")
    
  elif choice=='2':
    print("\n::COURSE list::")

    for index,item in enumerate(db.fetech_dtaa()):
      print("\n Sl no:" +str(index +1))
      print("Course ID :"+str(item[0]))
      print("Course name :"+str(item[1]))
      print("Course description:"+str(item[2]))
      print("Course price :"+str(item[3]))
      private = 'yes' if item[4] else 'NO'
      print("IS private:"+private)
      print("\n")
      #print("Course private :"+str(item[4]))

  elif choice=='3':
    record_id=int(input("\nEnter the id of the course you want to delete:"))
    if db.delete_data(record_id):
      print("Course was deleted successfully")
    else:
      print("OOPS something error")
    
  else:
    print("\n BAD CHOICE:")

if __name__=='__main__':
  main()

