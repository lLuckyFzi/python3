def translate(phrase):
    translation = ''
    for letter in phrase:
        if letter in "aiueo":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print("Mengubah huruf Vokal menjadi 'G' \n")
user_input = input("Masukkan tulisan: ")
result = translate(user_input)

print("Hasil: " + result)