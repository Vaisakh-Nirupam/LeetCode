# Advanced Room Booking 

# Mine
def hotel_manager(arrive,depart,k):
    if k == 0:
        return 0
    book = [(i,'Red') for i in arrive] + [(i,'Green') for i in depart]
    book.sort()    
    guest = 0
    for _,i in book:
        if i == 'Red':
            guest += 1
        else:
            guest -= 1
        if guest > k:
            return 0
    return 1
a = [1,3,5]
d = [2,6,8]
k = 1
print(hotel_manager(a,d,k))


# GPT
def hotel_manager(arrive,depart,k):
    bookings = [(i,1) for i in arrive] + [(i,-1) for i in depart]
    bookings.sort()
    guests = 0
    for _,i in bookings:
        guests+=i
        if guests > k:
            return 0
    return 1
a = [1,3,5]
d = [2,6,8]
k = 0
print(hotel_manager(a,d,k))