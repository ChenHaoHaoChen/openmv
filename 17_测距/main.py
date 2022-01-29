import sensor,time,image #引入sensor,time,image模块

sensor.reset()                     #重置感光元件
sensor.set_pixformat(sensor.RGB565)#设置照片格式为RGB565
sensor.set_framesize(sensor.QVGA)  #设置图像大小为QVGA
sensor.skip_frames()               #跳过0.3s内帧数
clock_1 = time.clock()             #构造时钟对象

red_threshold = (30, 80, 15, 50, -5, 20)#红色阈值

k = 20*62 #测距比例系数k = 距离 * 像素数
#求k方法，让色块在距openmv的20cm处测量其宽度的像素(blob_n.w())为62
while(True):
    clock_1.tick()         #开始追踪运行时间
    img = sensor.snapshot()#拍摄一张照片
    #用find_blobs函数找寻红色色块，且色块面积和像素应大于200
    for blob_n in img.find_blobs([red_threshold],are_threshold = 200,pixels_threshold = 200):
        img.draw_rectangle(blob_n.rect())      #用矩形框框出色块
        img.draw_cross(blob_n.cx(),blob_n.cy())#在色块中心画十字
        length = k / blob_n.w()#由比例系数k求得色块距openmv长度
    print(clock_1.fps(),length)#打印当前帧率和长度
