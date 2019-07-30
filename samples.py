def miles_to_feet(miles):
    print (5280*miles)

miles_to_feet(13)


def total_seconds(hours,minutes,seconds):

    print (hours *3600 + minutes *60 +seconds)

total_seconds(7, 21, 37)


def is_even(number):
    if number % 2 == 0:
        print("True")
    else:
        print("False")

is_even(5)


def name_and_age(name,age):
    if age <= 0 :
        print("invalid age")
    else:
        print(name + " is " + str(age) + " years old")

name_and_age("Eoin", 20)
