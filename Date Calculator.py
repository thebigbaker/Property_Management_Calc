import datetime

arrival_date_input = input("Arrival Date (xx/xx/xxxx):  ")

arrival_date_month = int(arrival_date_input[:2])
arrival_date_day = int(arrival_date_input[3:5])
arrival_date_year = int(arrival_date_input[6:])

arrival_date = arrival_date_month, arrival_date_day, arrival_date_year


print(arrival_date)


departure_date_input = input("Departure Date (xx/xx/xxxx):  ")

departure_date_month = int(departure_date_input[:2])
departure_date_day = int(departure_date_input[3:5])
departure_date_year = int(departure_date_input[6:])


departure_date = departure_date_year, departure_date_month, departure_date_day

print(departure_date)

def number_of_nights():
    date_one = datetime.date(arrival_date_year, arrival_date_month, arrival_date_day)
    date_two = datetime.date(departure_date_year, departure_date_month, departure_date_day)
    return (date_two - date_one).days

print('Number of Nights:  ', number_of_nights())