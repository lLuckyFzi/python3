personDetail = {
    "fullname": "Lucky Fauzi",
    "age": 21,
    "hobby": ["Basketball, Badminton, Sketching"],
}

print(personDetail["fullname"])

# With .get(key, message)
print(personDetail.get("asd", "Not Found"))
