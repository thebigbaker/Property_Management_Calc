import datetime

any_more_guests = "yes"
total_rental_fee = 0


def guest():
    return input('Guest Name:  ')


def arrival_date():
    return input('Arrival Date (xx/xx/xxxx):  ')


def departure_date():
    return input('Departure Date (xx/xx/xxxx):  ')


def number_of_nights():
    date_format = '%m/%d/%Y'
    arrival_day = input('Arrival Date (xx/xx/xxxx):  ')
    departure_day = input('Departure Date (xx/xx/xxxx):  ')

    return (datetime.datetime.strptime(departure_day, date_format) -
            datetime.datetime.strptime(arrival_day, date_format)).days


def nightly_rate():
    return input('Rate:  ')


def rental_fee_calc(property_name):
    while any_more_guests:
        guest_name = guest()
        total_nights = number_of_nights()
        rate = int(nightly_rate())
        rental_fee = total_nights * rate
        global total_rental_fee
        total_rental_fee += rental_fee
        print(property_name + ' Guest Name: ' + guest_name,
              'Number of Nights: ' + str(total_nights),
              'Nightly Rate: ' + str(rate),
              'Rental Fee: ' + str(rental_fee))

        anyone_else = input('Are there anymore guests?  ')
        if anyone_else == 'no':
            break


rental_fee_calc('Pacific Shores')
ps_total_rental_fee = total_rental_fee
print('Total Pacific Shores Rental Fee = ', ps_total_rental_fee)

total_rental_fee = 0

rental_fee_calc('Kihei Kai Nani')
kkn_total_rental_fee = total_rental_fee
print('Total Kihei Kai Nani Rental Fee = ', kkn_total_rental_fee)

combined_rental_fee = ps_total_rental_fee + kkn_total_rental_fee
print(combined_rental_fee)

management_fee = combined_rental_fee * 0.10
print('Total Management Fee:  ', '{0:.2f}'.format(management_fee))
