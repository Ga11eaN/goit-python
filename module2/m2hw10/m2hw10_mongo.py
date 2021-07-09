import contacts_list
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://Byuko:35715946@cluster0.wo3h0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)

db = client.Contacts

def save_contact_list(contact_list):
    for key, value in contact_list.data.items():
        db[contact_list.name].insert_one({'name' : key,
                                     'phone' : value['phone'],
                                     'address' : value['address'],
                                     'mail' : value['mail'],
                                     'birthday' : value['birthday'].data})

def load_contact_list(contact_list):
    user_input = input('Enter the name of your Contact List: ')
    contact_list.name = user_input
    
    load_from_mongo = db[user_input].find({})
    for record in load_from_mongo:
        loaded_record = contacts_list.Record(
            name = record['name'], 
            phone = record['phone'],
            address = record['address'],
            mail = record['mail'],
            birthday = contacts_list.Birthday(record['birthday'])
            )
        contact_list.data[record['name']] = loaded_record
        

test_cl = contacts_list.ContactList('new_cl')



for i in range(3):
    test_record = contacts_list.Record(name = 'Ivan'+str(i),
                                       phone = ['+3809367441'+str(i)],
                                       address = ['Kyiv, Mazepy 2'+str(i)],
                                       mail = ['IvanCelofan' + str(i) + '@gmail.com'],
                                       birthday = contacts_list.Birthday('1' + str(i) + '.01.2000'))
    test_cl.add_contact(test_record)

test_cl.print_contact_list()
save_contact_list(test_cl)

test_load_cl = contacts_list.ContactList()
load_contact_list(test_load_cl)
test_load_cl.print_contact_list()
