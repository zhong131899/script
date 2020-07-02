import time


class Player:
    def __init__(self, pag):
        self.pag = pag

    def qidong(self):
        self.pag.start()
        for pic in [self.pag.img_guanggao, self.pag.img_meiri, self.pag.img_huodong]:
            self.pag.guan_bi(pic)
        while not self.pag.panduan(self.pag.img_zhuomian):
            if self.pag.panduan(self.pag.img_zhuomian):
                print('已成功登陆桌面')
                pass
            time.sleep(1)
        print('未成功登录桌面，请手动检测登陆桌面')

    def main(self):
        while True:
            print(
                '''
                选择你想要的操作：
                1、进入作战
                2、领取任务奖励
                3、领取基建
                ······（完善中）
                q、退出


                ''')
            shuru = input()
            if shuru == '1':
                print('请在2s内切换至明日方舟')
                self.jrzz()
            elif shuru == '2':
                print('请在2s内切换至明日方舟')
                while not self.pag.panduan(self.pag.img_renwu):
                    self.pag.tuichu()
                self.pag.renwu()
                while not self.pag.panduan(self.pag.img_renwu):
                    self.pag.tuichu()
                print('finished!')
            elif shuru == '3':
                print('请在2s内切换至明日方舟')
                if not self.pag.panduan(self.pag.img_isjz):
                    self.pag.tuichu()
                self.pag.jj()
                self.pag.jjtc()

            elif shuru == 'q':
                self.pag.end()
                break

    def xuanze(self):
        print('''选择要刷的材料本：
        1、龙门币
        ······
        5、术士材料
        6、特种材料
        扩充ing
        ''')
        shuru = input()
        print('''
        要刷几次?
        ''')
        num = int(input('输入要刷的次数：'))
        time.sleep(2)
        if shuru == '1':
            usetime = 180
            return self.pag.img_wzcb, self.pag.img_hwys, self.pag.img_5, num, usetime
        elif shuru == '5':
            usetime = 180
            return self.pag.img_xpss, self.pag.img_cklx, self.pag.img_2, num, usetime
        elif shuru == '6':
            usetime = 180
            return self.pag.img_xpss, self.pag.img_sxsz, self.pag.img_1, num, usetime

    def jrzz(self):
        pic1, pic2, pic3, num, usetime = self.xuanze()
        time.sleep(2)
        self.pag.zm()
        if not self.pag.panduan(self.pag.img_zhuomian):
            print('请切换至游戏后重试')
            pass
        self.pag.zuozhan(pic1, pic2, pic3)
        for i in range(num):
            self.pag.xingdong()
            self.pag.xdjs(usetime)
        self.pag.zm()
        print('完成作战')

    def zd(self):
        self.qidong()
        pic1, pic2, pic3, num, usetime = self.pag.img_wzcb,  self.pag.img_hwys, self.pag.img_5, 4, 180
        time.sleep(2)
        self.pag.zm()
        if not self.pag.panduan(self.pag.img_zhuomian):
            self.pag.end()
        self.pag.zuozhan(pic1, pic2, pic3)
        for i in range(num):
            self.pag.xingdong()
            self.pag.xdjs(usetime)
        self.pag.zm()
        print('完成作战')
        while not self.pag.panduan(self.pag.img_renwu):
            self.pag.tuichu()
        self.pag.renwu()
        while not self.pag.panduan(self.pag.img_renwu):
            self.pag.tuichu()
        print('finished!')
        self.pag.jj()
        self.pag.jjtc()
        self.pag.end()
