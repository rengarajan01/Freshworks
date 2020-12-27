import main
import threading
import time

str = input("Do you want to do the process?(y/n)")
while(str == 'y' or str == 'Y'):
    print("Do you want to use multi-threading?(y/n)")
    ss = input()
    if ss == 'y'or ss =='Y':
        print("1.Create\n2.Read\n3.Delete")
        choice = int(input())
        if choice == 1:
            print("Enter key (only string)")
            key = input()
            print("Enter Value")
            val = input()
            print("Enter Time to live (only integer)")
            ttl = int(input())
            try:
                thread1 = threading.Thread(target =(main.create),args=(key,val,ttl,) )
                thread1.start()
            except:
                print("Error!")
        elif choice == 2:
            print("Enter key (only string)")
            key = input()
            try:
                thread2 = threading.Thread(target =(main.read),args=(key,) )
                thread2.start()
            except:
                print("Error!")
        elif choice == 3:
            print("Enter key (only string)")
            key = input()
            try:
                thread3 = threading.Thread(target =(main.delete),args=(key,) )
                thread3.start()
            except:
                print("Error!")
    else:
        print("1.Create\n2.Read\n3.Delete")
        choice = int(input())
        if choice == 1:
            print("Enter key (only string)",end="")
            key = input()
            print("Enter Value",end="")
            val = input()
            print("Enter Time to live (only integer)",end="")
            ttl = int(input())
            main.create(key,val,ttl)
        elif choice == 2:
            print("Enter key (only string)")
            key = input()
            main.read(key)
        elif choice == 3:
            print("Enter key (only string)")
            key = input()
            main.delete(key)
    str = input("Do you want to do the process?(y/n)")