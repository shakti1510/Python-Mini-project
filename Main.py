import sys
def check_empty(a):
    if a==[]:
        return 'Underflow'
    else:
        return 
def add_value(a,n):
    a.append(n)
def delete_value(a,b):
    if b in a:
        a.remove(b)
    else:
        sys.stderr.write('the element doesnt exist')
def rev_value(a):
    b= []
    if check_empty(a)=='Underflow':
        print('list is empty')
    else:
        b=a[::-1]
        print('the reversed list is:')
        print(b)
def sort_value(a):
    if check_empty(a)=='Underflow':
        print('list is empty')
    else:
        for i in range(0,len(a)):
            for j in range(len(a)-i-1):
                if a[j]<a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]
        print('sorted value list is')
        print(a)
def search_values(a,n):
    if check_empty(a)=='Underflow':
        print('list is empty')
    else:
        print('the position of',n,'=')
        for i in range(len(a)):
            if n==a[i]:
                print(i)
def display_values(a):
    if check_empty(a)=='Underflow':
        print('list is empty')
    else:
        print(a)
def show_topandbottom(a):
    if check_empty(a)=='Underflow':
        print('list is empty')
        print('so no values are there for showing you the top and bottom values')
    else:
        b=0
        e=len(a)-1
        print('_________________________')
        print('   the top value is',a[b])
        print('            and         ')
        print('the bottom value is',a[e])
        print('_________________________')
def summing_values(a):
    s=0
    try:
        if check_empty(a)=='Underflow':
            print('this list is empty')
        else:
            for i in range(len(a)):
                s=s+a[i]
            print(s)
        #this is for finding the
        #sum of all elements of teh list
        #we are using try just to check that the list is empty or not
    except:
        print('              Oopsi                 ')
        print('        the list is empty           ')

"""till here we studied about the list operations 
now lets see about the SQL table operations 
Soo........ . let's go """
import mysql.connector
c=mysql.connector.connect(host='localhost',user='root',passwd='root',database='XIIA')
cr=c.cursor()
def add(cb):
    try:
        sql='''insert into customer values(%d,'%s',%d,'%s','%s','%s',%d)'''%(cb[0],cb[1],cb[2],cb[3],cb[4],cb[5],cb[6])
        cr.execute(sql)
        print('______________________________')
        print('    addition is successful')
        print('______________________________')
        #this is just for the 
        #confirmation for the execution of the program
        c.commit()
    except:
        #if program goes to this 
        #it means , it is having a error in the execution
        c.rollback()
        print('           Oopsi               ')
        print('there is a problem in execution')
        print('________________________________')
    print('choose the next one')
def delete(b):
    try:
        sql="delete from customer where c_no=%d"%(b)
        cr.execute(sql)
        c.commit()
        print('_______ oo lala _________')
        print('   deletion is complete  ')
        print('_________________________')
        #as the above this also the same
    except:
        c.rollback()
        print('______________oo no__________________')
        print('there is a big problem , please check')
        #think of it there might be problem
        #think
    print('Go to next Or')
    print('retry this by reentering')
def upgrade_name():
    d=input('enter the name whose data should be changed')
    b=input('enter the updated Item_name ')
    try:
        sql="update customer set Item_name='%s' where name='%s'"%(b,d)
        cr.execute(sql)
        c.commit()
        print('_________________________')
        print('    value is updated     ')
        print('_________________________')
    except:
        c.rollback()
        sys.stderr.write('there is a error')
def display_table():
    try:
        sql="select*from customer"
        cr.execute(sql)
        b=cr.fetchall()
        for i in b:
            print(i)
        c.commit()
        print('                ')
        print('_________________________')
        print('the values are displayed ')
        print('_________________________')
        #this is for displaying 
        #So dont worry for it
    except:
        c.rollback()
        sys.stderr.write('there is a error')
def get_itfrom_hell(b):
    try:
        sql="select*from customer where name='%s'"%(b)
        cr.execute(sql)
        b=cr.fetchall()
        print(b)
        c.commit()
        print('                         ')
        print('_________________________')
        print('   value is displayed    ')
        print('_________________________')
    except:
        c.rollback()
        print('________oh no____________')
        print('    there is a problem   ')
        print("_________________________")
        sys.stderr.write('there is a error')
