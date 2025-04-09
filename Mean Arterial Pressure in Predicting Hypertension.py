age = int(input("Enter age: "))

sbp = float(input(" Enter sbp: "))
dbp = float(input(" Enter dbp: "))

pulse_pressure = sbp - dbp
mean_arterial_pressure = dbp + 1/3 * pulse_pressure

print("age:", age)
if age >= 35:
    print("moderate risk associated with age")
else:
    print("minimal risk associated with age")
    


print("sbp:", sbp)
print("dbp:", dbp)

if sbp >= 130:
    print("systolic hypertension")
else:
    print("normal systolic blood pressure")
    
    
if dbp >= 90:
        print("diastolic hypertension")
else:
    print("normal diastolic blood pressure")

print("pulse_pressure:", pulse_pressure)
print("mean_arterial_pressure: ", mean_arterial_pressure)

if mean_arterial_pressure >= 89:
    print("exposed")
else:
    print("unexposed")


def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is even! ⚖️")
    else:
        print(number, "is odd! 🎯")

check_even_odd(pulse_pressure)