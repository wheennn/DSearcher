# DSearcher — v0.2
# Est. 25.05.2026
# by wheen

import time
import platform
import os
import re

clear = "cls" if platform.system() == "Windows" else "clear"
is_enter = False

superscripted_characters = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
common_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

powers = ["1", "1"]
coeffs = [0, 0, 0]
solutions = [0, 0, 0]
substituted_solutions = [0, 0]

coeff_names = ["a", "b", "c"]
solution_names = ['x₁', 'x₂', 'x']
substituted_solution_names = ['t₁', 't₂']

errors_list = ["", "Error. Too much signs.", "Error. Not a quadratic, biquadratic or quasi-quadratic equation.", "Error. Input is empty.", "Error. The square root of discriminant isn't perfect.", "Error. The converted solution isn't perfect square.", "Error. Contains unsupported type of characters."]

while is_enter == False: 
 name_and_ver = ["D", "S", "e", "a", "r", "c", "h", "e", "r", " ", "—", " ", "v", "0", ".", "2"]
 author = ["b", "y", " ", "w", "h", "e", "e", "n"]
 os.system(clear)
 for i in name_and_ver:
  ascii_tags = ["\033[1m", "\033[0m"] if i in ("D", "S") else ["", ""]
  print(ascii_tags[0] + i + ascii_tags[1], end="")
  if name_and_ver.index(i) in (9, 10, 11, 12, 13, 14, 15):
   time.sleep(0.125)
  else:
   time.sleep(0.25)
 time.sleep(0.75)
 print("")
 for i in author:
  print(i, end="")
  time.sleep(0.125)
 time.sleep(0.75)
 print("\n\nPress Enter to start ", end="")
 is_enter = True if input("") == "" else False
mode = "menu"
is_enter = False

def maths_dispatcher(equation: str):
 global power_full_matches, coeff_full_matches, powers
 error_num = 0
 powers = ['1', '1']

 upcycled_equation = equation_upcycling(equation)

 power_full_matches = [upcycled_equation, ""]
 coeff_full_matches = [upcycled_equation, "", ""]

 error_num = error_dispatcher(upcycled_equation, powers, 0)

 if error_num == 0:
  power_type = power_type_identification(equation)

 if error_num == 0:
  for i in range(len(power_full_matches)):
   powers[i], power_full_matches[i] = power_search(power_full_matches[i], i, power_type)
   if i == 0:
    power_full_matches = equation_slicer(upcycled_equation, "powers")
   powers[i] = powers_converter(powers[i], power_type)

 if error_num == 0:
  error_num = error_dispatcher(upcycled_equation, powers, 1)

 if error_num == 0:
  equation_type, error_num = equation_type_classification(powers)

 if error_num == 0:
  coeffs = [1, 1, 1]
  for i in range(len(coeffs)):
   coeff_full_matches[i], coeffs[i] = coefficient_search(coeff_full_matches[i], i) 
   coeff_full_matches = equation_slicer(upcycled_equation, "coeffs") 

 if error_num == 0:
  discriminant = discriminant_arithmetic(coeffs)

 if error_num == 0:
  discriminant_root, error_num = discriminant_root_arithmetic(discriminant) 

 if error_num == 0:
  solutions, substituted_solutions, error_num = solutions_arithmetic(coeffs, discriminant_root, equation_type) 

 if error_num != 0: 
  error_num, coeffs, discriminant, discriminant_root, solutions, substituted_solutions, power_type, equation_type = error_num, [1, 1, 1], 0, 0, [0, 0, 0], [0, 0], "", ""
 return error_num, coeffs, discriminant, discriminant_root, solutions, substituted_solutions, power_type, equation_type

def equation_upcycling(equation: str) -> str:
 upcycled_equation = str(equation).replace(" ", "").replace("=0", "").replace("-", "-").replace("–", "-").replace("—", "-").replace("―", "-")
 return upcycled_equation

