class CSVSave():

    def save(self, *args, **kwargs):
        header_str = ''
        value_str = ''

        request_data = self.__dict__
        request_data['id'] = self.get_new_id()

        for key, val in request_data.items():
            header_str = header_str + f'{key},'
            value_str = value_str + f'{val},'

        try:
            with open(f"{self.__class__.__name__}.csv", 'r+') as csv_file:
                header_item = csv_file.readlines()
                if len(header_item) > 0:
                    csv_file.writelines(f'{value_str}\n')

                else:
                    csv_file.writelines(f'{header_str}\n')
                    csv_file.writelines(f'{value_str}\n')
        except FileNotFoundError:  
            with open(f"{self.__class__.__name__}.csv", 'w+') as csv_file:
                header_item = csv_file.readlines()
                if len(header_item) > 0:
                    csv_file.writelines(f'{value_str}\n')
                    print('Item Saved Successfully!!!')


                else:
                    csv_file.writelines(f'{header_str}\n')
                    csv_file.writelines(f'{value_str}\n')
                    print('Item Saved Successfully!!!')
        

    def create(self, validated_data, *args, **kwargs):

        header_str = ''
        value_str = ''

        # request_data = self.__dict__
        validated_data['id'] = self.get_new_id()

        for key, val in validated_data.items():
            header_str = header_str + f'{key},'
            value_str = value_str + f'{val},'

        try:
            with open(f"{self.__class__.__name__}.csv", 'r+') as csv_file:
                header_item = csv_file.readlines()
                if len(header_item) > 0:
                    csv_file.writelines(f'{value_str}\n')

                else:
                    csv_file.writelines(f'{header_str}\n')
                    csv_file.writelines(f'{value_str}\n')
        except FileNotFoundError:  
            with open(f"{self.__class__.__name__}.csv", 'w+') as csv_file:
                header_item = csv_file.readlines()
                if len(header_item) > 0:
                    csv_file.writelines(f'{value_str}\n')
                    print('Item Saved Successfully!!!')


                else:
                    csv_file.writelines(f'{header_str}\n')
                    csv_file.writelines(f'{value_str}\n')
                    print('Item Saved Successfully!!!')

    def delete(self,id):
        try:
            with open(f"{self.__class__.__name__}.csv", 'r') as csv_file:
                data = csv_file.readlines()
                for index, item in enumerate(data):
                    item_id =  item.split(',')[0]
                    if str(item_id) ==  str(id):
                        data.pop(index)   
        except FileNotFoundError:
            print('FILE NOT FOUND')

        try:
            with open(f"{self.__class__.__name__}.csv", 'w') as csv_file:
                csv_file.writelines(data)
                print('Deleted !!!!')


        except FileNotFoundError:
            print('file Not Found')


    def update(self, validated_data, *args, **kwargs):
        request_data = validated_data
        required_fields  =  self.__dict__.keys()
        for item in required_fields:
            if item not in request_data.keys():
                print(f'{item} is requeired Field')
                return 
        try:
            with open(f"{self.__class__.__name__}.csv", 'r') as csv_file:
                data = csv_file.readlines()
                ids =  [item.split(',')[0] for item in data]
                if str(request_data.get('id')) not in ids:
                    print("Id Doesn't Exists!!!")
                    return  

        except FileNotFoundError:
            print('FIle NOt FOund')

        data_str = ''
        for item in request_data.values():
            data_str += f'{item}, '
        
        data_str+='\n'

        try:
            for index, item in enumerate(data):
                    item_id =  item.split(',')[0]
                    if str(item_id) ==  str(request_data.get('id')):
                        data[index] = data_str                    

        except Exception as e:
            print(f'{e}')
        try:
            with open(f"{self.__class__.__name__}.csv", 'w') as csv_file:
                csv_file.writelines(data)
                print('Data updated Successfully!!')
        except FileNotFoundError:
            print('file NOt FOund')

    def get(self, id):
        try:
            with open(f"{self.__class__.__name__}.csv", 'r') as csv_file:
                data = csv_file.readlines()
                if id > 0 :
                    for index, item in enumerate(data):
                        item_id =  item.split(',')[0]
                        if str(item_id) ==  str(id) :
                            resp_data =   data.pop(index) 
                            print(resp_data)
                            return resp_data
                else:
                    for data_item in data:
                        print(data_item)
        except FileNotFoundError:
            print('FILE NOT FOUND')

    def get_new_id(self):
        try:
            with open(f"{self.__class__.__name__}.csv", 'r') as csv_file:
                content = csv_file.readlines()
                print(content)
                if len(content) > 0:
                    last_id = int(content[-1].split(',')[0])
                    return last_id + 1
                else:
                    return 1
        except Exception as e:
            return 1


class StudentModel(CSVSave):

    def __init__(self, name, grade, address, roll_number, contact, *args, **kwargs):
        self.id = kwargs.get('id', 0)
        self.name = name
        self.grade = grade
        self.address = address
        self.roll_number = roll_number
        self.contact = contact


student = StudentModel(name='sagar', grade='twelve',
                       address='ktm', roll_number=12, contact='987654')

student2 = StudentModel(id=4,  name='Sagarrrrsss', grade='twelve',
                        address='ktm', roll_number=12, contact='9876543')




class Animal(CSVSave):
    def __init__(self, name,  height, weight, *args, **kwargs) -> None:
        self.id  =  kwargs.get('id', 0)
        self.name =  name
        self.height =  height
        self.weight =  weight
        super().__init__()


instance =  Animal(name=None, height=None, weight=None)

while True:

    print('\nChoose What you want to do!!')

    print("""
        OPTIONS: 
        To Create: (C)
        To Read : (R)
        To Update : (U)
        To Delete : (D)
        To Quit : (Q)""")
            
    option =  input('Choose: ').upper()

    if option  =='C':
        data= {'id': 0}
        for item in instance.__dict__.keys():
            if item != 'id':
                item_inp =  input(f'{item}: ' )
                data[f'{item}']= item_inp


        instance.create(validated_data=data)

    elif option =='R':
        print('TOtal or Partial')
        r_type = input('Choose (T) For Total & (P) For Partial: ')
        if r_type.upper()=='P':
            item_id = input('Choose Item Id: ')
            header =  ''
            for i in instance.__dict__:
                header += f'{i}, '
            print(header)
            instance.get(item_id)
        
        if r_type.upper()=='T':
            print('Full Item is Fetching... \n')
            instance.get(0)

    elif option =='U':
        u_id = int(input('Choose Id: '))
        if u_id  > 0:
            data = instance.get(u_id)
            list_of_data  = data.split(',')   
            print('Skip For Default value')
            updated_data =  {}
            for index, item in enumerate(instance.__dict__):
                updated_data[f'{item}'] =  list_of_data[index]
                if item == 'id':
                    continue

                else:
                    input_data =  input(f'{item} ({list_of_data[index]}): ')
                    if input_data.strip():
                        updated_data[f'{item}'] =  input_data
                    else:
                        updated_data[f'{item}'] =  list_of_data[index]

            print(updated_data)
            instance.update(validated_data=updated_data)
        else:
            print('Invalid Id Provided')
    
    elif option =='D':
        try:
            item_id =  int(input('Choose Id To Delete: '))
        except Exception as e:
            print(f'Error : {e}')
        
        instance.delete(item_id)
    
    elif option =='Q':
        print('\nAbortted!!!')
        break

    else:
        print('\nInvalid Options')






