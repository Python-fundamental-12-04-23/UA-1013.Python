from counter_module import count

answer = str(input("Hi there. Which shape area do you want to calculate ?\nAnswer here: "))

if answer == "rectangle":
        a = int(input("Enter side a: "))
        b = int(input("Enter side b: "))
        print(count.rectangle_area(a, b))

elif answer == "triangle":
    h = int(input("Enter height: "))
    a = int(input("Enter side a: "))
    print((count.triangle_are(h, a)))

elif answer == "circle":
    r = int(input("Enter r of the circle: "))
    print(count.circle_are(r))
else:
    print("Wrong shape. Try again.")
