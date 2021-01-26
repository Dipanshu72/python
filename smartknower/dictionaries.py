dipanshu ={'rishi':20,'suman':19,'puja':18,'gracia':17}
print(dipanshu['rishi'])


smaple ={1:'abc',"kholi":142,1.1:41,True:'xyz'}
print(smaple.keys())
print(smaple.values())
#insertation of key-value

smaple['tom']=10
smaple['marshel']=20
print(smaple)


#deletion of key-value
del(smaple['tom'])
print(smaple)


#list vs dictonaries

list=['mayank',40,'shubman',30,'pujara',50,'bumrah',70]
dict={'mayank':40,'shubman':30,'pujara':50,'bumrah':70}
print(list[7])
print(dict['bumrah'])