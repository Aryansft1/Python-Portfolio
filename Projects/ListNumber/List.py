numbers = []
normal_count = 0

while True:
    n = int(input("Enter number: "))

    
    if n < 0:
        Manfi = [x for x in numbers if x > 0]
        if Manfi:
            avg = sum(Manfi) / len(Manfi)
            print("Average:", avg)
        else:
            print("Mosbat Nadarim")
        break

    
    elif n == 1:
        Yekta = list(set(numbers))
        print("Adad haye Yekta:", Yekta)
        normal_count = 0

    
    elif n == 0:
        numbers.clear()
        print("Adad ha Reset Shod")
        normal_count = 0

    
    else:
        numbers.append(n)
        normal_count += 1

        if normal_count == 10:
            print("Tedad Vorodi Ha Ziad Ast")
            normal_count = 0
