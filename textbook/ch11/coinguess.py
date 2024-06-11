import random

while True:
    guess = ''
    while guess not in ('表', '裏'):
        print('コインの表裏を当ててください。表か裏を入力してください :')
        guess = input()
    
    toss = '表' if random.randint(0, 1) == 0 else '裏'
    
    if guess == toss:
        print('当たり！')
    else:
        print(f'はずれ！もう一回当てて！ (正解は {toss} でした)')
        guess = input()
        if guess == toss:
            print('当たり！')
        else:
            print(f'はずれ。このゲームは苦手ですね。 (正解は {toss} でした)')
