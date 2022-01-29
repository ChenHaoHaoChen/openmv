#注意：本程序识别色块函数返回code有问题，无论什么颜色，总是返回2！！！

import sensor,time,image #引入sensor,time,image模块

sensor.reset()                     #重置感光元件
sensor.set_pixformat(sensor.RGB565)#设置照片格式为RGB565
sensor.set_framesize(sensor.QQVGA) #设置图像大小为QQVGA
sensor.set_auto_gain(False)        #颜色识别需关闭自动增益
sensor.set_auto_whitebal(False)    #颜色识别需关闭白平衡
sensor.skip_frames()               #跳过300ms内帧数

clock = time.clock()          #构造时钟对象
templates = ["/0.pgm","1.pgm"]#匹配模块位置字符串
thresholds = [(30, 100, 15, 127, 15, 127),
              (30, 100, -64, -8, -32, 32)] #红色,绿色阈值
while(True):
    clock.tick()           #开始追踪运行时间
    img = sensor.snapshot()#拍摄一张照片
    #调用find_blobs函数寻找面积大于200，像素点大于200的色块
    for blob in img.find_blobs(thresholds,are_threshold = 200,
                               pixels_threshold = 200):
        img = img.to_grayscale() #图像转换为灰度图
        #调用模块匹配函数，对模块进行匹配
        for template in templates:
            rect = img.find_template(image.Image(template),0.7,
                                     step = 4,search = image.SEARCH_EX)
            if rect:
                img.draw_rectangle(rect)   #用矩形框框出匹配成功模块
                print(blob.code(),template)#打印对应颜色索引和模块对应字符串
    img.draw_string(0,0,"fps:%0.1f"%clock.fps())#在图像上打印当前帧率
