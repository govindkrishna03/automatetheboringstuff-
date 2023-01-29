import pyinputplus as pyip
Price={'wheat':1,
       'white':1,
       'sourdough':5,
       'chicken':10,
       'turkey':9,
       'ham':5,
       'tofu':7,
       'cheddar':2,
       'Swiss':1,
       'Mozzarela':5,
       'mayo':2,
       'mustard':1,
       'lettuce':1,
       'tomato':1}
Order=[]
Total=0
bread_type=pyip.inputMenu(['wheat','white','sour dough'])
Order.append(bread_type)
protien_type=pyip.inputMenu(['chicken','turkey','ham','tofu'])
Order.append(protien_type)
Cheese_needed=pyip.inputYesNo('Sir,Do you need cheese?: ')
if Cheese_needed=='yes':
    cheese_type=pyip.inputMenu(['cheddar','swiss','mozzarella'])   
    Order.append(cheese_type)
extras=['mayo', 'mustard', 'lettuce', 'tomato']
choice=''
for i in extras:
    choice = pyip.inputYesNo('Would you like ' + i +'?\n')
    if choice == 'yes':
        Order.append(i)
    else:
        choice = ''

no_of_sandwiches=pyip.inputInt('Total no of sandwiches needed: ',min=1)
for i in Order:
    if i in Price.keys():
        Total+=Price.get(i) 
print('Total bill: ',Total)
