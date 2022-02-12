
# Question One
def timeConvert():

    minutes = int(input('Enter the number of minutes:'))
    if minutes <= 60:
        sec = minutes * 60
        print('The number of seconds is {0:.2f}'.format(sec))
    return sec

timeConvert()


#Question Two


number = 0

def questionTwo():
    global number
    number += 1
    return number

print(questionTwo())

# Question Three

def questionThree():
    num1 = int(input("Enter a number: "))
    if num1 % 2 == 0:
        print("It's Even number!")

    else:
        print("It's odd number")

questionThree()



# Question Four

userName = str(input("Enter your username: "))

print(userName.split("@")[0])


# Question Five

subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]
for a in range(len(subjects)):
    for b in range(len(verbs)):
        for c in range(len(objects)):
            result = "%s %s %s" % (subjects[a], verbs[b], objects[c])
            print(result)















