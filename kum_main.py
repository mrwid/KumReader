#__*__ coding:utf-8 __*__
#Author: Mr.Wid
#Date: 2012.08.22
#----------------

import appuifw
import graphics
import e32dbm
import sysinfo
import kum_start

class KumReader:
    def __init__(self):
        #初始化主程序
        app = kum_start.Start()
        del app
        
        self.CheckSrc()     #检查资源文件
        appuifw.body = appuifw.Canvas()
        self.MainFrame = self.CreateFrame()     #创建主界面画布
        self.ReadFrame = self.CreateFrame()     #创建阅读界面画图
        appuifw.body = self.mainUI = appuifw.Canvas(self.main_redraw, self.main_event)     #主程序主界面
        self.readUI = appuifw.Canvas(self.read_redraw, self.read_event)     #阅读界面

    #检查资源文件-----------
    def CheckSrc(self):
        try:
            try:    #尝试从C盘读取
                #检查图像资源文件-----------
                self.imgStart = graphics.Image.open(r'c:\python\images\KumReader_Start.JPG')    #启动画面
                self.imgBookShelf = graphics.Image.open(r'c:\python\images\KumReader_Bookshelf.JPG')    #书架
                self.imgMainMenu = graphics.Image.open(r'c:\python\images\KumReader_MainMenu.png')      #主菜单
                self.imgBook = graphics.Image.open(r'c:\python\images\KumReader_book.png')      #书籍封面
                self.imgBgGray = graphics.Image.open(r'c:\python\images\bg_Gray.JPG')       #灰色纹理图
                self.imgBgGreen = graphics.Image.open(r'c:\python\images\bg_Green.JPG')     #绿色纹理图
                self.imgBgYellow = graphics.Image.open(r'c:\python\images\bg_Yellow.JPG')   #黄色纹理图

                #检查配置文件----------
                self.dbSetting = e32dbm.open(r'c:\python\UserSettings.e32dbm', 'w')     #软件配置文件
                self.dbBookshelf = e32dbm.open(r'c:\python\Bookshelf.e32dbm', 'w')       #书架书籍信息

            except:     #尝试从D盘读取

                #检查图像资源文件-----------
                self.imgStart = graphics.Image.open(r'd:\python\images\KumReader_Start.JPG')
                self.imgBookShelf = graphics.Image.open(r'd:\python\images\KumReader_Bookshelf.JPG')
                self.imgMainMenu = graphics.Image.open(r'd:\python\images\KumReader_MainMenu.png')
                self.imgBook = graphics.Image.open(r'd:\python\images\KumReader_book.png')
                self.imgBgGray = graphics.Image.open(r'd:\python\images\bg_Gray.JPG')
                self.imgBgGreen = graphics.Image.open(r'd:\python\images\bg_Green.JPG')
                self.imgBgYellow = graphics.Image.open(r'd:\python\images\bg_Yellow.JPG')

                #检查配置文件----------
                self.dbSetting = e32dbm.open(r'd:\python\UserSettings.e32dbm', 'w')
                self.dbBookshelf = e32dbm.open(r'd:\python\Bookshelf.e32dbm', 'w')

        except:
            appuifw.note(self.cn('应用程序已损坏,请重新安装!'), 'error')
            appuifw.app.set_exit()

    #创建画布-------------
    def CreateFrame(self):
        appuifw.app.screen = "full"
        _w, _h = sysinfo.display_pixels()
        return graphics.Image.new(size = (_w, _h), mode = 'L')
    
    #编码处理------------
    def cn(self, x):
        return x.decode('utf-8')

    #事件处理-----------
    #----主界面事件处理----
    def main_redraw(self):
        try:
            self.mainUI.blit(self.MainFrame)
        except:
            pass

    def main_event(self):
        pass

    #----阅读界面事件处理----
    def read_redraw(self):
        try:
            self.mainUI.blit(self.ReadFrame)
        except:
            pass

    def read_event(self):
        pass


def test():
    app = KumReader()

    from e32 import Ao_lock
    lock=Ao_lock()
    appuifw.app.exit_key_handler=lock.signal
    lock.wait()

if __name__ == '__main__':
    test()