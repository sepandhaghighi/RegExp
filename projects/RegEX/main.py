import re

source="asjdhjkqwhejkqgggwelkajsdkljzcnm,zcnakgsjdaa1Sd9jsalamjajsdkashdkjqwehqwkejahsdjzxckjhjkhzjckhasjdkhasd"

if __name__=="__main__":
    find_1=re.match(r"salam","salam") #Match Method
    print(find_1)
    find_2=re.search(r"salam",source) # Searh Method
    print(find_2.start()) # Start Index
    print(find_2.end()) # Last Index
    print(find_2.group()) # Groups
    print(find_2.span()) # Span Index
    print(re.sub("salam","gh",source)) # Sub method and return a string
    print(re.match(r"^gr.y","gray").group()) # ^start metacharacter and . meta character
    print(re.search(r"[A-Z][a-z][0-9]",source).group()) #Character Classes
    print(re.search(r"[^A-Z][a-z][0-9]",source).group()) # Not Of Character Classes
    print(re.search(r"q(g)*",source).group()) # * metacharacter --> 0 or more of that group
    print(re.search(r"q(g)+",source).group()) # + metacharacter --> 1 or more of that group
    print(re.search(r"q(g)?",source).group()) # ? metacharacter --> 0 or 1 of that group
    match=re.match(r"(?P<first>abc)(?:def)(ghi)","abcdefghi") # name group (?P<group_name>group) and unattached group (?:group)
    print(match.group("first"))
    print(match.groups())
    print(re.findall(r"k(q|g)",source)) # (|) or metacharacter
    
