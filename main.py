from script import playGameAuto
from control import Player

version = 'v1.0'


if __name__ == '__main__':
    pag = playGameAuto()
    print(f'当前版本号为{version}')
    player = Player(pag)
    # player.qidong()
    # player.main()
    player.main()