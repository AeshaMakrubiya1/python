
locker = []

while True:
    print("\n[Menu] 1.Add 2.Show 3.Update 4.Delete 5.Subjects 6.Exit")
    m = input("-> ")

    if m == "1":
        rid = int(input("ID: "))
        nm = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("DOB (YYYY-MM-DD): ")
        subj = input("Subjects: ")
        key = (rid, dob)
        subs = list(set([x.strip() for x in subj.split(",") if x.strip()]))
        locker.append({"key": key, "name": nm, "age": age, "grade": grade, "subjects": subs})
        print("Saved!")
    elif m == "2":
        print("\n-- Records --")
        if not locker:
            print("Empty.")
        else:
            for r in locker:
                rid, dob = r["key"]
                print(f"ID {rid} | {r['name']} | Age {r['age']} | Grade {r['grade']} | DOB {dob} | Subjects {', '.join(r['subjects'])}")
    elif m == "3":
        target = int(input("ID: "))
        ok = False
        for r in locker:
            if r["key"][0] == target:
                ok = True
                print("1 Age  2 Subjects")
                k = input("Field: ")
                if k == "1":
                    r["age"] = int(input("Enter age: "))
                elif k == "2":
                    r["subjects"] = list(set([y.strip() for y in input("Enter subjects: ").split(",") if y.strip()]))
                print("Done.")
                break
        if not ok:
            print("Not found.")
    elif m == "4":
        target = int(input("ID to delete: "))
        pos = -1
        for i in range(len(locker)):
            if locker[i]["key"][0] == target:
                pos = i
                break
        if pos >= 0:
            del locker[pos]
            print("Removed.")
        else:
            print("Missing.")
    elif m == "5":
        uni = set()
        for r in locker:
            uni |= set(r["subjects"])
        print("All unique subjects:", ", ".join(sorted(uni)) if uni else "None")
    elif m == "6":
        print("Exit now.")
        break
    else:
        print("Invalid input.")
