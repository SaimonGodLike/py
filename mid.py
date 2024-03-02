import datetime

with open("input1.txt", "r") as a:
    lines = a.readlines()

p1 = datetime.datetime.strptime(lines[1].strip(), "%Y-%m-%d").date()
p2= datetime.datetime.strptime(lines[2].strip(), "%Y-%m-%d").date()
p3 = datetime.datetime.strptime(lines[3].strip(), "%Y-%m-%d").date()

oldest = min(p1, p2, p3)
dates = [p1, p2, p3]
dates.sort()

with open("output2.txt", "w") as b:
    b.write(f"The oldest one: {oldest}\n")
    b.write("From youngest to older:\n")
    for date in dates:
        b.write(f"{date}\n")

print("All answer is in output.txt.")