def modify_table(a,b):
    try:
        sql="alter table customer modify  %s %s "%(a,b)
        cr.execute(sql)
        c.commit()
        print('________________________')
        print('modification is complete')
        print('________________________')
    except:
        c.rollback()
        print('_ _ _ _ _  _ _ _ _ _Oopsi_ _ _ _ _ _ _ _ _ _ _')
        print('there is a error in the program please check')
        print('-----------------------------------------------')
        sys.stderr.write('there is a error')
c.close()

def add_filevalues(f,a):
    g=open(f,'a')
    g.write(a)
    g.close()
    #this function is to add
def count_file(f):
    c=0
    with open (f,'r') as g:
        b=g.read()
        for i in b.split():
            c+=1
    print(c)
def count_letter(f):
    c=0
    with open(f,'r') as g:
        b=g.read()
        for i in b:
            if i.isalpha():
                c+=1
    return c
def count_one(f,n):
    c=0
    with open(f,'r') as g:
        b=g.read()
        for i in b.split():
            if n==i:
                c+=1
        return c
def count_gl(f,n):
    c=0
    with open(f,'r') as g:
        b=g.read()
        for i in b.split():
            if n==i[0]:
                c+=1
        return c
def displayfile(f):
    with open(f,'r') as g:
        print(g.read())


