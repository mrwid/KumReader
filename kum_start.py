#__*__ coding:utf-8 __*__

import appuifw
import graphics
import sysinfo
import topwindow
import e32

def ShowStartFrame():
    _screenW , _screenH = sysinfo.display_pixels()  #获取屏幕宽/高
    try:
        try:
            _imgstart = graphics.Image.open(r"C:\python\images\KumReader_start.jpg")
        except SymbianError:
            _imgstart = graphics.Image.open(r"D:\python\images\KumReader_start.jpg")
    except:
        appuifw.note(cn("应用程序已损坏,请重新安装！\nError:401"), "error")
        appuifw.app.set_exit()
        
    screen = topwindow.TopWindow()
    screen.add_image(_imgstart, (0, 0, _screenW, _screenH))
    screen.size = (_screenW, _screenH)
    screen.show()
    e32.ao_sleep(2)
    screen.hide()
        
def cn(self, x):
    return x.decode("utf-8")

if __name__ == '__main__':
	appuifw.app.body = gui =appuifw.Canvas()
	appuifw.app.screen = "full"
	ShowStartFrame()
	