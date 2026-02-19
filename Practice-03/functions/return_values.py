def function(x,y):
    return x + y
result = function(5,3)
print(result)



def function():
    return ["apple", "banana", "pineapple"]
result = function()
for i in result():
    print(i, end=" ")



def function(x,y):
    return x + y
xx = int(input())
yy = int(input())
print(function(xx,yy)) 



def function(string1, string2):
    return string1 + " " + string2
print(function("Hello","World"))