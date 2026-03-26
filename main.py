import name 
name.greeting("Samira")

a=name.p1["age"]
b=name.p1["country"]
print(a)
print(b)
 

print("До изменения")
with open('nabi.txt', 'r') as file:
    content = file.read()
    print(content)

print("Добавить в конце")
with open('nabi.txt', 'a') as file:
    file.write("saranghe\n")
    print(content)

print("Добавить в начале")
with open('nabi.txt', 'r') as file:
    old_content = file.read()

with open('nabi.txt', 'w') as file:
    file.write("Meow\n" + old_content)
    
print(old_content)