temp=int(input("введите температуру воздуха"))
if temp>20:
    rainy=input("есть осадки?(да/нет):")

    if rainy.lower() == "да":
            print("наденьте футболку, шорты и дождевик")
    else:
            print("наденьте футболку и шорты")
else:
        if temp < 0:
            print("наденьте пуховик")
        else:
            rainy1 = input("есть осадки? (да/нет): ")
            if rainy1.lower() == "да":
                raining_heavily = input("осадки сильные? (да/нет): ")
                if raining_heavily.lower() == "да":
                    print("наденьте пальто, резиновые сапоги и зонт")
                else:
                    print("наденьте пальто и дождевик")
            else:
                print("наденьте пальто")