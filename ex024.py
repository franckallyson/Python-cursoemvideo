name = str(input('Enter a name:')).strip()
name_caps = name.lower()
if name_caps.find('santo') == 0:
    print("This name start with 'Santo'")
else:
    print("This name don't start with 'Santo'")

