#store sides of rectangle in a json file and find perimetr and divide by 3 and get ceil value using math and save result in other json file
import json
import math
with open("rect.json", "r") as file:
    data = json.load(file)
    a = data["a"]
    b = data["b"]
    perimeter = 2 * (a + b)
    result = math.ceil(perimeter / 3)
    with open("result.json", "w") as file:
        json.dump({"result": result}, file)



        