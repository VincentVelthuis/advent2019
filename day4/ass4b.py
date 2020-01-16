from tqdm import tqdm

low_lim = 206938
up_lim = 679128

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

def rule4(num):
  # Going from left to right, the digits never decrease;
  # they only ever increase or stay the same (like 111123 or 135679).
  for i in range(len(num)-1):
    if num[i] > num[i+1]:
      return False
  return True

n_passwords = 0
# n_rule1, n_rule2, n_rule3, n_rule4 = (0,)*4
for number in tqdm(range(low_lim, up_lim)):
  num =str(number)
  #n_rule1 += rule1(num)
  #n_rule2 += rule2(num)
  #n_rule3 += rule3(num)
  #n_rule4 += rule4(num)
  n_passwords += (rule4(num) and rule3(num) and rule2(num) and rule1(num))
#print("1:",n_rule1,"2:",n_rule2,"3:",n_rule3,"4:",n_rule4)
print(n_passwords,"possible passwords\n")
