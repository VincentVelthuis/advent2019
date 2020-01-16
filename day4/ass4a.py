from tqdm import tqdm

low_lim = 206938
up_lim = 679128

def rule1(number):
  # It is a six-digit number
  return len(str(number)) == 6

def rule2(number):
  # The value is within the range given in your puzzle input.
  ## THIS IS ALWAYS TRUE BY DEFINITION
  return True

def rule3(number):
  #Two adjacent digits are the same (like 22 in 122345)
  string = str(number)
  for i in range(len(string)-1):
    return string[i] == string[i+1]
  return False



boolean_rule1 = 0
boolean_rule3 = 0
boolean_total = 0
for number in tqdm(range(low_lim, up_lim)):
  boolean_rule1 += rule1(number)
  boolean_rule3 += rule3(number)
  boolean_total += (rule1(number) and rule3(number))
print(boolean_rule1)
print(boolean_rule3)
print(boolean_total)
