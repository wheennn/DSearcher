import time
import os
import re

print(
  "You're welcome to Discriminant Searcher or DSearcher. I'm fast solver of your quadratic equations. Type your classic math problem and I will solve it for you.\n"
  "UPD: Don't type the '=0' at the end or -a at the start\n"
  "Example: x²-6x+8 or x² - 6x + 8"
)
full_eq = input("").replace(" ", "")
print("Finding coefficients...")
time.sleep(2)
os.system('cls')
signs_q = full_eq.count('-') + full_eq.count('+')

expected_diapazone_a = "" # A PART
if signs_q == 2: 
 a = 1
elif signs_q >= 3:
 print("Sorry, I can't help with that. At the moment I'm programmed to solve only the easiest equations. Try to type something smaller like x²-6x+8")
 time.sleep(5)
 exit()
 if "-" in full_eq[0:5]:
  cord_as, cord_ae = re.search(r"-(.*?)x", full_eq).span()
  a = full_eq[cord_as:cord_ae - 1]
 else:
  print("I don't see any minuses before the a. It's seem you misunderstood me, type me a quadratic equation without '=0' at the end.")
  time.sleep(5)
  exit()

print(f"Coefficients for {full_eq}:")
time.sleep(2)
print(f"a = {a}")
time.sleep(2)

expected_diapazone_b = "" # B PART
if signs_q == 2:
 if "-" in full_eq[0:5]:
  tuple_b = re.search(r"-(.*?)x", full_eq).span()
  cord_bs, cord_be = tuple_b
  b = int(full_eq[cord_bs:cord_be - 1])
 elif "+" in full_eq[0:5]: 
  tuple_b = re.search(r"\+(.*?)x", full_eq).span()
  cord_bs, cord_be = tuple_b
  b = int(full_eq[cord_bs + 1:cord_be - 1])
else:
 print("Sorry, I can't help with that. At the moment I'm programmed to solve only the easiests equations. Try to type something smaller like x²-6x+8")
 time.sleep(5)
 exit()

print(f"b = {b}")
time.sleep(2)

expected_diapazone_c = "" # C PART
if signs_q == 2:
 if "-" in full_eq[5:7]:
  tuple_c = re.search(r"-\d+$", full_eq).span()
  cord_cs, cord_ce = tuple_c
  c = int(full_eq[cord_cs:cord_ce])
 elif "+" in full_eq[5:7]:
  tuple_c = re.search(r"\+\d+$", full_eq).span()
  cord_cs, cord_ce = tuple_c
  c = int(full_eq[cord_cs + 1:cord_ce])
else:
 print("Sorry, I can't help with that. At the moment I'm programmed to solve only the easiests equations. Try to type something smaller like x²-6x+8")
 time.sleep(5)
 exit()

print(f"c = {c}")
time.sleep(2)
os.system('cls')

print("Finding discriminant...")
time.sleep(3)

discriminant = int(b) * int(b) - 4 * (int(a) * int(c))
print(f"D = b² -4 * (a * c) = {b}² - 4 * ({a} * {c}) = {discriminant}")
time.sleep(1)
print(f"Your discriminant for this quadratic equation is {discriminant}")

print("Finding square root of the discriminant..")
time.sleep(3)

for i in range(100):
 if discriminant == i * i:
  d_root = i
  break
 
print(f"√D = {d_root}")
time.sleep(1)
print(f"Your square root of the discriminant for this quadratic equation is {d_root}")

print("Finding x₁ and x₂..")
time.sleep(3)

x1 = int(- b - d_root) / (2 * a)
x2 = int(- b + d_root) / (2 * a)

print(f"x₁ = (-b - √D) / (2 * a) = {int(x1)}")
print(f"x₂ = (-b + √D) / (2 * a) = {int(x2)}")

print("\nHere are your answers! Tell me if you will need more help.")
time.sleep(5)
exit()