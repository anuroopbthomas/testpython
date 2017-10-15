import sys

version = "1.0"
i = "0"
fileintial = open("gallons/gallonsleft" + i + ".txt","r")
intial = int(fileintial.read())
if intial < 30:
    file = open("gallons/gallonsleft" + i + ".txt","w")
    file.write("20")
    file.close()

gallonsBLeft = int(20)


while gallonsBLeft > 0:

    car = input("What car do you drive?: ")

    if car == "BMW":
        miles = float(input("How many miles will you travel:? "))
        gallons = miles / 29
    elif car == "Porsche":
        miles = float(input("How many miles will you travel:? "))
        gallons = miles / 24.5
    else:
        print("Invalid Car Model")
        sys.exit()
    print("Your car will use...")
    print(round(gallons, 2), "gallons")


    file2 = open("gallons/gallonsleft" + str(i) + ".txt", "r")
    gallonsBLeft = float(file2.read())
    print("This is how many gallons you had", round(gallonsBLeft,2))
    gallonsBLeft = gallonsBLeft - gallons
    print("This is how many gallons you have now", round(gallonsBLeft,2))
    file2.close()

    i = int(i) + 1
    file3 = open("gallons/gallonsleft" + str(i) + ".txt", "w")
    file3.write(str(gallonsBLeft))
    file3.close()



gallonsBLeft = int(11)
print("YOU ARE OUT OF FUEL")
print("Version: " + version)
