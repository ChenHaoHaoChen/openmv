import sensor,time,image #引入sensor,time,image模块

sensor.reset()                      #重置感光元件
sensor.set_pixformat(sensor.RGB565) #设置照片格式为RGB565
sensor.set_framesize(sensor.QVGA)   #设置图像大小为QVGA
sensor.set_auto_gain(False)         #颜色识别必须关闭自动增益
sensor.set_auto_whitebal(False)     #颜色识别必须关闭白平衡
sensor.skip_frames()                #跳过0.3s内帧数
clock_1 = time.clock()              #构造时钟对象
thresholds = [(30, 100, 15, 127, 15, 127),
              (30, 100, -64, -8, -32, 32),
              (68, 15, -5, 30, -75, -31)] #红色,绿色,蓝色阈值
ROI = [0,0,320,240]  #感兴趣区

#下位完整参数版
#while(True):
#    clock_1.tick()
#    img = sensor.snapshot()
#    for blob_n in img.find_blobs(thresholds,roi = ROI,x_stride = 2,y_stride = 1,are_threshold = 400,pixels_threshold = 400,merge = False,margin = 0):
#        img.draw_rectangle(blob_n.rect(),color = (255,0,0))
#        img.draw_cross(blob_n.cx(),blob_n.cy(),size = 5,color = (0,255,0))
#    print(clock_1.fps())


#为了方便,不常用参数可不设置

#单颜色识别
while(True):
    clock_1.tick()          #开始追踪运行时间
    img = sensor.snapshot() #拍摄一张照片
    #使用find_blobs函数，并遍历图像中阈值为红色,面积大于200,像素大于200的色块
    for blob_n in img.find_blobs([thresholds[0]],are_threshold = 200,pixels_threshold = 200):
        img.draw_rectangle(blob_n.rect())      #画框,框出色块
        img.draw_cross(blob_n.cx(),blob_n.cy())#画十字,十字中心为框中心
        print(blob_n.code())
    print(clock_1.fps()) #打印当前帧率

#多颜色识别
while(True):
    clock_1.tick()          #开始追踪运行时间
    img = sensor.snapshot() #拍摄一张照片
    #使用find_blobs函数，并遍历图像中阈值为红色、绿色、蓝色,面积大于200,像素大于200的色块,merge=True意为合并所有颜色阈值为一个
    for blob_n in img.find_blobs(thresholds,are_threshold = 200,pixels_threshold = 200,merge = True):
        img.draw_rectangle(blob_n.rect())      #画框,框出色块
        img.draw_cross(blob_n.cx(),blob_n.cy())#画十字,十字中心为框中心
        print(blob_n.code())
    print(clock_1.fps()) #打印当前帧率
