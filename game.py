from Invetory import Inventory
from Item import Item


class Player:
    def __init__(self, name, inventory):
        self.name = name 
        self.invetory = inventory
        

def create_character():
    name = input("Digite o nome do personagem: ")
    invertory = Inventory()
    return name, invertory
        
while True:
    print('''
      Selecione uma opcao
      1 - Criar Personagem
      2 - Verificar inventário
      3 - Adicionar item
      4 - Remover item
      5 - Finalizar
    ''')
    option = input(": ")
    
    global character
    
    match option:
        case '1':
            name, invetory = create_character()
            character = Player(name, invetory)
        case '2':
            character.invetory.list_items()
        case '3':
            name = input('Digite o nome do item: ')
            kind = input('Digite o tipo do item: ')
            value = input('Digite o valor do item: ')
            item = Item(name, kind, value)
            character.invetory.add_item(item)
        case '4':
            character.invetory.remove_item()
        case '5':
            break
        case _:
            continue