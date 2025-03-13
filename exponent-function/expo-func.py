def power_of_num(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print("Perpangkatan \n")
user_input = input("Masukkan angka: ")
pow = input("Masukkan pangkat: ")
result = power_of_num(int(user_input), int(pow))

print("Hasil dari " + str(user_input) + " Pangkat " + str(pow) + " adalah: " + str(result))