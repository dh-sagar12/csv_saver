import jwt
import db
from models import Users, AuthToken
import datetime



JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 200


class Authenticate():
    def __init__(self) -> None:
        self.token =  None

    def create_user(self,username, password):
        user = Users(username=username, password=password)
        already_created =  user.get(username=username)
        print('already_created', already_created)
        if len(already_created) > 0:
            print('User Already Created With this username')
            return 'User Already Created With this username'
        else:
            user.create()
            return 'User Created Successfully!!!'

    
    def login(self, username, password):
        user = Users()
        data = user.get(username=username)
        if len(data)> 0 and data[0].get('password') == password:
            payload = {
            'user_id': data[0].get('id'),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=JWT_EXP_DELTA_SECONDS)
             }
            jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
            self.token  =  jwt_token

            token_model  =  AuthToken(token=self.token, user_id=data[0].get('id'), is_active=True)
            token_model.revoke_auth_token(user_id=data[0].get('id'))
            token_model.create()
            print('User Logged In successfully')
            return data[0].get('id')

        else:
            print('invalid credentials')
            return None
    
    def verify_user(self, user_id):
        token_model  =  AuthToken()
        active_jwt  =  token_model.get_active(user_id= user_id)[0].get('token')
        self.token  =  active_jwt        
        try:
           data =  jwt.decode(self.token, JWT_SECRET, algorithms=JWT_ALGORITHM)
           return data
        except Exception as e:
            return {'error': f'{e}'}



authenticateInstance =  Authenticate()
# authenticateInstance.login(username='sagar1', password='1234')
authenticateInstance.verify_user(5)