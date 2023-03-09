#creating a dictionary
#with each items as pair
Dict=dict([(1,'python'),(2,'programming')])
print("\nDictionary with eachj item as pair;")
print(Dict)
#creating an empty dictionary
Dict={}
print("empty dictionary:")
print(Dict)
#adding elements one at a time
Dict[0]='python'
Dict[2]='program'
Dict[3]=1
print("\nDictionary after adding 3 elements:")
print(Dict)
#updating exisiting keys value
Dict[2]='welcome'
print("\nupdated key value:")
print(Dict)

#python program to demonstrate
#accessing a elemnt from a dictionary
#creating a Dictionary
Dict={1:'python','name':'Is',3:'Case-sensitive'}
#accessing a element using key
print("Accessing a elemnt using key:")
print(Dict['name'])
#accessing a elemt using get() method
print("Accessing a element using get:")
print(Dict.get(3))
#intial Dictionary
Dict={5:"welcome",6:'to',7:'python','A':{1:'python',2:'Is',3:'simple'},'B':{1:'python',2:'pramming'}}
print("intial Dictionary:")
print(Dict)
#deleting a key va;lue
del Dict[6]
print("\nDeleting a specific key:")
print(Dict)


                        
