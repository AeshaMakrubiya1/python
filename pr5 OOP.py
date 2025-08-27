
class Subject:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        cls = "Subject"
        return cls + "(" + "name=" + str(self.name) + ", age=" + str(self.age) + ")"

class EmployeeY(Subject):
    def __init__(self, name, age, code="", pay=0.0):
        super().__init__(name, age)
        self.__code = str(code)
        self.__pay = float(pay)

    # encapsulation
    def fetch_code(self): return self.__code
    def assign_code(self, new_code): self.__code = str(new_code)
    def read_salary(self): return self.__pay
    def update_salary(self, value):
        value = float(value)
        if value < 0: print("Invalid pay")
        else: self.__pay = value

    # 'overloading' via alternative constructors
    @classmethod
    def basic(cls, name, age, code):
        return cls(name, age, code, 0.0)
    @classmethod
    def from_map(cls, d):
        return cls(d.get("name",""), d.get("age",0), d.get("employee_id",""), d.get("salary",0))

    def __str__(self):
        return "EmployeeY(name=" + str(self.name) + ", age=" + str(self.age) + ", code=" + str(self.__code) + ", pay=$" + str(self.__pay) + ")"
    # comparison operators -> pay based
    def __eq__(self, other): return isinstance(other, EmployeeY) and self.read_salary() == other.read_salary()
    def __lt__(self, other): return isinstance(other, EmployeeY) and self.read_salary() < other.read_salary()
    def __gt__(self, other): return isinstance(other, EmployeeY) and self.read_salary() > other.read_salary()

    def exhibit(self): print(self)

class LeadY(EmployeeY):
    def __init__(self, name, age, code, pay, dept):
        super().__init__(name, age, code, pay)
        self.dept = dept
    def exhibit(self):
        print(super().__str__() + " | dept: " + str(self.dept))

class EngineerY(EmployeeY):
    def __init__(self, name, age, code, pay, lang):
        super().__init__(name, age, code, pay)
        self.lang = lang
    def exhibit(self):
        print(super().__str__() + " | language: " + str(self.lang))

print("check:", issubclass(LeadY, EmployeeY), issubclass(EngineerY, EmployeeY))

rollcall = []
ledger = {}

def banner():
    print("\n--- Staff Console ---")
    print("1) New Subject")
    print("2) New EmployeeY")
    print("3) New LeadY")
    print("4) New EngineerY")
    print("5) Show")
    print("6) Compare Pay")
    print("7) Exit")

while True:
    banner()
    pick = input("Choose: ").strip()
    if pick == "1":
        nm = input("Name: "); ag = int(input("Age: "))
        rollcall.append(Subject(nm, ag))
        print("saved")
    elif pick == "2":
        nm = input("Name: "); ag = int(input("Age: "))
        cd = input("EmpCode: "); py = float(input("Pay: "))
        e = EmployeeY(nm, ag, cd, py); ledger[e.fetch_code()] = e; print("ok")
    elif pick == "3":
        nm = input("Name: "); ag = int(input("Age: "))
        cd = input("EmpCode: "); py = float(input("Pay: ")); dp = input("Dept: ")
        m = LeadY(nm, ag, cd, py, dp); ledger[m.fetch_code()] = m; print("ok")
    elif pick == "4":
        nm = input("Name: "); ag = int(input("Age: "))
        cd = input("EmpCode: "); py = float(input("Pay: ")); lg = input("Language: ")
        d = EngineerY(nm, ag, cd, py, lg); ledger[d.fetch_code()] = d; print("ok")
    elif pick == "5":
        print("a) Subjects  b) EmployeeY by id  c) all EmployeeY")
        sub = input("-> ").strip().lower()
        if sub == "a":
            if not rollcall: print("none")
            for i, p in enumerate(rollcall, 1): print(i, p)
        elif sub == "b":
            key = input("id: "); obj = ledger.get(key)
            if obj: obj.exhibit()
            else: print("not found")
        else:
            if not ledger: print("empty")
            for v in ledger.values(): v.exhibit()
    elif pick == "6":
        a = input("id1: "); b = input("id2: ")
        x = ledger.get(a); y = ledger.get(b)
        if not x or not y: print("missing")
        else:
            if x == y: print("same pay")
            elif x > y: print(a, "earns more than", b)
            else: print(a, "earns less than", b)
    elif pick == "7":
        print("bye"); break
    else:
        print("wrong")
