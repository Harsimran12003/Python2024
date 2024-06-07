#DICTIONARY
#key value ordering
#we do indexing by providing key value

friend= {101: "john", 102:" jennie", 103:"jack"}
print(friend, type(friend), id(friend))
print(friend[102])

friend= {"jj": "john", "je":" jennie", "ja":"jack"}
print(friend["ja"])

num= {1: "CALL", 2:"MESSAGE", 3:"CALL BACK"}


instagram= {"ben": {"joe","jim", "fionna", "harry", "joe"},
            "kane":{"joe", "george", "fionna", "jack"}}

print(instagram["ben"])
print(instagram["ben"] & instagram["kane"])

#update
friend= {"jj": "john", "je":" jennie", "jj":"jack"}
print(friend["jj"])   #data is overwritten