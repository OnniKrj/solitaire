CARD_WIDTH = 70
CARD_HEIGHT = 100
DROP_PROXIMITY = 20

import flet as ft

class Card(ft.GestureDetector):
    def __init__(self, solitaire, color):
        super().__init__()
        self.slot= None
        self.mouse_cursor=ft.MouseCursor.MOVE
        self.drag_interval=5
        self.on_pan_start=self.start_drag
        self.on_pan_update=self.drag
        self.on_pan_end=self.drop
        self.left=None
        self.top=None
        self.solitaire = solitaire
        self.color = color
        self.content=ft.Container(bgcolor=self.color, width=CARD_WIDTH, height=CARD_HEIGHT)