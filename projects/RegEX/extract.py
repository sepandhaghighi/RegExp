import re


if __name__=="__main__":
    file=open("email.txt","r")
    source=file.read()
    find_1=re.findall(r"[\w\.-]+@[\w\.-]+\.com",source)
    print(find_1)
