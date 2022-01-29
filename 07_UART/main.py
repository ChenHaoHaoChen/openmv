from pyb import UART,delay #从pyb模块中引入UART,delay
uart_3 = UART(3,9600) #配置UART3波特率为9600
uart_1 = UART(1,9600) #配置UART1波特率为9600
while(True):          #仅有UART1和UART3可配置
    uart_3.write("Hello World!") #UART3发送字符串
    delay(1000)
