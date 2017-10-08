version = "1"
i = "0"
file = open("gallonsleft" + i + ".txt","w")
file.write("11")
file.close()
gallonsBLeft = int(11)


while gallonsBLeft > 0:

    car = input("What car do you drive?: ")
    miles = int(input("How many miles will you travel:? "))
    if car == "BMW":
        gallons = miles / 29
    elif car == "Porsche":
        gallons = miles / 24.5
    else:
        print("Invalid Car Model")
    print("Your car will use...")
    print(gallons, "gallons")


    file2 = open("gallonsleft" + str(i) + ".txt", "r")
    gallonsBLeft = float(file2.read())
    print("This is how many gallons you had", gallonsBLeft)
    gallonsBLeft = gallonsBLeft - gallons
    print("This is how many gallons you have now", gallonsBLeft)
    file2.close()

    i = int(i) + 1
    file3 = open("gallonsleft" + str(i) + ".txt", "w")
    file3.write(str(gallonsBLeft))
    file3.close()



gallonsBLeft = int(11)
print("YOU ARE OUT OF FUEL")
print("hello world version: " + version)
