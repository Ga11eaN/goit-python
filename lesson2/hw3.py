counter = 0
insertion = ''
operators = ('+' , '-' , '*' , '/')
result = 0
operator = '+'

while insertion != '=':
    if counter % 2 == 0:
        try:
            insertion = input('Enter the number: ')
            number = float(insertion)
            counter += 1
            
            if operator == '+':
                result = result + number
            elif operator == '-':
                result = result - number
            elif operator == '*':
                result = result * number
            else:
                result = result / number
                
        except ValueError:
            if insertion != '=':
                print(f'{insertion} is not a number. Please try again')
    else:
        insertion = input('Enter the operator: ')
        if insertion in operators:
            operator = insertion
            counter += 1
        elif insertion != '=':
            print(f'{insertion} is not an operator. Please try again')

if not result % 1:
    print(int(result))
else:
    print(result)