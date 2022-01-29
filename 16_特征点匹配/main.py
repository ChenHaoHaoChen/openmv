import sensor,time,image #引入sensor,time,image模块

sensor.reset()                        #重置感光元件
sensor.set_pixformat(sensor.GRAYSCALE)#设置照片格式为灰度图
sensor.set_framesize(sensor.QVGA)     #设置图像大小为QVGA
sensor.skip_frames(time = 1000)       #跳过1s内不稳定帧数

clock_1 = time.clock()#构造时钟对象
keypoint_1 = None     #原匹配对象关键点
#画出关键点
def draw_keypoints(img,keypoint):
    if keypoint:
        print(keypoint)             #打印出原匹配对象关键点参数
        img.draw_keypoints(keypoint)#画出原匹配对象关键点
        img = sensor.snapshot()     #拍摄一张照片
        time.sleep_ms(2000)         #延时2s
#主程序
while(True):
    clock_1.tick()         #构造始终对象
    img = sensor.snapshot()#拍摄一张照片
    if keypoint_1 == None:
        #采集原匹配对象关键点
        keypoint_1 = img.find_keypoints(max_keypoints = 150,threshold = 10,scale_factor = 1.2)
        draw_keypoints(img,keypoint_1)
    else:
        #采集现匹配对象关键点
        keypoint_2 = img.find_keypoints(max_keypoints = 150,threshold = 10,scale_factor = 1.2,normalized = True)
        if keypoint_2:
            #原匹配对象与现匹配对象关键点进行匹配
            match = image.match_descriptor(keypoint_1,keypoint_2)
            if match.count() >= 10:
                    img.draw_rectangle(match.rect())     #用框框出现匹配对象
                    img.draw_cross(match.cx(),match.cy())#在现匹配对象中央用十字点出
            print(match.count(),match.theta())    #输出现匹配对象匹配关键点数以及旋转角度
    img.draw_string(0,0,"fps:%0.2f"%clock_1.fps())#在图像上显示当前帧率
