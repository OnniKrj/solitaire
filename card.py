CARD_WIDTH = 70
CARD_HEIGHT = 100
CARD_OFFSET = 20
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
        self.card_offset = CARD_OFFSET
        self.content=ft.Container(bgcolor=self.color, width=CARD_WIDTH, height=CARD_HEIGHT)
        
        
    def move_on_top(self):
        for card in self.get_draggable_pile():
            self.solitaire.controls.remove(card)
            self.solitaire.controls.append(card)
        self.solitaire.update()
        
    def bounce_back(self):
        draggable_pile = self.get_draggable_pile()
        for card in draggable_pile:
            card.top = card.slot.top + card.slot.pile.index(card) * CARD_OFFSET
            card.left = card.slot.left
        self.solitaire.update()
        
    def place(self, slot):
        draggable_pile = self.get_draggable_pile()
        for card in draggable_pile:
            card.top = slot.top + len(slot.pile) * CARD_OFFSET
            card.left = slot.left
            
            if card.slot is not None:
                card.slot.pile.remove(card)
            
            card.slot = slot
            slot.pile.append(card)
        self.solitaire.update()
        
    def start_drag(self, e: ft.DragStartEvent):
        self.move_on_top()
        self.update()
        
    def drag(self, e: ft.DragUpdateEvent):
        draggable_pile = self.get_draggable_pile()
        for card in draggable_pile:
            card.top = max(0, self.top + e.delta_y) + draggable_pile.index(card) * CARD_OFFSET
            card.left = max(0, self.left + e.delta_x)
            card.update() 
        
    def drop(self, e: ft.DragEndEvent):
        for slot in self.solitaire.slots:
            if (
                abs(self.top - (slot.top + len(slot.pile) * CARD_OFFSET)) < DROP_PROXIMITY 
            and abs(self.left - slot.left) < DROP_PROXIMITY
            ):
                self.place(slot)
                self.update()
                return
        self.bounce_back()
        self.update()
        
    def get_draggable_pile(self):
        if self.slot is not None:
            return self.slot.pile[self.slot.pile.index(self):]
        return [self]