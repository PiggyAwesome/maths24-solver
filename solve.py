import random
import threading

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

try:
 a = int(input("Enter number 1: "))
 b = int(input("Enter number 2: "))
 c = int(input("Enter number 3: "))
 d = int(input("Enter number 4: "))
except ValueError:
    print("Invalid numbers!")
    exit()

w = a
x = b
y = c
z = d
e = [w, x, y, z]
def threadtarget(e):
 numbers = random.shuffle(e)
 print(e)
 a = e[0]
 b = e[1]
 c = e[2]
 d = e[3]
 
 
 x1 = random.choice('+-*/')
 x2 = random.choice('+-*/')
 x3 = random.choice('+-*/')
 try:
  math = eval(f"{a} {x1} {b} {x2}{c} {x3} {d}")
  sum = str(f"{a} {x1} {b} {x2} {c} {x3} {d}")
 except ZeroDivisionError:
     pass
 try:
  number = 1
  while math != 24:
      print(colored(252, 3, 224,f"Try Number: ") + colored(200, 1, 500,f"{number} ") + colored(240, 246, 175, f"| {sum} = {math}"))
      x1 = random.choice('+-*/')
      x2 = random.choice('+-*/')
      x3 = random.choice('+-*/')
      sum = str(f"{a} {x1} {b} {x2} {c} {x3} {d}")
      math = eval(sum)
      if math != 24:
              sum = str(f"({a} {x1} {b}) {x2} {c} {x3} {d}")
              math = eval(sum) 
              print(colored(252, 3, 224,f"Try Number: ") + colored(200, 1, 500,f"{number} ") + colored(240, 246, 175, f"| {sum} = {math}"))
              number += 1
              if math != 24:
               sum = str(f"({a} {x1} {b} {x2} {c}) {x3} {d}")
               math = eval(sum) 
               print(colored(252, 3, 224,f"Try Number: ") + colored(200, 1, 500,f"{number} ") + colored(240, 246, 175, f"| {sum} = {math}"))
               number += 1
               if math != 24:
                sum = str(f"({a} {x1} ({b} {x2} {c})) {x3} {d}")
                math = eval(sum) 
                print(colored(252, 3, 224,f"Try Number: ") + colored(200, 1, 500,f"{number} ") + colored(240, 246, 175, f"| {sum} = {math}"))
                number += 1
                if math != 24:
                 sum = str(f"(({a} {x1} {b}) {x2} {c}) {x3} {d}")
                 math = eval(sum) 
                 print(colored(252, 3, 224,f"Try Number: ") + colored(200, 1, 500,f"{number} ") + colored(240, 246, 175, f"| {sum} = {math}"))
                 number += 1
                 if math != 24:
                  sum = str(f"({a} {x1} ({b} {x2} {c}) {x3} {d})")
                  math = eval(sum) 
                  print(colored(252, 3, 224,f"Try Number: ") + colored(200, 1, 500,f"{number} ") + colored(240, 246, 175, f"| {sum} = {math}"))
                  number += 1
 
  
      numbers = random.shuffle(e)
      a = e[0]
      b = e[1]
      c = e[2]
      d = e[3]
      number += 1
      if number >= 69420:
          print(f"Try Number: {number} | There is no awnser")
          exit()
  print("\n\n"+sum + " = " + str(math))
  print(colored(100, 91, 244,(f'Found Awnser on attempt {number}\n\n🔥 ') + colored(240, 246, 175,('https://github.com/PiggyAwesome 🔥'))))
 except ZeroDivisionError:
     pass
 
threading.Thread(target = threadtarget(e), daemon=True).start
threading.Thread(target = threadtarget(e), daemon=True).start
threading.Thread(target = threadtarget(e), daemon=True).start
