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


    def update(self, *args, **kwargs):
        request_data = kwargs
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
        except FileNotFoundError:
            print('file NOt FOund')

    def get(self, id):
        try:
            with open(f"{self.__class__.__name__}.csv", 'r') as csv_file:
                data = csv_file.readlines()
                for index, item in enumerate(data):
                    item_id =  item.split(',')[0]
                    if str(item_id) ==  str(id):
                        resp_data =   data.pop(index)   
                        print(resp_data)
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

# student.save()
# student_4 =  StudentModel()
# student2.update()
# student2.get(2)

# student2  = StudentModel(id=2, name='adsfasdf')

class Animal(CSVSave):
    def __init__(self, height, weight, *args, **kwargs) -> None:
        self.id  =  kwargs.get('id', 0)
        self.height =  height
        self.weight =  weight
        super().__init__()



a =  Animal(  height=20, weight=100)
# a.save()
a.update(id=  2, height = 200, weight =  500)