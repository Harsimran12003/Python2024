#Multi Value Container
#TUPLE: Which cannot be changed, once created
        #IMMUTBALE

#homogeneous
friends= ("john","jennie","jim","jack")
print (friends, type(friends), id(friends))

#heterogeneous
friends= ("john","jennie","jim","jack",123)
print (friends, type(friends), id(friends))


print(friends[0], type(friends[0]), id(friends[0]))
print(friends[1], type(friends[1]), id(friends[1]))
print(friends[2], type(friends[2]), id(friends[2]))
print(friends[3], type(friends[3]), id(friends[3]))
print(friends[4], type(friends[4]), id(friends[4]))

#change will give error
#friends[0]="jane"

#MVC: list
#MUTABLE: can be changed 
friends= ["john","jennie","jim","jack",123]
friends[0]="jane"
print (friends, type(friends), id(friends))
