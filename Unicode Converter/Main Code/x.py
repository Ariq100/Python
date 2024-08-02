value1 = "Hello World SOMETHING ÖÖWAS OÜÄ_:"

value2 = value1.encode("UTF-32")

print(value2)

value3 = value2.decode("UTF-32")

print("\n \n ")
print(value3)