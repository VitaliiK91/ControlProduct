def main():
  N = int(input("Please enter N:"))
  if N < 2 or N > 10000:
    print("You fucked up!!!")
    return
  numbers = []
  for i in range(0,N):
    numbers.append(int(input()))
  R = int(input("Please enter R:"))
  expected_R = find_control_number(numbers,N)
  print("Expected number is:" + str(expected_R))
  if(R == expected_R):
    print("Passed")
  else:
    print("Failed")

def find_control_number(numbers, N):
  found = False
  check = numbers[0] * numbers[1]
  for i in range(1, N - 1):
    for j in (i+1, N - 1):
      if(numbers[i] != numbers[j]):
       mult =  numbers[i] * numbers[j]
       if (mult % 6 == 0 and mult < check ):
         found = True
         check = mult
  if found:
    return check
  else:
    return 0
main()