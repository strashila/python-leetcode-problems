### Fibanacci recurs

def fibba_recurs(limit, a=0, b=1):
    if (a >= limit):
        return
    else:
        print(a)
        c = a + b
        a = b
        b = c
        fibba_recurs(limit, a, b)

#fibba_recurs(100)

# find out if fibbanacci

def is_in_fibba(num, a=0, b=1):
    num_in_fibba = False
    while a <= num:
        if a == num:
            num_in_fibba = True
            return num_in_fibba
        else:
            c = a + b
            a = b
            b = c
    return num_in_fibba

print(is_in_fibba(13))


    