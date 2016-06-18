import re

source="asjdhjkqwhejkqgggwelkajsdkljzcnm,zcnakgsjdaa1Sd9jsalamjajsdkashdkjqwehqwkejahsdjzxckjhjkhzjckhasjdkhasd"

if __name__=="__main__":
    find_1=re.match(r"salam",source)
    print(find_1)
    find_2=re.search(r"salam",source)
    print(find_2.start())
    print(find_2.end())
    print(find_2.group())
    print(find_2.span())
    print(re.sub("salam","gh",source))
    print(re.match(r"^gr.y","gray").group())
    print(re.search(r"[A-Z][a-z][0-9]",source).group())
    print(re.search(r"[^A-Z][a-z][0-9]",source).group())
    print(re.search(r"q(g)*",source).group())
    print(re.search(r"q(g)+",source).group())
    print(re.search(r"q(g)?",source).group())
    match=re.match(r"(?P<first>abc)(?:def)(ghi)","abcdefghi")
    print(match.group("first"))
    print(match.groups())
    print(re.findall(r"k(q|g)",source))
