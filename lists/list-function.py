numbers = [1, 4, 45, 8, 21, 54, 90, 76]
friend_list = ["Zikri", "Fadil", "Julian", "Nabil", "Noval"]

# .extend()
friend_list.extend(numbers)
print(str(friend_list) + " example of .extend()")

# .append()
friend_list.append("Alfa")
print(str(friend_list) + " example of .append()")

# .insert()
friend_list.insert(5, "Rehan")
print(str(friend_list) + " example of .insert()")

# .pop()
friend_list.pop()
print(str(friend_list) + " example of .pop()")

# .index()
print(str(friend_list.index("Rehan")) + " example of .index()")

# .count()
print(str(friend_list.count("Rehan")) + " example of .count()")

# .sort()
numbers.sort()
print(str(numbers) + " example of .sort()")

# .reverse()
numbers.reverse()
print(str(numbers) + " example of .reverse()")

# .copy()
friend_list_copy = friend_list.copy()
print(str(friend_list_copy) + " example of .copy()")

# .remove()
friend_list.remove(1)
print(str(friend_list) + " example of .remove()")

# .clear()
# friend_list.clear()
# print(str(friend_list) + " example of .clear()")