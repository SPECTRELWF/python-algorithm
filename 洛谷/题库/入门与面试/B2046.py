n = int(input())

walk = n / 1.2

bike = 27 + 23 + n / 3.0

if walk > bike:
    print("Bike")
elif walk == bike:
    print("All") 
else:
    print("Walk")