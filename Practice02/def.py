name = [
    {'name': 'Dias', 'id': '001'},
    {'name': 'Niyaz', 'id': '002'},
    {'name': 'Almas', 'id': '003'}
]

gpa = [
    {'id': '001', 'gpa': '3.85'},
    {'id': '002', 'gpa': '3.54'},
    {'id': '003', 'gpa': '3.12'}
]

for i in name:
    for s in gpa:
        if i['id'] == s['id']:
            print(i['name'], "-", s['gpa'])