list=['car',3,5,True,4,4]
#ordered,changeable and allow duplicates
print(list)
list[2:4]='doll',3,"sell"
list.insert(5,"dell")
list.append("rell")
list.remove(3)
print(list)
print(len(list))
print(type(list))
print(list[2:4])

tuple=("rekd",4,3.54,"foll")
#ordered, unchangeable and allows duplicates
print(tuple)
print(type(tuple))
print(tuple[0])

#unordered, can be changed but DO NOT ALLOW DUPLLICATE
dicttionary={
    "name":"saif",
    "age":21,
    "vehicle":"ferrari"
}
print(type(dicttionary))
print(dicttionary["vehicle"])
#same
print(dicttionary.get("vehicle"))
#to remove
dicttionary.pop("name")
print(dicttionary)

