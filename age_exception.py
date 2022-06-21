try:
    age = int(input("age: "))   # input data should be numbers
    print(age)
except ValueError:      # inbuilt Exception
    print("\'invalid value' please make sure age should be a positive number ")

