#__*__ coding:utf-8 __*__

import appuifw
import graphics
import sysinfo

class NoStartImg(Exception):
    pass

class Start:
    def __init__(self):
        appuifw.app.body = self.gui =appuifw.Canvas()
        appuifw.app.screen = "full"
        self._screenW , self._screenH = sysinfo.display_pixels()  #获取屏幕宽/高

        try:
            self.ShowStartFrame()
        except NoStartImg:
			appuifw.note(self.cn("应用程序已损坏,请重新安装！\nError:401"), "error")
			appuifw.app.set_exit()

    def ShowStartFrame(self):
		try:
			try:
				_imgstart = graphics.Image.open(r"C:\python\images\KumReader_start.jpg")
				self.gui.blit(_imgstart)
			except SymbianError:
				_imgstart = graphics.Image.open(r"D:\python\images\KumReader_start.jpg")
				self.gui.blit(_imgstart)
		except:
			raise NoStartImg
        
    def cn(self, x):
        return x.decode("utf-8")

def test():
	AppStart = Start()
	
	from e32 import Ao_lock
	lock=Ao_lock()
	appuifw.app.exit_key_handler=lock.signal
	lock.wait()

if __name__ == '__main__':
	test()