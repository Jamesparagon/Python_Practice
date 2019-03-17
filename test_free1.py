#coding=utf-8

list1 = ['a','b','c','c','z','d']
list2 = ['z','d','ls']
list3 = []
for i in list2:
    if i not in list1:
        list3.append(i)
print(list3)


matches = [{'match_day':1,'match_no':101,'sum':1234},{'match_day':5,'match_no':301,'sum':5678},{'match_day':3,'match_no':3,'sum':4728},{'match_day':4,'match_no':401,'sum':1359},{'match_day':5,'match_no':300,'sum':1413},{'match_day':3,'match_no':3,'sum':1354},{'match_day':4,'match_no':402,'sum':1333},{'match_day':2,'match_no':300,'sum':2561}]
matches_dic = {}
for i in matches:
    if i['match_day'] not in matches_dic:
        matches_dic[i['match_day']] = i['sum']
    else:
        matches_dic[i['match_day']] += i['sum']
result = sorted(set(matches_dic.items()))
for i in result:
    print(i[0],i[1])









































def format_name(s):
    s1 = s[0:1].upper() + s[1:].lower()
    return s1
result = map(format_name, ['james','mAadDDFDF','tOm'])
print(list(result))

