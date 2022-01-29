import sensor,time,image #引入sensor,time,image模块

sensor.reset() #重置感光元件
sensor.set_pixformat(sensor.GRAYSCALE) #设置照片格式为GRAYSCALE即灰度
sensor.set_framesize(sensor.QQVGA)#设置图像大小为QQVGA,模板匹配使用QQVGA，若使用QVGA内存可能会爆
sensor.skip_frames()                   #不设置参数，默认跳过300ms内帧数

template_1 = image.Image("/template_1.pgm") #模板1“陈”
template_2 = image.Image("/template_2.pgm") #模板2“浩”

clock_1 = time.clock() #构造时钟对象

while(True):
    clock_1.tick()          #开始追踪时钟运行时间
    img = sensor.snapshot() #拍摄一张照片

    #调用模块匹配函数,匹配模块1,阈值为0.6,跳过像素步数为5,使用SEARCH_EX算法;返回参数为模块的(x,y,w,h)
    rect_1 = img.find_template(template_1,0.7,step = 4,search = image.SEARCH_EX)
    if rect_1:
        img.draw_rectangle(rect_1) #用框框出模块1
    #同时匹配模块2
    rect_2 = img.find_template(template_2,0.7,step = 4,search = image.SEARCH_EX)
    if rect_2:
        img.draw_rectangle(rect_2)

    print(clock_1.fps()) #打印当前帧数
