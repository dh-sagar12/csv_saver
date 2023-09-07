import db

class NewsModel():
    def __init__(self, id=None, title =None, description=None) -> None:
        self.id  =  id
        self.title =  title
        self.description = description
    
    def create(self, *args, **kwargs):
        sql =  f"INSERT INTO {self.__class__.__name__}(title, description) values ('{self.title}', '{self.description}')"
        connection =   db.pg_instance.get_connection()
        connection.execute(sql)
        db.pg_instance.Commit()

    def get(self, id=None, *args, **kwargs):
        if id is not None:
            sql =  f"SELECT * FROM newsmodel WHERE ID  = {id}"
            data =  db.pg_instance.FetchData(sql)
            return data
        else:
            sql =  f"SELECT * FROM newsmodel"
            data =  db.pg_instance.FetchData(sql)
            return data

    def delete(self, id):
        sql =  f"DELETE FROM {self.__class__.__name__} WHERE id =  {id}"
        connection =   db.pg_instance.get_connection()
        connection.execute(sql)
        db.pg_instance.Commit()
    
    def update(self, data,  *args, **kwargs):
        print(data)
        sql  = 'UPDATE newsmodel SET  '
        for key, value in data.items():
            if key != 'id':
                sql += f"{key} =  '{value}', "
        

        sql = sql[:len(sql)-2]
        sql += f" WHERE id  = {data.get('id')}"
        connection =   db.pg_instance.get_connection()
        connection.execute(sql)
        db.pg_instance.Commit()        
        print('\nNews Updated Successfully!!!')




class Users():
    def __init__(self, id=None, username =None, password=None) -> None:
        self.id  =  id
        self.username =  username
        self.password = password
    


    def create(self, *args, **kwargs):
        sql =  f"INSERT INTO {self.__class__.__name__}(username, password) values ('{self.username}', '{self.password}')"
        connection =   db.pg_instance.get_connection()
        print(sql)
        connection.execute(sql)
        db.pg_instance.Commit()

    def get(self, id= None, username  = None,  *args, **kwargs):
        sql = f"SELECT * FROM users WHERE id =  {id if id is not None else 0} OR username =  '{username if username is not None else ''}'"
        data = db.pg_instance.FetchData(sql)
        return data


class AuthToken():
    def __init__(self, id=None, user_id =None, token=None, is_active =None) -> None:
        self.id  =  id
        self.user_id =  user_id
        self.token = token
        self.is_active = is_active

    
    def create(self, *args, **kwargs):
        sql =  f"INSERT INTO auth_token (user_id, token, is_active) values ('{self.user_id}', '{self.token}', '{self.is_active}' )"
        connection =   db.pg_instance.get_connection()
        connection.execute(sql)
        db.pg_instance.Commit()

    def get_active(self, user_id, *args, **kwargs):
        sql = f"SELECT * FROM auth_token WHERE user_id =  {user_id} and is_active"
        data = db.pg_instance.FetchData(sql)
        return data
    
    @staticmethod
    def revoke_auth_token(user_id):
        connection =   db.pg_instance.get_connection()
        sql =  f"UPDATE auth_token SET is_active = false WHERE user_id = {user_id} AND is_active"
        connection.execute(sql)
        db.pg_instance.Commit()


# user  =  Users()
# user.get(username='sagar')

