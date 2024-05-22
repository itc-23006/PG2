from functools import reduce

stuff = {'ロープ': 1, 'たいまつ': 6, '金貨': 42, '手裏剣': 1, '矢': 12}

def display_inventory(inventory):
    print("持ち物リスト:")
    item_total = reduce(lambda total, item: total + item[1], map(lambda item: (print(f"{item[0]}: {item[1]}"), item)[1], inventory.items()), 0)
    print("アイテム総数: " + str(item_total))

display_inventory(stuff)