def power_type_identification(equation: str) -> str:
 global powers
 superscript_count = 0
 for i in range(10):
  superscript_count += equation.count(superscripted_characters[i])
 if superscript_count > 0:
  power_type = "superscripted"
  powers = ['¹', '¹']
 else:
  power_type = "normal"
  powers = ['1', '1']
 return power_type

def equation_type_classification(powers: list) -> str:
 error_num = 0
 if int(powers[0]) == 2 and int(powers[1]) == 1:
  equation_type = "quadratic"
 elif int(powers[0]) == 4 and int(powers[1]) == 2:
  equation_type = "biquadratic"
 else:
  equation_type = "quasi-quadratic"
 return equation_type, error_num

def error_dispatcher(equation: str, powers: list, i: int) -> int:
 signs = equation.count("-") + equation.count("+")
 error_num = 0
 nums, symbols = 0, 0
 special_characters = ["x", "^"]
 for x in range(len(common_characters)):
  nums += equation.count(common_characters[x])
  nums += equation.count(superscripted_characters[x])
  if x in (0, 1):
   symbols += equation.count(special_characters[x])
 
 contains_unsupported_symbols = True if len(equation) - nums - signs - symbols > 0 else False
 
 if i == 0: # pt. 0
  if equation == "":
   error_num = 3
  if signs > 3:
   error_num = 1
  if contains_unsupported_symbols == True:
   error_num = 6

 elif i == 1: # pt. 1
  if int(powers[0]) == int(powers[1]) * 3:
   error_num = 2
  if int(powers[0]) != int(powers[1]) * 2:
   error_num = 2

 return error_num

def powers_converter(power: str, power_type: str) -> int:
 if not power or power in ("1", "¹"):
  power = "1"
  return power
 if power_type == "superscripted":
  try:
   power = str(superscripted_characters.index(power))
  except ValueError:
   pass
 return str(power)

def power_search(equation: str, i: int, power_type: str) -> str:
 worked = False
 converted_match = "1"
 limit = 1

 try:
  if power_type == "normal": 
   converted_match = re.search(r"x\^(.*?)-", equation).group()
  elif power_type == "superscripted":
   converted_match = re.search(r"x(.*?)-", equation).group()
  power_full_matches[i] = converted_match
  converted_match = converted_match.removeprefix("x").removeprefix("^").removesuffix("+").removesuffix("-")
  worked = True
 except AttributeError:
  converted_match = "1"

 if len(converted_match) > limit:
  worked = False
  converted_match = "1"

 if worked == False: 
  try:
   if power_type == "normal":
    converted_match = re.search(r"x\^(.*?)\+", equation).group()
   elif power_type == "superscripted":
    converted_match = re.search(r"x(.*?)\+", equation).group()
   power_full_matches[i] = converted_match
   converted_match = converted_match.removeprefix("x").removeprefix("^").removesuffix("+").removesuffix("-")
   worked = True
  except AttributeError:
   converted_match = "1"

 if len(converted_match) > limit:
  worked = False
  converted_match = "1"

 powers[i] = str(converted_match)
 return powers[i], power_full_matches[i]

def equation_slicer(equation: str, method: str):
 if method == "powers": 
  power_full_matches[1] = equation[len(power_full_matches[0]):]
  return power_full_matches
 
 elif method == "coeffs": 
  if len(coeff_full_matches) > 0 and coeff_full_matches[0]:

   start1 = len(coeff_full_matches[0])
   remaining = equation[start1:]
   coeff_full_matches[1] = remaining 

   if "x" in remaining:
    last_x = remaining.rfind("x")
    coeff_full_matches[2] = remaining[last_x+1:]
   else:
    coeff_full_matches[2] = remaining

  return coeff_full_matches
 
