#打印99乘法表
 for x in range(1,10):
     for y in range(1,x+1):
         print("%d*%d=%d"%(y,x,y*x),end="|")
     print("")#换行，注意print前后的位置
