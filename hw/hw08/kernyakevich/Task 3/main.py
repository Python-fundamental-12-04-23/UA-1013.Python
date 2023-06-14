from helpers1 import rect_area, triangle_area, circle_area

def main():
    print("Площу якої фігури ви хочете обчислити?")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")

    choice = input("Введіть свій вибір (1-3): ")

    if choice == "1":
        length = float(input("Введіть довжину прямокутника, l: "))
        width = float(input("Введіть ширину прямокутника, b: "))
        area = rect_area(length, width)
        print("Площа прямокутника дорівнює:", area)
    elif choice == "2":
        base = float(input("Введіть основу трикутника, b: "))
        height = float(input("Введіть висоту трикутника, h: "))
        area = triangle_area(base, height)
        print("Площа трикутника дорівнює:", area)
    elif choice == "3":
        radius = float(input("Введіть радіус кола, r: "))
        area = circle_area(radius)
        print("Площа кола дорівнює:", area)
    else:
        print("Неправильний вибір. Будь ласка, введіть правильний варіант (1-3).")

if __name__ == "__main__":
    main()