def coefficient_search(equation: str, iteration: int) -> int:
 global coeff_names
 coefficient, worked, full_match = 1, False, "1"

 try:
  if iteration == 0:
   full_match = re.search(r"(.*?)x", equation).group()
  elif iteration == 1:
   full_match = re.search(r"\+(.*?)x", equation).group()
  elif iteration == 2:
   if "+" in equation:
    full_match = equation.split("+")[-1]
   elif "-" in equation:
    full_match = -int(equation.split("-")[-1])
   else:
    full_match = equation
  coefficient = str(full_match).removeprefix("+").removesuffix("x")
  worked = True
 except AttributeError:
  coefficient = 1

 if iteration == 0 and "x" in str(full_match):
  if str(full_match).startswith("x"):
   coefficient = 1
   worked = True
  if str(full_match) == "-x":
   coefficient = -1
   worked = True

 if worked == True:
  try: 
   coefficient = int(coefficient)
  except ValueError:
   worked = False
   coefficient = 1

 if worked == False: 
  try:
   if iteration in (0, 1): 
    full_match = re.search(r"-(.*?)x", equation).group()
   elif iteration == 2:
    if "+" in equation:
     full_match = equation.split("+")[-1]
    elif "-" in equation:
     full_match = -int(equation.split("-")[-1])
    else:
     full_match = equation
   coefficient = str(full_match).removeprefix("+").removesuffix("x")
   worked = True
  except AttributeError:
   coefficient = 1

 if iteration == 0 and "x" in str(full_match):
  if str(full_match).startswith("x"):
   coefficient = 1
   worked = True
  if str(full_match) == "-x":
   coefficient = -1
   worked = True

 if worked == True:
  try: 
   coefficient = int(coefficient)
  except ValueError:
   worked = False
   coefficient = 1

 if coefficient == "":
  coefficient = 1
 if coeff_names[iteration] == "a" and coefficient == "":
  coefficient = 1
 coeff_full_matches[iteration], coeffs[iteration] = full_match, coefficient
 return coeff_full_matches[iteration], coeffs[iteration]

def discriminant_arithmetic(coeffs: list) -> int:
 discriminant = (int(coeffs[1]) * int(coeffs[1])) - (4 * (int(coeffs[0]) * int(coeffs[2])))
 if discriminant == None:
  discriminant = 0
 return discriminant
 
def discriminant_root_arithmetic(discriminant: int) -> int:
 error_num = 0
 discriminant_root = 0
 index = 0
 started_time = int(time.time())
 while True:
  index += 1
  current_time = int(time.time())
  if discriminant == index * index:
   discriminant_root = index
   break
  elif discriminant == (index * -1) * (index * -1):
   break
  elif current_time - started_time == 1 and discriminant != (index * -1) * (index * -1) and discriminant != index * index:
   break
 return discriminant_root, error_num

