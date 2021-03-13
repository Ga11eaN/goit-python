from collections import UserDict, UserList, UserString


class Field():
    pass
  
class Name(UserString, Field, ):
    pass
    
class Phone(UserList, Field,):
    pass

class AddressBook(UserDict, Field):
    def add_record(self, record):
        self.data[record.name] = record.phone
    
class Record(Field):
    def __init__(self, user_name):
        self.name = Name(user_name)
        
    phone = Phone()
    
    def add_phone(self, number):
        self.phone.append(number)
        
    def delete_phone(self):
        self.phone.clear()
        
    def change_phone(self, number):
        user_input = input(f'Please choose the number of phone to change "1", "2", "3"... or "all"')
        if user_input.isnumeric() and len(self.phone) >= int(user_input) and int(user_input) > 0:
            self.phone[int(user_input)-1] = number
        elif user_input == 'all':
            self.phone.clear()
            self.phone.append(number)
        else:
            print('Wrong command')
