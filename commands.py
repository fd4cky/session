from abc import ABC, abstractmethod


class EditorCommand(ABC):
    """Абстрактный базовый класс для всех команд редактора.

    Этот класс определяет общий интерфейс для команд, которые могут быть выполнены
    и отменены.
    """
    @abstractmethod
    def execute(self):
        """Выполняет действие команды."""
        pass

    @abstractmethod
    def undo(self):
        """Отменяет действие команды."""
        pass


class AddShapeCommand(EditorCommand):
    """Команда для добавления фигуры на холст."""

    def __init__(self, canvas, shape):
        """Инициализирует команду добавления фигуры.

        Args:
            canvas (Canvas): Объект холста, куда будет добавлена фигура.
            shape (Shape): Объект фигуры, которую нужно добавить.
        """
        self.canvas = canvas
        self.shape = shape

    def execute(self):
        """Выполняет добавление фигуры на холст."""
        self.canvas.add_shape(self.shape)

    def undo(self):
        """Отменяет добавление фигуры, удаляя ее с холста.

        Для отмены используется ссылка на саму фигуру и холст, сохраненные при инициализации команды.
        """
        self.canvas.remove_shape(self.shape)


class RemoveShapeCommand(EditorCommand):
    """Команда для удаления фигуры с холста.

    Реализует паттерн Command для операции удаления фигуры, позволяя ее отменить.
    """

    def __init__(self, canvas, shape):
        """Инициализирует команду удаления фигуры.

        Args:
            canvas (Canvas): Объект холста, с которого будет удалена фигура.
            shape (Shape): Объект фигуры, которую нужно удалить.
        """
        self.canvas = canvas
        self.shape = shape

    def execute(self):
        """Выполняет удаление фигуры с холста."""
        self.canvas.remove_shape(self.shape)

    def undo(self):
        """Отменяет удаление фигуры, добавляя ее обратно на холст.

        Для отмены используется ссылка на саму фигуру и холст, сохраненные при инициализации команды.
        """
        self.canvas.add_shape(self.shape)


class MoveShapeCommand(EditorCommand):
    """Команда для перемещения фигуры."""

    def __init__(self, shape, dx, dy):
        """Инициализирует команду перемещения фигуры.

        Args:
            shape (Shape): Перемещаемый объект фигуры.
            dx (int): Смещение по оси x.
            dy (int): Смещение по оси y.
        """
        self.shape = shape
        self.dx = dx
        self.dy = dy
        # Сохраняем оригинальные координаты для возможности отмены
        self.original_x = shape.x
        self.original_y = shape.y

    def execute(self):
        """Выполняет перемещение фигуры, изменяя ее координаты."""
        self.shape.x += self.dx
        self.shape.y += self.dy

    def undo(self):
        """Отменяет перемещение фигуры, восстанавливая ее исходные координаты."""
        self.shape.x = self.original_x
        self.shape.y = self.original_y


class ChangeColorCommand(EditorCommand):
    """Команда для изменения цвета фигуры."""

    def __init__(self, shape, new_color):
        """Инициализирует команду изменения цвета фигуры.

        Args:
            shape (Shape): Объект фигуры, цвет которой нужно изменить.
            new_color (str): Новый цвет для фигуры.
        """
        self.shape = shape
        self.new_color = new_color
        # Сохраняем оригинальный цвет для возможности отмены
        self.original_color = shape.color

    def execute(self):
        """Выполняет изменение цвета фигуры на новый."""
        self.shape.color = self.new_color

    def undo(self):
        """Отменяет изменение цвета фигуры, восстанавливая ее исходный цвет."""
        self.shape.color = self.original_color
