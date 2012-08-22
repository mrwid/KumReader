KumReader项目进度描述
=====================

#启动界面#
*启动界面已完成，kum_start.py，调用为: kum_start.ShowStartFrame()

#主程序#
*主程序的资源文件检测方法CheckSrc()已完成,当资源文件缺失时弹出警告并自动退出程序;

*事件响应与处理框架已完成,可在main_redraw和main_event方法中将其完善

*编码处理cn函数,将x处理成utf-8编码已完成

*文件选择功能已完成,SelectFile(),返回选择的文件的路径

*主界面的初始化InitMainFrame()完成从书架信息数据库中读取书籍坐标与路径功能,在主界面显示混乱问题待完善

*显示图像素材预留方法MakeImg(self, style)待完善,此方法目的是将不同的素材按照style参数组装成不同的窗口,为双缓冲绘图做准备


#进度描述#
*请参阅FunctionIntroduction.md

Author: Mr.Wid

ver: 0.1.20120822.1835