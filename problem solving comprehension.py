
# find largest and second largest from given list of numbers.
ip = [2,15,8,11,25,16]

if ip[0] > ip[1]:
    largest, sec_largest = ip[0], ip[1]
else:
    largest, sec_largest = ip[1], ip[0]

for x in ip[2:]:
    if x > largest:
        sec_largest = largest
        largest = x
    elif sec_largest < x < largest:
        sec_largest = x

print("Largest: ",largest)
print("Second largest: ",sec_largest if largest != sec_largest else "No second largest")


print()
# ip=['sravani','sravan','kumar','kumari','lalitha','lalith','arjun','lakshmi','nandini']
# op=[(('sravani','female'),('sravan','male'),('kumar','male'))

ip = ['Sravani','Sravan','kumar','kumari','lalitha','lalith','arjun','lakshmi','nandini']
op = tuple((name.lower(), "Female" if name.lower().endswith(("i","a")) else "Male")for name in ip)
print(op)