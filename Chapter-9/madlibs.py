import re
text=open('/home/govind/automatetheboringstuff/Chapter-9/Multiclipboard.txt','r')
content = text.read()
words =list(content.split())
text.close
adj=re.compile(r'ADJECTIVE')
noun=re.compile(r'NOUN')
verb=re.compile(r'VERB')
adverb=re.compile(r'ADVERB')
text_result=open('/home/govind/automatetheboringstuff/Chapter-9/Multiclipboardresult.txt','w')
text_result_string=" "
for i in words:
    if adj.match(i):
        i = adj.sub(input("Enter an adjective: "), i)
    elif noun.match(i): 
        i = noun.sub(input("Enter a noun: "), i)
    elif verb.match(i):
        i = verb.sub(input("Enter a verb: "), i)
    elif adverb.match(i):
        i = adverb.sub(input("Enter an adverb: "), i)
    text_result_string += i + " "
    text_result.write(i + " ")

print(text_result_string)
text_result.close()

