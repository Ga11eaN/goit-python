from collections import UserDict, UserList, UserString
from datetime import datetime

class Field():
    __value = ''
    
    @property
    def value(self):
        return self.__value
        
    @value.setter
    def value(self, new_value):
        self.__value = new_value
    
  
class Name(UserString, Field):
    pass
    
class Phone(UserList, Field):

    @property
    def value(self):
        return self
        
    @value.setter
    def value(self, new_value):
        if new_value[0] == '0' and len(new_value) == 10:
            self.data.append(new_value)
        else:
            print('Phone value is not correct. Should start from 0 and have 10 digits')

class AddressBook(UserDict, Field):

    n = 2
    offset = 0
    birthday = {}
    
    def add_record(self, record):
        self.data[record.name] = record.phone
        self.birthday[record.name] = record.birthday
        
    def __next__(self):
        key_list = list(self.data)
        end_value = self.offset + self.n
        
        if self.offset >= len(key_list):
            raise StopIteration
            
        page = ''
        for i in key_list[self.offset:end_value]:
            page += f'{i} ({self.birthday[i]}) : {self.data[i]}\n'

        self.offset = end_value
        return page
        
    def __iter__(self):
        return self    
        
        
class Birthday(UserString):
    
    def __init__(self, birthday):
        self.data = birthday
        self.value = birthday
    
    @property
    def value(self):
        return self.data
        
    @value.setter
    def value(self, new_value):

        try:
            self.year = int(new_value[6:])
            self.month = int(new_value[3:5])
            self.day = int(new_value[:2])
            self.date = datetime(self.year, self.month, self.day)
            self.data = new_value
        except ValueError:
            self.data = ''
            print('Birthday input is not correct. Should be in format: DD/MM/YYYY')
    
class Record(Field):
    def __init__(self, user_name, birthday = 0):
        self.name = Name(user_name)
        self.birthday = Birthday(birthday)
        self.phone = Phone()

    def add_phone(self, number):
        self.phone.value = number
        
    def delete_phone(self):
        self.phone.clear()
        
    def change_phone(self, number):
        user_input = input(f'Please choose the number of phone to change "1", "2", "3"... or "all"')
        if user_input.isnumeric() and len(self.phone) >= int(user_input) and int(user_input) > 0:
            self.phone.pop(int(user_input)-1)
            self.add_phone(number)
        elif user_input == 'all':
            self.phone.clear()
            self.add_phone(number)
        else:
            print('Wrong command')

    def days_to_birthday(self):
        if not self.birthday:
            return 'Birthday is not defined' 
        else:
            now = datetime.now()
            delta1 = datetime(now.year, self.birthday.month, self.birthday.day)
            delta2 = datetime(now.year + 1, self.birthday.month, self.birthday.day)
            
            delta = ((delta1 if delta1 > now else delta2) - now).days
            
            return delta
            

a = Record('Ivan', birthday = '25/03/1993')
a.add_phone('0936792731')
a.add_phone('0674718277')

b = Record('Hui', birthday = 'asdasd')
b.add_phone('0936792731')
b.add_phone('0674718277')

c = Record('Senya', birthday ='23/4234/4234')
c.add_phone('0674718277')

add_book = AddressBook()
add_book.add_record(a)
add_book.add_record(b)
add_book.add_record(c)

print(a.days_to_birthday())
for i in add_book:
    print(i)