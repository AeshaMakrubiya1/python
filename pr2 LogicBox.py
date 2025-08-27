print("Pattern & Numbers")

while True:
    print("\nOptions: 1.Pattern 2.NumberCheck 3.End")
    sel = input("Enter option: ")

    if sel == "1":
        cnt = int(input("Rows? "))
        if cnt <= 0:
            print("break on wrong input")
            break
        for r in range(1, cnt+1):
            print("*"*r)
    elif sel == "2":
        stt = int(input("Start range: "))
        enn = int(input("End range: "))
        if stt >= enn:
            print("Invalid input -> continue")
            continue
        add = 0
        for no in range(stt, enn+1):
            if no % 2 == 0:
                print(no, "even")
            else:
                print(no, "odd")
            add += no
        print("Sum =", add)
    elif sel == "3":
        print("End program.")
        break
    else:
        print("Try again")
