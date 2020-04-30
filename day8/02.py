import random
score = 0
def show_intro():
    intro = "Ты долго блуждал по миру, чтобы найти сокровища дракона и, наконец, подобрался к его логову, где он их хранит, перед тобой две двери, и ты должен выбрать одну из них!"
    print(intro)

def choose_cave():
    cave = ""
    while cave != "1" and cave != "2":
        print("Выбирай, странник! 1 или 2")
        cave = input()
    return cave


def check_cave(cave, score):
    print('Дракон раскрывет свою пасть и .......')
    good_cave = random.randint(1, 2)
    good_cave = str(good_cave)
    if cave == good_cave:
        score = score + 1
        print('Делится с тобой своими сокровищами! Твой счёт:', score)
    if cave != good_cave:
        score =  0
        print('cъел тебя')

play_again = "Да"
while play_again == "Да":
    show_intro()
    my_cave = choose_cave()
    check_cave(my_cave, score)
    print('Начать сначала?')
    play_again = input()
