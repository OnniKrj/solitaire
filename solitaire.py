import flet as ft

'''
Card dragging with GestureDetector's on_pan_update
'''

class Solitaire:
    def __init__(self):
        self.start_top = 0
        self.start_left = 0

def main(page: ft.Page):

    def bounce_back(game, card):
        '''return card to it's starting position'''
        card.top = game.start_top
        card.left = game.start_left
        page.update()

    def start_drag(e: ft.DragStartEvent):
        solitaire.start_top = e.control.top
        solitaire.start_left = e.control.left
        e.control.update()

    def drop(e: ft.DragEndEvent):
        if (
            abs(e.control.top - slot.top) < 20
            and abs(e.control.left - slot.left) < 20
        ):
            place(e.control, slot)

        else:
            bounce_back(solitaire, e.control)
    
    def place(card, slot):
        '''place card to the slot'''
        card.top = slot.top
        card.left = slot.left
        page.update()

    def drag(e: ft.DragUpdateEvent):
        e.control.top = max(0, e.control.top + e.delta_y)
        e.control.left = max(0, e.control.left + e.delta_x)
        e.control.update()

    card = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=5,
        on_pan_start=start_drag,
        on_pan_update=drag,
        on_pan_end=drop,
        left=0,
        top=0,
        content=ft.Container(bgcolor=ft.colors.GREEN, width=70, height=100),
    )

    slot = ft.Container(
        width=70, height=100, left=200, top=0, border=ft.border.all(1)
    )

    solitaire = Solitaire()

    page.add(ft.Stack(controls=[slot, card], width=1000, height=500))

ft.app(target=main)

