from func.calculate_area import calculate_rectangle, calculate_triangle, calculate_circle


while True:
    print("Which area you would like to calculate ? Type: rectangle / triangle / circle. If you want stop a program input 'q'")
    user_input = input()
    if user_input == "rectangle":
        print("Please input 'a' and 'b' for rectangle: ")
        a, b = int(input()), int(input())
        print(calculate_rectangle(a, b))

    if user_input == "triangle":
        print("Please input 'a' and 'h' for triangle: ")
        a, h = int(input()), int(input())
        print(calculate_triangle(a, h))

    if user_input == "circle":
        print("Please input 'r' for circle: ")
        r = int(input())
        print(calculate_circle(r))
    if user_input == 'q':
        break
