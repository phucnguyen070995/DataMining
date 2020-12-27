data = open("out1.txt", encoding="utf-8").read()
data = data.decode('string-escape').decode("utf-8")
print(data)