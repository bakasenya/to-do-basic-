todolist = []

class Todolist:
    
    
    def add_task(self, task):
        todolist.append(task)
        
    def remove_task(self, task):
        if task in todolist:
            todolist.remove(task)
        
    def view_task(self, task):
        if not todolist:
            print("Your todo-list is empty")
        else:
            print(f"Your todo-list:")
            for task in todolist:
                print(f"- {task}")
    

def main():
    todo = Todolist()
    
    while True:
        
        user_input = (input("Menu\n1.Add a task\n2.Remove a task\n3.View to-do list?\n4.Exit.\nEnter your choice: "))
        
        if user_input == "4":
            print("Exiting todo list. Have a good day!")
            break
            
        if user_input == "1":
            task = input("Enter your task: ")
            todo.add_task(task)
            
        elif user_input == "2":
            task = input("Which task do you want to remove? ")
            todo.remove_task(task)
            
        elif user_input == "3":
            todo.view_task(task)
            
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()