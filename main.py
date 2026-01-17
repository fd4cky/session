from figures import *
from commands import *


class Canvas:
    """Представляет собой холст, который может содержать и отображать различные геометрические фигуры."""

    def __init__(self):
        """Инициализирует пустой холст.

        Список shapes будет хранить все добавленные фигуры.
        """
        self.shapes = []

    def add_shape(self, shape):
        """Добавляет фигуру на холст.

        Args:
            shape (Shape): Объект фигуры, который нужно добавить. Должен быть экземпляром класса Shape.

        Raises:
            TypeError: Если переданный объект не является экземпляром класса Shape.
        """
        if not isinstance(shape, Shape):
            raise TypeError(f"{shape} это левый обьект")
        self.shapes.append(shape)

    def remove_shape(self, shape):
        """Удаляет фигуру с холста.

        Args:
            shape (Shape): Объект фигуры, который нужно удалить.

        Raises:
            ValueError: Если фигуры нет на холсте
        """
        if shape not in self.shapes:
            raise ValueError(f"{shape} нету на холсте")
        self.shapes.remove(shape)

    def draw_all(self):
        """Отрисовывает все фигуры, находящиеся на холсте.

        Каждая фигура вызывает свой метод draw для отображения. (но сейчас там только принт :( )
        """
        print("\nВсе фигуры на холсте:")
        if not self.shapes:
            print("холст пуст")
            return
        for shape in self.shapes:
            shape.draw(self)


class EditorHistory:
    """Класс для управления историей команд, позволяющий отменять и повторять действия.

    Использует два стека: undo_stack для выполненных команд, которые можно отменить,
    и redo_stack для команд, которые были отменены и могут быть повторены.
    """

    def __init__(self):
        """Инициализирует пустые стеки для операций отмены и повтора."""
        self.undo_stack = []
        self.redo_stack = []

    def execute_command(self, command):
        """Выполняет команду и добавляет ее в стек отмены.

        При выполнении новой команды стек повтора очищается, так как история после текущей точки становится неактуальной.

        Args:
            command (EditorCommand): Команда для выполнения.
        """
        command.execute()
        self.undo_stack.append(command)
        self.redo_stack.clear()

    def undo(self):
        """Отменяет последнюю выполненную команду.

        Перемещает отмененную команду в стек повтора.
        """
        if not self.undo_stack:
            print("Отменять нечего")
            return
        command = self.undo_stack.pop()
        command.undo()
        self.redo_stack.append(command)

    def redo(self):
        """Повторяет последнюю отмененную команду.

        Перемещает повторенную команду обратно в стек отмены.
        """
        if not self.redo_stack:
            print("Повторять нечего")
            return
        command = self.redo_stack.pop()
        command.execute()
        self.undo_stack.append(command)
