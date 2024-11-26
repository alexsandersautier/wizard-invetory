class Inventory:
    def __init__(self):
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
        
    def remove_item(self):
        self.list_items()
        item = input('Digite código do item: ')
        self.items.pop(int(item) - 1)
    
    def list_items(self):
        if len(self.items) < 1:
            print("Inventário vazio")
            return
        print("Itens no inventário: ")
        for i, item in enumerate(self.items):
            print(f'{i+1} - {item.name} do tipo {item.kind} com o valor {item.value}')
        