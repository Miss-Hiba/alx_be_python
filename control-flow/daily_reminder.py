task=input("enter your task : ")
priority=input("priority (high, medium, low) : ")
time_bound=input("is it time-bound ? (yes or no) : ")
if priority=="high" and time_bound=="yes" :
    print(task ,"is a high priority task that requires immediate attention today!")
elif priority=="low" and time_bound=="no" :
    print(task ,"is a low priority task. Consider completing it when you have free time.")
elif priority=="high" and time_bound=="no" :
    print(task ,"is a high priority complete it as soon as possible!")
else :
    print(task ,"is a low priority.but, you still have to finish it.")
