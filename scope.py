x = 50

def my_func():
    # global x can redefine x globally, but using return is better..
    # because it keeps things clean and compartmentalized. (L E G B)
    x = 'kilop'
    return x

print x
x = my_func()
print type (x)
print x
