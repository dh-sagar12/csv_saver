import psycopg2

class PgConnection():

    def __init__(self, db_host, db_name,  db_user, db_password):
        self.db_host  =  db_host
        self.db_name  =  db_name
        self.db_user  =  db_user
        self.db_password  =  db_password

    

    def get_connection(self):
        try:
            # conn = psycopg2.connect(database = self.db_name, user  = self.db_user, password=  self.db_password, host=  self.db_host)
            conn =  psycopg2.connect(f"dbname={self.db_name} user={self.db_user} password={self.db_password}")
            conn.autocommit = True
        except Exception as e:
            print(e)
            return e
        curr =  conn.cursor()
        return curr


    def FetchData(self, sql, *args):
        curr =   self.get_connection()
        curr.execute(sql)
        result =  [dict(zip([column[0] for column in curr.description], row))
                for row in curr.fetchall()]
        
        return result


    
    def Commit(self):
        conn =  psycopg2.connect(f"dbname={self.db_name} user={self.db_user} password={self.db_password}")
        return conn.commit()



pg_instance  =  PgConnection(db_host='localhost', db_name='news', db_password='*****', db_user='postgres')