def solutions_arithmetic(coeffs: list, discriminant_root: int, equation_type: str) -> tuple[list, list, int]:
 error_num = 0
 coeffs[0], coeffs[1], coeffs[2] = int(coeffs[0]), int(coeffs[1]), int(coeffs[2])
 for i in range(len(solutions) - 1):
  math = int((-coeffs[1] - discriminant_root) / (2 * coeffs[0])) if i == 0 else int((-coeffs[1] + discriminant_root) / (2 * coeffs[0]))
  
  if equation_type == "quadratic":
   solutions[i] = math
  elif equation_type in ("biquadratic", "quasi-quadratic"):
   substituted_solutions[i] = math

 if equation_type in ("biquadratic", "quasi-quadratic"):
  for i in range(len(substituted_solutions)):
   started_time = int(time.time())
   index = 0
   while True:
    index += 1
    current_time = int(time.time())
    math_string = "index"
    for x in range((int(powers[0]) // 2) - 1):
     math_string += " * index"
    resulted = eval(math_string, {"index": index})
    neg_resulted = eval(math_string, {"index": -index})
    if substituted_solutions[i] == resulted and substituted_solutions[i] == neg_resulted:
     solutions[i] = index * -1, index
     break
    elif substituted_solutions[i] == neg_resulted:
     solutions[i] = index * -1
     break
    elif substituted_solutions[i] == resulted:
     solutions[i] = index
     break
    else:
     if current_time - started_time == 1:
      break

 for i in solutions: 
  if i == solutions[2]:
   pass
  if str(i).startswith("-") and i not in substituted_solutions:
   index = solutions.index(i)
   correct = index + 1 if index == 0 else index - 1 if index == 1 else index
   solutions[2] = solutions[correct]

 return solutions, substituted_solutions, error_num 

while True and is_enter == False:
 os.system(clear)
 print("Enter a quadratic, biquadratic or quasi-quadratic equation: ")
 given_eq = input("")
 os.system(clear)
 error_num, coeffs, discriminant, discriminant_root, solutions, substituted_solutions, power_type, equation_type = maths_dispatcher(given_eq)
 statuses = ["Upcycling an equation..", "Checking up the powers..", "Searching coefficients..", "Calculating the discriminant..", "Calculating square root of the discriminant..", "Finding solutions.."]
 status_sleepings = [0.5, 0.75, 0.75, 1, 0.75, 1.25] 

 for i in statuses:
  current_sleep = status_sleepings[statuses.index(i)]
  print(f"\r\033[K{i}", end="", flush=True)
  time.sleep(current_sleep)

 os.system(clear)
 if error_num == 0:
  print("Quadratic equation" if equation_type == "quadratic" else "Biquadratic equation" if equation_type == "biquadratic" else "Quasi-quadratic equation")
  print(given_eq)

  if int(powers[0]) > 2:
   print(f"t = x^{int(powers[0]) // 2}" if power_type == "normal" else f"t = x{superscripted_characters[int(powers[0]) // 2]}")
   if power_type == "normal":
    print(given_eq.replace(f"x^{int(powers[0]) // 2}", "t").replace(f"x^{int(powers[0])}", "t^2"))
   elif power_type == "superscripted":
    print(given_eq.replace(f"x{superscripted_characters[int(powers[0]) // 2]}", "t").replace(f"x{superscripted_characters[int(powers[0])]}", "t²"))

  for x in coeff_names:
   y = coeffs[coeff_names.index(x)]
   print(f"{x} = {y}")
  print(f"D = {coeffs[1]}² - 4 * ({coeffs[0]} * {coeffs[2]}) = {discriminant}")
  if discriminant_root != 0:
   print(f"√D = {discriminant_root}")

  if discriminant_root != 0:
   lists = substituted_solutions if int(powers[0]) > 2 else solutions
   list_names = substituted_solution_names if int(powers[0]) > 2 else solution_names

   for x in list_names:

    if list_names.index(x) in (0, 1):
     y = lists[list_names.index(x)]
     sign = "-" if x == list_names[0] else "+" if x == list_names[1] else ""
     print(f"{x} = {-coeffs[1]} {sign} {discriminant_root} / 2 * {coeffs[0]} = {y}")

   if lists == substituted_solutions and str(solutions[0]).startswith("-") == False and str(solutions[1]).startswith("-") == False:

    print(f"{solution_names[0]} = {str(solutions[0]).replace(",", ";").replace("[", "").replace("]", "").replace("(", "").replace(")", "")}")
    print(f"{solution_names[1]} = {str(solutions[1]).replace(",", ";").replace("[", "").replace("]", "").replace("(", "").replace(")", "")}")

   if str(solutions[0]).startswith("-") and str(solutions[1]).startswith("-"):
    print("The equation has no real roots.")

   if solutions[2] != 0 and equation_type in ("biquadratic", "quasi-quadratic") and str(solutions[0]).count("-") + str(solutions[1]).count("-") != 2:
    negative_solution = solutions[0] if str(solutions[0]).startswith("-") else solutions[1]
    print(f"x ≠ {negative_solution}")
    print(f"x = {solutions[2]}")

  else:
   print("The equation has no real roots.")

 elif error_num != 0:
  print(errors_list[error_num])
 user_input = input("")
 is_enter == True if user_input else False