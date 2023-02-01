import re


password = 'krish@1234leo'
com = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[#?!@$%^&*-]).{8,}$')
ans = com.findall(password)
print(ans)