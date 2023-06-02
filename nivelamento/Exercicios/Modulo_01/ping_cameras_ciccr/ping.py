import os
import csv

def ping(file):
  content = ""
  with open(file) as file:
    reader = csv.reader(file)

    next(reader)  # Advance past the header

    for row in reader:
      print(row[0])
      response = os.system("ping -c 1 " + row[0])

      # and then check the response...
      if response == 0:
        content += ",".join(row) + ",UP\n"
        print(row[0] + " UP")
      else:

        content += ",".join(row) + ",DOWN\n"
        print(row[0] + " DOWN")

  with open("data/pingados.csv", "w") as f:
    f.write(content)

ping("data/ipping.csv")
