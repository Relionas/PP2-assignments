import re

# 1
print(bool(re.match(r'^ab*$', 'abbbb')))

# 2
print(bool(re.match(r'^ab{2,3}$', 'abb')))

# 3
print(re.findall(r'^[a-z]+_[a-z]+$', 'hello_world'))

# 4
print(re.findall(r'[A-Z][a-z]+', 'Hello World Test'))

# 5
print(bool(re.match(r'^a.*b$', 'axxxb')))

# 6
text = "Hello, world. Python is cool"
print(re.sub(r'[ ,.]', ':', text))

# 7 Snake → Camel
def snake_to_camel(text):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), text)

print(snake_to_camel("hello_world_test"))

# 8 Split at uppercase
print(re.split(r'(?=[A-Z])', 'HelloWorldTest'))

# 9 Insert spaces before capitals
print(re.sub(r'(?<!^)(?=[A-Z])', ' ', 'HelloWorldTest'))

# 10 Camel → Snake
def camel_to_snake(text):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()

print(camel_to_snake("HelloWorldTest"))