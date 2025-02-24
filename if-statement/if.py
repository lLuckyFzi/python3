is_male = False
is_tall = True

if is_male:
    print("You are Male")
else :
    print("You are Female")

# with or
if is_male or is_tall:
    print("You are Male or Tall, or maybe both")
else :
    print("You are Female")

# with and
if is_male and is_tall:
    print("You are male")
else :
    print("You are not male")

# with elif and with and not
if is_male and is_tall:
    print("You are tall male")
elif is_male and not(is_tall):
    print("You are male but short")
elif not(is_male) and is_tall:
    print("You are Female and tall")
else :
    print("You are Female")