
import datetime
any_more_ps_guests = "yes"
total_ps_rental_fee = 0


while any_more_ps_guests == "yes":

    ps_guest_name = input('Pacific Shores Guest Name:  ')

    ps_arrival_date_input = input("Arrival Date (xx/xx/xxxx):  ")
    ps_arrival_date_month = int(ps_arrival_date_input[:2])
    ps_arrival_date_day = int(ps_arrival_date_input[3:5])
    ps_arrival_date_year = int(ps_arrival_date_input[6:])
    ps_arrival_date = ps_arrival_date_month, ps_arrival_date_day, ps_arrival_date_year

    ps_departure_date_input = input("Departure Date (xx/xx/xxxx):  ")
    ps_departure_date_month = int(ps_departure_date_input[:2])
    ps_departure_date_day = int(ps_departure_date_input[3:5])
    ps_departure_date_year = int(ps_departure_date_input[6:])
    ps_departure_date = ps_departure_date_year, ps_departure_date_month, ps_departure_date_day

    def number_of_nights():
        date_one = datetime.date(ps_arrival_date_year, ps_arrival_date_month, ps_arrival_date_day)
        date_two = datetime.date(ps_departure_date_year, ps_departure_date_month, ps_departure_date_day)
        return (date_two - date_one).days


    def ps_nightly_rate():
        rate = input('Rate:  ')
        return rate


    ps_total_nights = number_of_nights()
    ps_rate = ps_nightly_rate()
    ps_total_rental_fee = int(ps_total_nights) * int(ps_rate)

    print([ps_guest_name, ps_total_nights, ps_rate, ps_total_rental_fee])

    total_ps_rental_fee += ps_total_rental_fee

    anyone_else = input('Are there anymore guests?  ')
    if anyone_else == 'no':
        break


print('Pacific Shores Total Rental Fee:  ', total_ps_rental_fee)

any_more_kkn_guests = 'yes'
total_kkn_rental_fee = 0

while any_more_kkn_guests == "yes":

    kkn_guest_name = input('Kihei Kai Nani Guest Name:  ')

    kkn_arrival_date_input = input("Arrival Date (xx/xx/xxxx):  ")
    kkn_arrival_date_month = int(ps_arrival_date_input[:2])
    kkn_arrival_date_day = int(ps_arrival_date_input[3:5])
    kkn_arrival_date_year = int(ps_arrival_date_input[6:])
    kkn_arrival_date = kkn_arrival_date_month, kkn_arrival_date_day, kkn_arrival_date_year

    kkn_departure_date_input = input("Departure Date (xx/xx/xxxx):  ")
    kkn_departure_date_month = int(ps_departure_date_input[:2])
    kkn_departure_date_day = int(ps_departure_date_input[3:5])
    kkn_departure_date_year = int(ps_departure_date_input[6:])
    kkn_departure_date = kkn_departure_date_year, kkn_departure_date_month, kkn_departure_date_day


    def number_of_nights():
        date_one = datetime.date(kkn_arrival_date_year, kkn_arrival_date_month, kkn_arrival_date_day)
        date_two = datetime.date(kkn_departure_date_year, kkn_departure_date_month, kkn_departure_date_day)
        return (date_two - date_one).days

    def kkn_nightly_rate():
        rate = input('Rate:  ')
        return rate

    kkn_total_nights = number_of_nights()
    kkn_rate = kkn_nightly_rate()
    kkn_total_rental_fee = int(kkn_total_nights) * int(kkn_rate)

    print([kkn_guest_name, kkn_total_nights, kkn_rate, kkn_total_rental_fee])

    total_kkn_rental_fee += kkn_total_rental_fee

    anyone_else = input('Are there anymore guests?  ')
    if anyone_else == 'no':
        break

print('Kihei Kai Nani Total Rental Fee:  ', total_kkn_rental_fee)
print('Total Rental Fee Amount: ', total_ps_rental_fee + total_kkn_rental_fee)

total_management_fee = (total_ps_rental_fee + total_kkn_rental_fee) * 0.10
print('Total Management Fee:  ', '{0:.2f}'.format(total_management_fee))