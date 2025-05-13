def task():
   tasks = []
   print("----- Welcome To The File Manager Task -----")
   total_task = int(input("Please Enter That How Many Tasks You Want To Add: "))
   for i in range(1, total_task+1):
     task_name = input(f"Please Enter Task{i}: ")
     tasks.append(task_name)

   print(f"Today's Tasks Are\n{tasks}")

   while True:
     operation = int(input("Please Enter The Number Of Operation You Want To Perform:\n1- Add\n2- Update\n3- View\n4- Delete\n5- Exit/Stop:\n Enter = ")) 
     if operation == 1:
         add = input("Enter The Task You Want To Add: ")
         tasks.append(add)
         print(f"Task '{add}' Has Been Successfully Added.....")

     elif operation == 2:
         update_tsk = input("Enter The Task You Want To Update: ")
         if update_tsk in tasks:
              up = input("Please Enter The New Task: ")
              ind = tasks.index(update_tsk)
              tasks[ind] = up
              print(f" '{up}' Task Has Been Updated Successfully.....Here's The Updated Task's List.....\n {tasks}")
         
         else:
             print(f" '{update_tsk}' Doesn't Exist...Please Enter Existed Task Name To Update.....")
     
     elif operation == 3:
           print(f"Total Tasks Are..... {tasks}")
     
     elif operation == 4:
         del_value = input("Enter The Task Name You Want To Delete: ")
         if del_value in tasks:
             ind = tasks.index(del_value)
             del tasks[ind]
             print(f" '{del_value}' Task Has Been Deleted Successfully.....")
         
         else:
             print(f" '{del_value}' Doesn't Exist...Please Enter The Existed Task Name To Delete.....")

     elif operation == 5:
           print(f"Your App Has Been Closed..... ")
           break
     else:
         print("Invalid Input: Please Enter Valid Operation.....")
       
task()         

