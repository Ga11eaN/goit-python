def input_error(actions):
    def inner(command):
        try:
            result = actions(command)
        except ValueError:
            result ="Wrong q-ty of arguments"
        except KeyError:
            result = 'Wrong command'
        except IndexError:
            result = 'Wrong command'
        return result
    return inner

def hello():
    return 'How can I help you?'

def closed():
    return 'Good bye!'

def add_name(name, phone):
    if phone.isnumeric():
        phone_dict[name] = phone
        output = f'{name} added to your phone book'
    else:
        output = 'Input for add is not correct, should be: "add [name] [phone number]"'
    return output

def change_phone(name, phone):
    if phone.isnumeric():
        phone_dict[name] = phone
        output = f'{name} number has been changed'
    else:
        output = 'Input for change is not correct, should be: "change [name] [phone number]"'
    return output

def get_phone(name):
    return f'Phone number for {name}: {phone_dict[name]}'

def show_book():  
    return phone_dict

def get_handler(operation):
    COMMANDS = {
        'hello': hello,
        'close': closed,
        'exit': closed,
        'good bye': closed,
        'add': add_name,
        'change': change_phone,
        'phone': get_phone,
        'show': show_book
    }

    return COMMANDS[operation]

@input_error
def actions(command):
    command_lower = command.lower().split()[0]
    handler = get_handler(command_lower)
        
    if command_lower in ('hello', 'good bye', 'close', 'exit'):
        output = handler()
    elif command_lower.startswith('add'):
        com,name,phone = command.split()
        output = handler(name, phone)
    elif command_lower.startswith('change'):
        com, name, phone = command.split()
        output = handler(name, phone)
    elif command_lower.startswith('phone'):
        com, name = command.split()
        output = handler(name)
    elif command.lower() == 'show all':
        output = handler()
    else:
        output = 'Wrong command'
        
    return output

def main():
    phone_dict = {'Lisa': '0936665554'}
    while True:
        message = input('Enter command please: ')
        result = actions(message)
        print(result)
        if result == 'Good bye!':
            break
            
if __name__ == '__main__':
    main()