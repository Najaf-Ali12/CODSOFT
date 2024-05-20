To_do = {
  "najaf": {
    "task1": {"description": "python", "status": "pending"},
    "task2": {"description": "java", "status": "completed"},
    "task3": {"description": "webdevelopment", "status": "completed"}
  },
  "aftab": {
    "task1": {"description": "pakistanstudy", "status": "completed"},
    "task2": {"description": "communicationskills", "status": "pending"},
    "task3": {"description": "webdevelopment practice", "status": "completed"}
  },
  "mushtaque": {
    "task1": {"description": "python practice", "status": "completed"},
    "task2": {"description": "java practice", "status": "pending"},
    "task3": {"description": "webdevelopment practice", "status": "completed"}
  }
}

def Update():
  try:
    name = input("enter the name of the person whose data in to-do list you want to update:").lower()
    if name in To_do.keys():
      task = int(input("enter the task number that you want to update:"))
      new = input(f"enter the updated task at the index {task} of {name}:").lower()
      found = False  # Flag to track if task number is found
      for key, value in To_do[name].items():
        if key == f"task{task}":
          value["description"] = new  # Update description within task dictionary
          found = True
          print("Updated")
          break         
      if not found:
        print(f"Task number {task} does not exist for {name}.")
    else:
      print(f"{name} is not in the To_do list")
  except:
    print("please give valid information that is asked from you")

def Create():
  print("Thanks to create new task lists and add new tasks!")
  tasknumber = 1
  name = input("enter the name of the person who will do these works of to-do list:")
  if name not in To_do.keys():
    To_do[name] = {}  # Initialize an empty dictionary for tasks
  while True:
    ask= int(input("enter 1 if you want to add a task or 2 if you want to exit adding tasks:"))
    if ask == 1:
      task = input(f"enter the task number {tasknumber}:")
      status = input(f"Enter task status (pending/completed): ").lower()  # Track task status
      if status not in ("pending", "completed"):
          print("Invalid status. Please enter 'pending' or 'completed'.")
          continue
      To_do[name][f"task{tasknumber}"] = {"description": task, "status": status}  # Store task with details
      tasknumber += 1
    elif ask == 2:
      break
    else:
      print("INVALID CHOICE")
    
  else:
    print( name, " is already in to-do list")

def Track():
  name = input("Enter the name of the person whose tasks you want to track: ")
  if name in To_do.keys():
    print(f"\nTasks for {name}:")
    for task_id, task_details in To_do[name].items():
      print(f"{task_id}: {task_details['description']}, Status: {task_details['status']}")
  else:
    print(f"No tasks found for {name}.")
def View():
  print("To_do List")
  for key,value in To_do.items():
    print(f"\n{key}")
    for task_id,task_detail in value.items():
      print(f"- {task_detail['description']} ({task_detail['status']})")
while True:
  print("What you want to do within To_do list")
  print("1:update someones's data\n2:create a new tasklist for a new person\n3:Track To_do list\n4:View To_do lisIT\n5:EXIT")
  try:
    choice=int(input("enter 1,2,3,4 or 5:"))
    if choice==1:
      Update()
    elif choice==2:
      Create()
    elif choice==3:
      Track()
    elif choice==4:
      View()
    elif choice==5:
      break
    else:
      print("INVALID CHOICE")
  except:
    print("RECHEAK YOUR INPUTS!")

