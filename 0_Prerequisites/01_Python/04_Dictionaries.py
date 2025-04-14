user = {
    "name": "Alice",
    "age": 25
}

print(user["age"])


# Use can used get to avoid KeyError :
print(user.get("age"))  # Safer if key might not exist