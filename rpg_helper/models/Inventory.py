

class Inventory:
    def __init__(self, user_id: str, item: str):
        self.user_id = user_id
        self.item = item

    def __str__(self):
        return self.item