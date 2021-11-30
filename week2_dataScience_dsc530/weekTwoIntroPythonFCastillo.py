#Felipe Castillo
#Date: 09/06/2021
#DSC: 530


def main():
    fName = "felipe"
    lName = "Castillo "
    print("Hello world, I wonder why that is always the default coding text to start with")


    print("Add: "+ str(6 + 5))
    print("Subtract: "+ str(5 - 3))
    print("Mulitply: " + str(6* 4))
    print("Divide: "+ str(6/2))

    fullName =  fName+ " "+ lName
    print("Concact: " + fullName)

    #list of values

    zipCode = ["75602", "789603", "90210","589000"]

    zipCode.append("73086")

    for i in zipCode:
        print(i)

    animalInZoo = ("bear", "lion","zebra", "monkey")

    print(animalInZoo)





if __name__ == '__main__':
    main()