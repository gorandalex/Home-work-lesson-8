from datetime import datetime, timedelta

def get_birthdays_per_week(list_birthdays : list):
    #Визначаємо поточну дату та період привітання
    current_date = datetime.now().date()
    start_congrat = current_date + timedelta(days = (5 - current_date.weekday()))
    end_congrat = start_congrat + timedelta(days= 6)
    dayofweek_birthdays = {}
    list_birthdays = {}
    #Формуємо один словник з днем тижня для кожної дати, 
    #другий для кожного дня тижня, щоб додавати співробітників
    for add_years in range(7):
        day_congrat = start_congrat + timedelta(days = add_years)
        if day_congrat.weekday() in (5, 6):
            dayofweek_birthdays[day_congrat] = datetime.strftime(day_congrat + timedelta(days = (7 - day_congrat.weekday())), '%A')
        else:
            dayofweek_birthdays[day_congrat] = datetime.strftime(day_congrat, '%A')
        if not dayofweek_birthdays[day_congrat] in list_birthdays:
            list_birthdays[dayofweek_birthdays[day_congrat]] = []
    
    for employer in list_birthdays:
        #Визначаємо дату дня народження, як що вона припадає на 29 число лютого, 
        #а в поточному році такої дати немає, то будемо поздоровляти 28 лютого
        try:
            date_birthday = employer['birthday'].replace(year= current_date.year).date()
        except ValueError:
            date_birthday = employer['birthday'].replace(year= current_date.year, day= 28).date()
        #Як що дата попадає до періоду привітання, то додаємо співробітника до списку потрібного дня тижня
        if start_congrat <= date_birthday <= end_congrat:
            list_birthdays[dayofweek_birthdays[date_birthday]].append(employer['name'])

    #Як що для якогось дня тижня список не порожній, виводимо його користувачу    
    for day_of_week, employer in list_birthdays.items():
        if employer:
            print('{}: {}'.format(day_of_week, ', '.join(employer))) 

