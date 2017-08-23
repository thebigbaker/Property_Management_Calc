any_more_ps_guests = "yes"
total_ps_rental_fee = 0

while any_more_ps_guests == "yes":


    def ps_guest_name():
        guest = input('Pacific Shores Guest Name:  ')
        return guest

    def ps_stay_length():
        total_nights = input('Number of Nights:  ')
        return total_nights

    def ps_nightly_rate():
        rate = input('Rate:  ')
        return rate


    ps_guest = ps_guest_name()
    ps_total_nights = ps_stay_length()
    ps_rate = ps_nightly_rate()
    ps_total_rental_fee = int(ps_total_nights) * int(ps_rate)

    print([ps_guest, ps_total_nights, ps_rate, ps_total_rental_fee])

    total_ps_rental_fee += ps_total_rental_fee

    anyone_else = input('Are there anymore guests?  ')
    if anyone_else == 'no':
        break


print('Pacific Shores Total Rental Fee:  ', total_ps_rental_fee)





any_more_kkn_guests = 'yes'
total_kkn_rental_fee = 0

while any_more_kkn_guests == "yes":


    def kkn_guest_name():
        guest = input('Kihei Kai Nani Guest Name:  ')
        return guest

    def kkn_stay_length():
        total_nights = input('Number of Nights:  ')
        return total_nights

    def kkn_nightly_rate():
        rate = input('Rate:  ')
        return rate


    kkn_guest = kkn_guest_name()
    kkn_total_nights = kkn_stay_length()
    kkn_rate = kkn_nightly_rate()
    kkn_total_rental_fee = int(kkn_total_nights) * int(kkn_rate)

    print([kkn_guest, kkn_total_nights, kkn_rate, kkn_total_rental_fee])

    total_kkn_rental_fee += kkn_total_rental_fee

    anyone_else = input('Are there anymore guests?  ')
    if anyone_else == 'no':
        break


print('Kihei Kai Nani Total Rental Fee:  ', total_kkn_rental_fee)

print('Total Rental Fee Amount: ', total_ps_rental_fee + total_kkn_rental_fee)

total_management_fee = (total_ps_rental_fee + total_kkn_rental_fee) * 0.10

print('Total Management Fee:  ', '{0:.2f}'.format(total_management_fee))











