#using if and elif
is_male=False
is_tall=True
if is_male and is_tall:
    print("You are a tall male")   
elif is_male and not(is_tall):
    print("You are male but not tall")
elif not(is_male) and is_tall:
    print("You are tall but not male")
else:
  print("yor are neither tall nor male")