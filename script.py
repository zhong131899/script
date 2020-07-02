import time
import pyautogui as pag
from pywinauto import application
import sys
import ctypes


class playGameAuto:
    def __init__(self):
        self.app_base = application.Application(backend="uia")
        self.app = self.app_base.start(
                r"D:\明日方舟\emulator\nemu\EmulatorShell\NemuLauncher.exe -p com.hypergryph.arknights")
        self.img_start = r'caiyang\start.png'
        self.img_huanxing = r'caiyang\huanxing.png'
        self.img_huodong = r'caiyang\huodong.png'
        self.img_meiri = r'caiyang\meiri.png'
        self.img_guanggao = r'caiyang\guanggao.png'
        self.img_renwu = r'caiyang\renwu.png'
        self.img_richang = r'caiyang\richang.png'
        self.img_lingqu = r'caiyang\lingqu.png'
        self.img_isrenwu = r'caiyang\isrenwu.png'
        self.img_tuichu = r'caiyang\tuichu.png'
        self.img_zuozhan = r'caiyang\zuozhan.png'
        self.img_xpss = r'caiyang\xpss.png'
        self.img_cklx = r'caiyang\cklx.png'
        self.img_2 = r'caiyang\2.png'
        self.img_isdaili = r'caiyang\isdaili.png'
        self.img_daili = r'caiyang\daili.png'
        self.img_ksxd = r'caiyang\ksxd.png'
        self.img_ksxd2 = r'caiyang\ksxd2.png'
        self.img_xdjs = r'caiyang\xdjs.png'
        self.img_zhuomian = r'caiyang\zhuomian.png'
        self.img_hqwz = r'caiyang\hqwz.png'
        self.img_isgkzm = r'caiyang\isgkzm.png'
        self.img_gkzm = r'caiyang\gkzm.png'
        self.img_skip = r'caiyang\skip.png'
        self.img_iscaigou = r'caiyang\iscaigou.png'
        self.img_caigou = r'caiyang\caigou.png'
        self.img_isxinyong = r'caiyang\isxinyong.png'
        self.img_xinyong = r'caiyang\xinyong.png'
        self.img_sqxy = r'caiyang\sqxy.png'
        self.img_5 = r'caiyang\5.png'
        self.img_mylz = r'caiyang\mylz.png'
        self.img_lizhi = r'caiyang\lizhi.png'
        self.img_hwys = r'caiyang\hwys.png'
        self.img_wzcb = r'caiyang\wzcb.png'
        self.img_keyao = r'caiyang\keyao.png'
        self.img_isjz = r'caiyang\isjz.png'
        self.img_jj1 = r'caiyang\jj1.png'
        self.img_qbsh = r'caiyang\qbsh.png'
        self.img_qbjf = r'caiyang\qbjf.png'
        self.img_end = r'caiyang\end.png'
        self.img_end2 = r'caiyang\end2.png'
        self.img_jjtc = r'caiyang\jjtc.png'
        self.img_sxsz = r'caiyang\sxsz.png'
        self.img_1 = r'caiyang\1.png'
        self.img_isrw = r'caiyang\isrw.png'
        self.img_qdky = r'caiyang\qdky.png'

    @staticmethod
    def cao_zuo(pic):
        start_time = time.time()
        finished = False

        while not finished:
            try:
                locations = pag.locateOnScreen(pic)
                # print(locations)
                if locations is not None:
                    pag.moveTo(locations, duration=0.5)
                    pag.click()
                    finished = True
                    time.sleep(1)
            except:
                break
            if time.time()-start_time > 2:
                break

    @staticmethod
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except WindowsError:
            return False

    @staticmethod
    def panduan(pic):
        if pag.locateOnScreen(pic) is not None:
            return True
        else:
            return False

    def start(self):
        if self.is_admin():
            # 需要管理员权限执行的操作
            self.app = application.Application(backend="uia")
            self.app.start(
                r"D:\明日方舟\emulator\nemu\EmulatorShell\NemuLauncher.exe -p com.hypergryph.arknights")
        else:
            # 判断版本是否为python3
            if sys.version_info[0] == 3:
                # 获取管理员权限再次运行
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        while True:
            if self.panduan(self.img_start):
                self.cao_zuo(self.img_start)
                print('开始游戏')
                break
            time.sleep(5)
        while True:
            if self.panduan(self.img_huanxing):
                self.cao_zuo(self.img_huanxing)
                print('唤醒')
                break
            time.sleep(5)

    def guan_bi(self, pic):
        for num in range(2):
            if self.panduan(pic):
                self.cao_zuo(pic)
                pag.moveRel(-200, 0)
                pag.click()
                break
            time.sleep(2)

    def tuichu(self):
        self.cao_zuo(self.img_tuichu)

    def renwu(self):
        if pag.locateOnScreen(self.img_isrenwu):
            self.cao_zuo(self.img_renwu)
            while self.panduan(self.img_isrw):
                self.cao_zuo(self.img_isrw)
                while self.panduan(self.img_lingqu):
                    self.cao_zuo(self.img_lingqu)
                    pag.moveRel(-200, 0)
                    pag.click()
                    print('已成功领取任务奖励！')
                    time.sleep(1)
            # self.cao_zuo(self.img_richang)
            # while self.panduan(self.img_lingqu):
            #     self.cao_zuo(self.img_lingqu)
            #     pag.moveRel(-200, 0)
            #     pag.click()
            #     print('已成功领取任务奖励！')
            #     time.sleep(1)
        else:
            print('无可领取，或未在桌面')

    def xingdong(self):
        if not self.panduan(self.img_isdaili):
            self.cao_zuo(self.img_daili)
        self.cao_zuo(self.img_ksxd)
        if self.panduan(self.img_keyao):
            self.cao_zuo(self.img_qdky)
            time.sleep(2)
        elif self.panduan(self.img_mylz):
            self.cao_zuo(self.img_lizhi)
            time.sleep(2)
            pass
        time.sleep(2)
        self.cao_zuo(self.img_ksxd2)
        print('开始行动！')

    def zuozhan(self, pic1, pic2, pic3=None):
        self.cao_zuo(self.img_zuozhan)
        self.cao_zuo(pic1)
        self.cao_zuo(pic2)
        if pic3 is not None:
            self.cao_zuo(pic3)

    def xdjs(self, timenum=180):
        x = True
        start_time = time.time()
        while not self.panduan(self.img_xdjs):
            time.sleep(10)
            if time.time()-start_time > timenum:
                x = False
                break
        if x:
            time.sleep(2)
            self.cao_zuo(self.img_xdjs)
        else:
            time.sleep(2)
            pag.click(600, 600)
        print('行动结束！')

    def gkzm(self):
        if self.panduan(self.img_isgkzm):
            self.cao_zuo(self.img_gkzm)
            for pic in [r'caiyang\hxr1.png', r'caiyang\hxr2.png', r'caiyang\hxr3.png']:
                if self.panduan(pic):
                    self.cao_zuo(pic)
                    time.sleep(3)
                    self.cao_zuo(self.img_skip)
                    time.sleep(2)
                    pag.click()
                    time.sleep(1)
            print('已成功完成公开招募！')

    def zm(self):
        while not self.panduan(self.img_zuozhan):
            self.tuichu()
        print('已成功返回桌面！')

    def xingyong(self):
        if self.panduan(self.img_iscaigou):
            print('yes')
            self.cao_zuo(self.img_caigou)
            if self.panduan(self.img_isxinyong):
                self.cao_zuo(self.img_xinyong)
                self.cao_zuo(self.img_sqxy)
                pag.click()
                print('已成功领取信用！')
                time.sleep(1)

    def jj(self):
        if self.panduan(self.img_isjz):
            self.cao_zuo(self.img_isjz)
            self.cao_zuo(self.img_jj1)
            if self.panduan(self.img_qbjf):
                self.cao_zuo(self.img_qbjf)
            if self.panduan(self.img_qbsh):
                self.cao_zuo(self.img_qbsh)
            self.jjtc()

    def jjtc(self):
        self.cao_zuo(self.img_jjtc)

    def end(self):
        self.cao_zuo(self.img_end)
        self.cao_zuo(self.img_end2)
        print('退出游戏')


if __name__ == '__main__':
    pga = playGameAuto()
    # pga.start()
    time.sleep(2)
    # list1 = [pga.img_huodong, pga.img_meiri, pga.img_guanggao]
    # for pic in list1:
    #     pga.guanbi(pic)
    for i in range(3):
        pga.xingdong()
        pga.xdjs()
    pga.end()