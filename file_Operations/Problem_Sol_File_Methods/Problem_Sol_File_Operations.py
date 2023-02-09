# Python veri yapıları methodtlarını düzenli bir şekilde dosya yazdormak

#Liste methodlarını aldık
lists_method = list()
for method in dir(list):
    lists_method.append(method)

#Set methodlarını aldık
sets_methods=list()
for method in dir(set):
    sets_methods.append(method)

#String methodlarını aldık
string_methods=list()
for method in dir(str):
    string_methods.append(method)

#tuple methodlarını aldık
tuple_methods=list()
for method in dir(tuple):
    tuple_methods.append(method)

#Dict methodlarını aldık
dict_methods=list()
for method in dir(dict):
    dict_methods.append(method)

basliklar=["Lists Methods","Sets Methods","Strings Methods","Tuples Methods","Dicts Methods"]
classes=[lists_method,sets_methods,string_methods,tuple_methods,dict_methods]

max_len=0
for class_ in classes:
    if len(class_)>max_len:
        max_len=len(class_)

with open("Methods.txt", "w") as myFile:
    for i in range(max_len):
        print()
        myFile.write("\n")
        for class_ in classes:
            if i>=len(class_):
                 print("-------",end="")
                 print(" "*23,end="")
                 myFile.write("-------")
                 myFile.write(" "*23)
            else:
                 print(class_[i],end="")
                 print(" "* (30-len(class_[i])),end="")
                 myFile.write(class_[i])
                 myFile.write(" "* (30-len(class_[i])))










