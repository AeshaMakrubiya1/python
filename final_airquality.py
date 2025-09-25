
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ITEMS = ['Fetch data', 'Show head/tail', 'Wash data', 'Lite metrics', 'Paint graphs', 'Bye']

class AirqualityTool:
    def __init__(self):
        self.df = pd.DataFrame()

    def quickstats(self, path):
        if not os.path.exists(path):
            d=pd.date_range("2023-03-01", periods=150, freq="D")
            tmp=pd.DataFrame({
                "date":d,
                "city":np.random.choice(["Alpha","Beta","Gamma","Delta"], len(d)),
                "AQI":np.random.randint(35,320,len(d)),
                "PM25":np.random.uniform(5,180,len(d)),
                "PM10":np.random.uniform(10,230,len(d)),
                "Temp":np.random.uniform(10,40,len(d))
            })
            tmp.to_csv(path,index=False)
        parse_cols = []
        if os.path.exists(path):
            cols = list(pd.read_csv(path, nrows=0).columns)
            if "date" in cols: parse_cols=["date"]
        self.df = pd.read_csv(path, parse_dates=parse_cols)
        if "date" in self.df.columns: self.df["date"] = pd.to_datetime(self.df["date"])

    def look(self):
        if self.df.empty: 
            print("No data to show."); return
        print(self.df.head(3)); print(self.df.tail(3))
        print("Cols->", list(self.df.columns))
        print(self.df.dtypes)

    def drawit(self):
        if self.df.empty: return
        for c in self.df.columns:
            if self.df[c].dtype.kind in "biufc": self.df[c].fillna(self.df[c].median(), inplace=True)
            else: self.df[c].fillna("Unknown", inplace=True)

    def wash(self):
        if self.df.empty: return
        print("AQI std:", round(float(self.df["AQI"].std()),2))

    def loadit(self):
        if self.df.empty: return
        plt.figure(); self.df.groupby(self.df["date"].dt.to_period("W"))["AQI"].mean().plot(); plt.ylabel("AQI weekly avg"); plt.title("LINE view"); plt.tight_layout(); plt.savefig("airquality_06_line.png"); plt.close()
        plt.figure(); self.df["AQI"].plot(kind="kde"); plt.title("KDE view 2"); plt.tight_layout(); plt.savefig("airquality_06_kde.png"); plt.close()

def show_menu():
    print("\n======================================")
    print("Pocket Suite :: Hola!")
    print("======================================")
    for i, it in enumerate(ITEMS, 1): print(f"{i}) {it}")

def main():
    app = AirqualityTool()
    while True:
        show_menu()
        pick = input(">> ").strip()
        if pick == "1":
            p = input("CSV path (blank to auto-generate): ") or "airquality.csv"
            app.quickstats(p); print("loaded ✓")
        elif pick == "2":
            app.look()
        elif pick == "3":
            app.drawit(); print("cleaned ✓")
        elif pick == "4":
            app.wash()
        elif pick == "5":
            app.loadit(); print("plots saved 📊")
        elif pick == "6":
            print("bye!"); break
        else:
            print("??")

if __name__ == "__main__":
    main()
