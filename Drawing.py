from math import sqrt

from PySide6.QtCore import QSize, QPoint, QRect, Qt
from PySide6.QtGui import QPainter, QPainterPath, QPen, QTransform
from PySide6.QtWidgets import QWidget, QApplication, QFrame

S2 = sqrt(2)
S_CUBIC = 4 / 3 * (S2 - 1)
DIRECTION = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
REVERSE_DIRECTION = DIRECTION[::-1]
TANGENTS = [((0, -S_CUBIC), (-S_CUBIC, 0)),
            ((S_CUBIC, 0), (0, -S_CUBIC)),
            ((0, S_CUBIC), (S_CUBIC, 0)),
            ((-S_CUBIC, 0), (0, S_CUBIC)),
            ]


def fibonacci(count):
    numbers = []
    a, b = 0, 1
    while len(numbers) < count:
        numbers.append(b)
        a, b = b, a + b
    return numbers


def cycle(my_list, start_at=None):
    start_at = 0 if start_at is None else start_at  # my_list.index(start_at)
    while True:
        yield my_list[start_at]
        start_at = (start_at + 1) % len(my_list)


def offset_points(points, offset=QPoint(0, 0)):
    for point in points:
        point += offset


def draw_line_through_points(points):
    path = QPainterPath()
    path.moveTo(points[0])
    for point in points[1:]:
        path.lineTo(point)
    return path


def draw_cubic_through_points(points, tangents):
    path = QPainterPath()
    path.moveTo(points[0])
    for i in range(len(points) - 1):
        if i == 0:
            path.moveTo(points[0])

        path.cubicTo(tangents[i][0], tangents[i][1], points[i + 1])

    return path


class GoldenRatio:

    def __init__(self, start_point, size, count=9):
        self.start_point = start_point or QPoint(0, 0)
        self.fibonacci = fibonacci(count)
        self.size = size
        self.points = self.get_points()
        self.rects = self.get_rects()
        self.bounding_rect = self.rects[-1].united(self.rects[-2])
        self.spiral_path = draw_cubic_through_points(self.points, self.get_tangent_points())
        self.start_relative = self.start_point - self.bounding_rect.topLeft()

    def get_points(self):
        points = [self.start_point]
        p = QPoint(self.start_point)
        i = 0
        count = len(self.fibonacci)
        direction = cycle(DIRECTION, 0)
        while i < count:
            dx, dy = next(direction)
            dx, dy = dx * self.size, dy * self.size
            p += QPoint(self.fibonacci[i] * dx, self.fibonacci[i] * dy)
            i += 1
            points.append(QPoint(p))

        return points

    def get_rects(self, points=None):
        points = points or self.points
        rects = []
        for i in range(len(points) - 1):
            r = QRect(points[i], points[i + 1])
            rects.append(r.normalized())

        return rects

    def get_tangent_points(self, points=None):
        points = points or self.points
        i = 0
        count = len(points) - 1
        direction = cycle(TANGENTS, 0)
        tangents = []
        while i < count:
            p1, p2 = next(direction)
            p1 = QPoint(p1[0] * self.size * self.fibonacci[i], p1[1] * self.size * self.fibonacci[i])
            p2 = QPoint(p2[0] * self.size * self.fibonacci[i], p2[1] * self.size * self.fibonacci[i])

            tangents.append((points[i] + p1, points[i + 1] + p2, points[i + 1]))
            i += 1

        return tangents


class RuleOfThirds:

    def __init__(self, rect: QRect):
        self.path = None
        self.draw(rect)

    def draw(self, rect: QRect):
        width = rect.width()
        height = rect.height()

        self.path = QPainterPath()

        self.path.moveTo(width / 3, 0)
        self.path.lineTo(width / 3, height)
        self.path.moveTo(2 * width / 3, 0)
        self.path.lineTo(2 * width / 3, height)

        self.path.moveTo(0, height / 3)
        self.path.lineTo(width, height / 3)
        self.path.moveTo(0, 2 * height / 3)
        self.path.lineTo(width, 2 * height / 3)

        self.path.translate(rect.topLeft())


class SpiralWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        offset = QPoint(960, 540)
        self.golden = GoldenRatio(offset, 5, 12)
        self.rules = RuleOfThirds()

    def paintEvent(self, event):
        painter = QPainter(self)
        # pen_dot = QPen()
        # pen_dot.setStyle(Qt.DotLine)
        # painter.setPen(pen_dot)
        # painter.drawPath(self.path)
        # painter.drawLine(960, 0, 960, 1080)
        # painter.drawLine(0, 540, 1920, 540)

        # unit = self.unit
        # for i in range(int(540 / unit)):
        #     p1 = QPoint(960, 540 + i * unit)
        #     p2 = QPoint(960, 540 - i * unit)
        #     painter.drawText(p1, f'{i}')
        #     painter.drawEllipse(p1, 3, 1)
        #     painter.drawText(p2, f'{-i}')
        #     painter.drawEllipse(p2, 3, 1)
        #
        # for i in range(int(960 / unit)):
        #     p1 = QPoint(960 + i * unit, 540)
        #     p2 = QPoint(960 - i * unit, 540)
        #     painter.drawText(p1, f'{i}')
        #     painter.drawEllipse(p1, 1, 3)
        #     painter.drawText(p2, f'{-i}')
        #     painter.drawEllipse(p2, 1, 3)

        # painter.drawRect(self.golden.bounding_rect)

        pen = QPen()
        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        path = QPainterPath(self.golden.spiral_path)
        path.translate(-self.golden.bounding_rect.topLeft())
        painter.drawPath(self.golden.spiral_path)
        # painter.drawPath(self.rules.path)

        painter.end()


if __name__ == '__main__':
    app = QApplication()
    widget = SpiralWidget()
    widget.show()
    widget.showMaximized()
    app.exec()
