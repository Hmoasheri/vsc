import easygui
import os
import sys
t=easygui
letters=['f','n',' ','.','!','?','@','h','s','k','r','l','u','m','p','i','y','j','w','q','t','b','c','a','z','d','e','g','v','o','x']
val=['2','f','u','6','q','i','@','4','h','*','%','c','7','d','#','x','y','a','3','v','s','&','p','g','9','t','b','3','!','1','w','5','k','8','z','0','$',]
s=''
def atc(text):
    command = ('echo ' + text.strip() + '| clip')
    os.system(command)
def en(x):
    z=''
    for a in x:
        y=letters.index(a)
        e=val[y]
        z=e+z
    t.msgbox(z)
    atc(z)
def de(x):
    w=''
    for a in x:
        y=val.index(a)
        e=letters[y]
        w=e+w
    t.msgbox(w)
while(True):
    s=t.enterbox("1.encrypt\n2.decrypt\n4.exit")
    if(s=='1'):
        d=t.enterbox("enter your words : ")
        en(d)
    elif(s=='2'):
        v=t.enterbox("enter your code :  ")
        de(v)
    elif(s=='4'):
        break
    else:
        t.msgbox("sorry wrong")
        

    
