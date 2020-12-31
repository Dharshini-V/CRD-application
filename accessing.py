


import code as x 


x.create("sas",25)


x.create("sr",70,3600) 


x.read("sas")


x.read("sr")


x.create("sas",50)



x.modify("sas",55)


 
x.delete("sas")

t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()

