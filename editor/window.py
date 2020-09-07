import sys
from typing import Optional
from typing import Sequence
from typing import Tuple


class Window:
    MAX_CX = sys.maxsize
    SCROLL_MARGIN = 1

    def __init__(
        self,
        lines: Optional[Sequence[str]] = None,
        width: int = 0,
        height: int = 0,
        cx: int = 0,
        cy: int = 0,
        wx: int = 0,
        wy: int = 0,
    ):
        self._lines = lines or []
        self.width = width
        self.height = height
        self.cx = cx
        self.cy = cy
        self.wx = wx
        self.wy = wy

        self._cx_hint = cx

    def up(self) -> "Window":
        if self.cy > 0:
            self.cy -= 1
            self._set_cx_after_vertical_movement()
            if self.wy > 0 and self.cy < self.wy + self.SCROLL_MARGIN:
                self.wy -= 1
        return self

    def down(self) -> "Window":
        if self.cy < len(self._lines) - 1:
            self.cy += 1
            self._set_cx_after_vertical_movement()
            if (
                # The window hasn't exceeded the file.
                self.wy + self.height < len(self._lines)
                # The cursor has exceeded the window.
                and self.cy >= self.wy + self.height - self.SCROLL_MARGIN
            ):
                self.wy += 1
        return self

    def _set_cx_after_vertical_movement(self) -> None:
        if self.cx > self._max_cx:
            # Cursor exceeded the line
            if self.cx > self._cx_hint:
                self._cx_hint = self.cx
            self.cx = max(self._max_cx, 0)
        else:
            self.cx = min(self._cx_hint, self._max_cx)

    def left(self) -> "Window":
        if self.cx > 0:
            self.cx -= 1
            self._cx_hint = self.cx
        return self

    def right(self) -> "Window":
        if self.cx < self._max_cx:
            self.cx += 1
            self._cx_hint = self.cx
        return self

    def home(self) -> "Window":
        self.cx = self._cx_hint = 0
        return self

    def end(self) -> "Window":
        self._cx_hint = self.MAX_CX
        self.cx = min(self._cx_hint, self._max_cx)
        return self

    @property
    def _max_cx(self) -> int:
        return len(self._lines[self.cy]) - 1

    def screen_cursor(self) -> Tuple[int, int]:
        return (self.cy - self.wy, self.cx - self.wx)

    def screen_lines(self) -> Sequence[str]:
        return self._lines[self.wy : self.wy + self.height]