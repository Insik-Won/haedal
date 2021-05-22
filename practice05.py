import turtle
import csv

turtle.shape('turtle')

with open("turtle_data.csv", 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        command = line[0]
        value = int(line[1])
        if (command == 'f'):
            turtle.forward(value)
        elif (command == 'r'):
            turtle.right(value)
        else:
            print('알 수 없는 명령어입니다.')

turtle.mainloop()



