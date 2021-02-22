from datetime import datetime, timedelta
from random import choice, randint


#Check if date is in range fron saturday this week and saturday next week
def check_date(date):
    date_now = datetime.now()
    weekday_int = date_now.weekday()
    date = date.replace(year = date_now.year)

    delta_to_start = timedelta(days = 5 - weekday_int)
    start_date = date_now + delta_to_start
    start_date = start_date.replace(hour = 0, minute =0, second = 0, microsecond = 0)
    end_date = start_date + timedelta(days = 7)

    if date >= start_date and date < end_date:
        return True
    else:
        return False

#counting celebrating days
def congratulate(users):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    result_dict = {day : [] for day in days}
    
    for items in users:
        weekday = datetime.strftime(items["birthday"], "%A")
        if check_date(items['birthday']):
            result_dict[weekday].append(items['name'])
        
    result_dict['Monday'] = result_dict.pop('Saturday') + result_dict.pop('Sunday') + result_dict['Monday']
    
    for day in days[:5]:
        if result_dict[day]:
            print(f'{day}: {", ".join(result_dict[day])}')

#Check with some random values
def main():
    users = []
    names = ['Bill', 'Stan', 'Kenny', 'Kyle', 'Eric', 'Wendy']
    
    for i in range(20):
        d = datetime(year = randint(1950, 2000), month = 2, day = randint(18, 28))
        users.append({'name': choice(names)+str(i),'birthday' : d})
        
    congratulate(users)

if __name__ == '__main__':
    main()