f=open("base_dataset.txt","r")
lines=f.readlines()
f.close() 

f=open("base_dataset2.txt","w")
for i in lines:
    sentence="START\* " + "START\* "+i
    f.write(sentence)