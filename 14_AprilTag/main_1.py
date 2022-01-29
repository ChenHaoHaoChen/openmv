import sensor,time,image #引入sensor,time模块

sensor.reset() #重置感光元件
sensor.set_pixformat(sensor.RGB565)#设置照片格式为RGB565
sensor.set_framesize(sensor.QQVGA) #设置图像大小为QQVGA(160*120),若设置为QVGA(320*240)很卡
sensor.skip_frames(time = 1000)    #跳过1秒内不稳定帧数

#设置以像素为单位的相机x方向的焦距，2.8为镜头焦距，3.984为感光元件的长，160为图像长度=img.width()
f_x = (2.8/3.984)*160
#设置以像素为单位的相机y方向的焦距，2.8为镜头焦距，2.952为感光元件的宽，120为图像长度=img.height()
f_y = (2.8/2.952)*120
#图像的x中心位置 = img.width()/2
c_x = 160/2
#图像的y中心位置 = img.height()/2
c_y = 120/2

clock_1 = time.clock() #构造时钟对象

#弧度转换为角度函数
def angle(radian):
    return radian*180/3.14

while(True):
    clock_1.tick() #开始追踪运行时间
    img = sensor.snapshot() #拍摄一张照片
    #使用find_apriltags函数对图像进行找寻AprilTag
    for apriltags in img.find_apriltags(fx = f_x,fy = f_y,cx = c_x,cy = c_y):
        img.draw_rectangle(apriltags.rect(),color = (255,0,0)) #用红色框框出AprilTag
        img.draw_cross(apriltags.cx(),apriltags.cy(),color = (0,255,0)) #用绿色十字标出AprilTag标签中心
        values = [apriltags.x_translation(),    #返回AprilTag空间中x方向坐标
                  apriltags.y_translation(),    #返回AprilTag空间中y方向坐标
                  apriltags.z_translation(),    #返回AprilTag空间中z方向坐标
                  angle(apriltags.x_rotation()),#返回AprilTag空间中x方向旋转角度
                  angle(apriltags.y_rotation()),#返回AprilTag空间中y方向旋转角度
                  angle(apriltags.z_rotation())]#返回AprilTag空间中z方向旋转角度
        print(values)
    print(clock_1.fps()) #停止追踪运行时间并返回当前帧数
