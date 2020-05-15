def test():
    print ('test')

def test2():
    print ('test2')

#test = {'test':'blabla','test2':'blabla2'}
#for key, val in test.items():
#    key() # Here i want to call the function with the key name, how can i do so?

test = {test:'blabla', test2:'blabla2'}

for key, val in test.items():
    key()
