todos=[]

while True:
    user_action=input('''enter your choice
     add 
     show 
     complete                 
     exit : ''')
    
    match user_action:
        case 'add':
            n=int(input("ENTER THE NUMBER OF TASK TO ADD : "))
          
            for items in range(n):
                todo=input("ENTER THE TASK : ")
                found=False
                for strings in todos:
                    if strings.lower() in todo.lower() or todo.lower() in strings.lower():
                        found=True
                        break
                if found:
                    print("ALREADY ADDED")
                else:
                    todos.append(todo)
            
        case 'show':
            for item in todos:
                print(item)
            print("THESE ARE PENDING TASKS : ")
        
        case 'complete':
            comp = input("ENTER TASK TO COMPLETE : ")
            found = False
            for task in todos:
               if task.strip().lower() == comp.strip().lower():
                  todos.remove(task)
                  found = True
                  print("COMPLETED")
                  break
            if not found:
                print("Task not found in the list.")

            
                       
        case 'exit':
            break
        