a=[]
f=input('enter the file to be used')
while True:
    print('                             Hi Users                                  ')
    print('Myself computer is here to show you some functions which can be done on')
    print('                            Using python                                ')
    print('1.list')
    print('2.text file')
    print('3.SQL tables')
    print('4.Exit')
    print('enter the choice in integer like=1 or 2 etc')
    #this is important to the user to know the choice
    print('make your choice ')
    z='''ooue 
    enter your choice da'''
    ch=int(input(z))
    #as the argumentis in string and
    #if you will give string/floating pt number/some thing else
    #pc will reply ' af go to hell'
    if ch==1:
        # so now we are starting with list 
        #these are common fuctions 
        #but are nice and understandable
        while True:
            print('            so you want to start with list       ')
            print('                     nice                        ')
            print("                 ok let's start                  ")
            print('        the given below are the operations       ')
            print('             which can be done in list           ')
            print('No.1.adding a single value to list')
            print('No.2.adding a list of values')
            print('No.3.deleting values to list')
            print('No.4.reversing the list')
            print('No.5.finding the all value from the list')
            print('No.6.finding the top and bottom values of the list')
            print('No.7.finding the sum of all elements of the list')
            print('No.8.to print sorteed list and keeping the original list safe')
            print('No.9.to find the given value')
            print('No.10.Exit from the program')
            print('        the order for this is like=1 or 2 etc      ')
            print('enter your suitable choice')
            p=int(input())
            if p==1:
                print('enter the choice to be added')
                n=int(input())
                try:
                    add_value(a,n)
                    print('_______________________________________')
                    print('now the values you have given are added')
                    print('_______________________________________')
                except:
                    sys.stderr.write('      there is a error      ')
            elif p==2:
                print('please note the values should be entered in the form of list')
                a=eval(input('enter the list of values to be added'))
                b=list(a)
                for i in range(len(b)):
                    add_value(a,b[i])
                print('the list of values are been added')
            elif p==3:
                print('   enter the values to be deleted  ')
                c=int(input(':'))
                try:
                    delete_value(a,c)
                    print('----------------------------------------')
                    print('      the value is been deleted         ')
                    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
                except:
                    sys.stderr.write('   there is a error     ')
            elif p==4:
                try:
                    rev_value(a)
                    print('____________________________________________________')
                    print('the above values are the reversed values of the list')
                    print('____________________________________________________')
                except:
                    print('          there is a problem in reversing           ')
            elif p==5:
                try:
                    display_values(a)
                    print("------------------------------------------------------------")
                    print(" the above values are the values stored in the list till now")
                    print("------------------------------------------------------------")
                except:
                    sys.stderr.write('         there is a error         ')
            elif p==6:
                try:
                    show_topandbottom(a)
                    print('-----------------------------------------------------------')
                    print('               these are the ends of the list              ')
                    print('-----------------------------------------------------------')
                except:
                    sys.stderr.write('          there is a error             ')
            elif p==7:
                try:
                    summing_values(a)
                    print('============================================================')
                    print('         this is the sum of all values of the list          ')
                    print('============================================================')
                except:
                    sys.stderr.write('                there is a error                 ')
            elif p==8:
                #now we are sorting values of the list
                try:
                    print('okk as you wish')
                    sort_value(a)
                    print('this is the sorted values')
                except:
                    sys.stderr.write('there is a error')
            elif p==9:
                try:
                    n=int(input('enter the value'))
                    search_values(a,n)
                except:
                    sys.stderr.write('there is a error')
            elif p==10:
                print('Are you sure ?')
                print('Mmmmm OK then')
                break
            else:
                print('Oooooohh')
                sys.stderr.write('wrong choice')
    elif ch==2:
        h=open(f,'w')
        h.write(' \n')
        h.close()
        while True:
            print(' Now you are in a text file program ')
            print('  these are the used for text file  ')
            print('          and they are              ')
            print('No.1.adding an one word/one line to the text file ')
            print('No.2.adding many lines to the text file')
            print('No.3.count the total no of words')
            print('No.4.count the no of letter in the file')
            print('No.5.count the no of given words')
            print('No.6.count the no of words starting from the given word')
            print('No.7.display the text file')
            print('No.8.Exit')
            print('the order for this is like=1 or 2 etc')
            l=input('enter your choice=')
            if l=='1':
                print("add the word below")
                s=input('enter the line to be added')
                p=' '+s+' '
                add_filevalues(f,p)
                print('___________________________')
                print('  the word has been added  ')
                print('___________________________')
            elif l=='2':
                s=input('enter the line to be added')
                a='\n'+s+'\n'
                add_filevalues(f,a)
                print('___________________________')
                print('  the word has been added  ')
                print('___________________________')
            elif l=='3':
                print('the no of words are')
                count_file(f)
                print('_________________________') 
            elif l=='4':
                c=count_letter(f)
                print('the total no of letters in file is ')
                print('                ',c,'              ')
                print('___________________________________')
            elif l=='5':
                n=input('enter the word to be counted')
                c=count_one(f,n)
                print('the no of words of the given word ',n,'is')
                print('                   ',c,'                 ')
                print('_________________________________________')
            elif l=='6':
                n=input('enter the letter=')
                print('the no of words starting with',n,'is')
                print('                ',count_gl(f,n),'               ')
                print('____________________________________')
            elif l=='7':
                displayfile(f)
            elif l=='8':
                print('this is the values stored in text file')
                print('Mmmm ok')
                print('your wish')
                break
            else:
                sys.stderr.write('wrong choice')
    elif ch==3:
        import mysql.connector 
        c=mysql.connector.connect(host='localhost',user='root',passwd='root',database='XIIA')
        cr=c.cursor()
        while True:
            print('       Now you are in a SQL program       ')
            print('  these are the used for SQL programming  ')
            print('          and they are              ')
            print('No.1.adding  the details of the new customer ')
            print('No.2.deleting the details of the given customer')
            print('No.3.Upgrading information  of the  given customer')
            print('No.4.displaying the entire list of the customer of our shop')
            print('No.5.displaying the details of the of the given customer')
            print('No.6.add a new column to the customer list ')
            print('No.7.Exit')
            print('the order for this is like=1 or 2 etc')
            z=int(input('enter your choice='))
            if z==1:
                cb=[]
                w=int(input('enter rno'))
                b=input('enter name')
                x=int(input('enter age'))
                d=input('enter aadhar')
                e=input('enter item name')
                f=input('enter quantity')
                g=int(input('enter price'))
                cb=cb+[w,b,x,d,e,f,g]
                add(cb)
            elif z==2:
                b=int(input('enter the c_no of whose the data should be deleted='))
                delete(b)
            elif z==3:
                upgrade_name()
            elif z==4:
                display_table()
            elif z==5:
                b=input('enter the name whose data should be displayed')
                get_itfrom_hell(b)
            elif z==6:
                a=input('enter the name of the new column')
                b=input('enter the data type of the table')
                modify_table(a,b)
            elif z==7:
                break
            else:
                sys.stderr.write('wrong choice')
    elif ch==4:
        print('ookkbye and have a nice day')
        break
        #this is the end of the program 
        #i think you had a nice journey of 400+ lines so bye
    else:
        sys.stderr.write('wrong choice')
