from tqdm import tqdm

low_lim = 206938
up_lim = 679128

def all_rules_old(num):
  return rule1(num) and rule2(num) and rule3(num) and rule4(num)

def all_rules(num):
  return rule1(num) and rule2(num) and rule3b(num) and rule4(num)

def rule1(num):
  # It is a six-digit number
  # THIS IS ALWAYS TRUE FOR THIS INPUT
  return len(num) == 6

def rule2(number):
  # The value is within the range given in your puzzle input.
  ## THIS IS ALWAYS TRUE BY DEFINITION
  return True

def rule3(num):
  #Two adjacent digits are the same (like 22 in 122345)
  for i in range(len(num)-1):
    if num[i] == num[i+1]:
      return True
  return False

def rule3b(num):
  # the two adjacent matching digits are not part 
  #   of a larger group of matching digits
  for i in range(len(num)-1):
    if num[i] == num[i+1] and i < len(num)-2:
      if num[i] == num[i+2]:
        continue
      else :
        return True
  return False

def rule4(num):
  # Going from left to right, the digits never decrease;
  # they only ever increase or stay the same (like 111123 or 135679).
  for i in range(len(num)-1):
    if num[i] > num[i+1]:
      return False
  return True

print("TESTCASES 4a:")
print("111111:",all_rules_old(str(111111)),"\tTrue",
      "\n223450:",all_rules_old(str(223450)),"\tFalse",
      "\n123789:",all_rules_old(str(123789)),"\tFalse\n")

print("TESTCASES 4b:")
print("112233:",rule3b(str(112233)),"\tTrue",
      "\n123444:",rule3b(str(123444)),"\tFalse",
      "\n666667:",rule3b(str(666667)),"\tFalse",
      "\n588999:",rule3b(str(588999)),"\tFalse",
      "\n111122:",rule3b(str(111122)),"\tTrue")
#
'''n_passwords = 0
print("\nCalculating possibilities:")
for number in tqdm(range(low_lim, up_lim)):
  password_ok = all_rules(str(number))
  n_passwords += password_ok
  if password_ok:
    print(number)
print(n_passwords,"possible passwords\n")
'''
