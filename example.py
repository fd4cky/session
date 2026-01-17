from main import *

canvas = Canvas()
history = EditorHistory()


print("\nДобавим так называемый круг")
circle = Circle(x=50, y=50, radius=20, color='blue')
add_circle_command = AddShapeCommand(canvas, circle)
history.execute_command(add_circle_command)
canvas.draw_all()

print("\nДобавим так называемый прямоугольник")
rectangle = Rectangle(x=100, y=100, width=60, height=40, color='red')
add_rectangle_command = AddShapeCommand(canvas, rectangle)
history.execute_command(add_rectangle_command)
canvas.draw_all()

print("\nПереместим круг далеко")
move_circle_command = MoveShapeCommand(circle, 1000, 1000)
history.execute_command(move_circle_command)
canvas.draw_all()

print("\nОтменим две последние команды")
history.undo()
history.undo()
canvas.draw_all()

print("\nОтменим отмену двух последних команд")
history.redo()
history.redo()
canvas.draw_all()