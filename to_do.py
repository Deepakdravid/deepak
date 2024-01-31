todos=[]

while True:
    user_action=input('''enter your choice
     add 
     show 
     complete                 
     exit : ''')
    
    match user_action:
        case 'add':
            todo=input("ENTER NEW TASK : ")
            todos.append(todo)
            file=open('todos.txt','w')
            file.writelines(todos)
            file.close()
        case 'show':
            for item in todos:
                print(item)
            print("THESE ARE PENDING TASKS : ")
        
        case 'complete':
            if(user_action=='complete'):
                com=input("ENTER TASK TO COMPLETE : ")
                todos.remove(com)
                print("COMPLETED")
            
                       
        case 'exit':
            break
