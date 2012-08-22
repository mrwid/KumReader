#__*__ coding:utf-8 __*__
#Author: Mr.Wid
#Date: 2012.08.22
#----------------

import kum_start
import appuifw
import graphics
import e32dbm
import sysinfo
import powlite_fm

class KumReader:
    def __init__(self):
        #初始化主程序
        self.CheckSrc()     #检查资源文件
        #kum_start.ShowStartFrame()      #显示软件启动界面
        appuifw.app.screen = 'full'
        appuifw.app.body = self.mainUI = appuifw.Canvas()     #主程序主界面
        self.InitMainFrame()

        
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

    
    #编码处理------------
    def cn(self, x):
        return x.decode('utf-8')

    #事件处理-----------
    def main_redraw(self):
        try:
            self.mainUI.blit(self.MainFrame)
        except:
            pass

    def main_event(self):
        pass

    #文件选择-----------
    def SelectFile(self):
        path = powlite_fm.manager().AskUser('c:/', find = 'file')
        return path

    #初始化主界面------------
    def InitMainFrame(self):
        place = [(int(self.dbBookshelf['T0']), int(self.dbBookshelf['V0'])),
                 (int(self.dbBookshelf['T1']), int(self.dbBookshelf['V0'])),
                 (int(self.dbBookshelf['T2']), int(self.dbBookshelf['V0'])),
                 (int(self.dbBookshelf['T0']), int(self.dbBookshelf['V1'])),
                 (int(self.dbBookshelf['T1']), int(self.dbBookshelf['V1'])),
                 (int(self.dbBookshelf['T2']), int(self.dbBookshelf['V1'])),
                 (int(self.dbBookshelf['T0']), int(self.dbBookshelf['V2'])),
                 (int(self.dbBookshelf['T1']), int(self.dbBookshelf['V2'])),
                 (int(self.dbBookshelf['T2']), int(self.dbBookshelf['V2'])),
            ]
        font = (appuifw.available_fonts()[2], 11)
        for i in range(9):
            self.imgBookShelf.blit(self.imgBook, target = place[i])
            _bookName = self.dbBookshelf[str(i)][19:-4]
            self.imgBookShelf.text(place[i], self.cn(self.dbBookshelf[str(i)][19:]), (40,40,40),font )
        self.mainUI.blit(self.imgBookShelf)

    #显示图像-----------
    def MakeImg(self, style):
        pass
        

def test():
    app = KumReader()

    from e32 import Ao_lock
    lock=Ao_lock()
    appuifw.app.exit_key_handler=lock.signal
    lock.wait()

if __name__ == '__main__':
    test()