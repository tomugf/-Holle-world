#_*_coding:utf-8_*_
import datetime
import copy
def dealleft(first,final,lis,temp):
    #temp用来标记位于凸包上的点
    max=0
    index=-1
    #处理first到final的上方，得到使first，final，i 三点组成的三角形面积最大的点i
    if first<final:
        for i in range(first,final):
            #获得first，final，i 的坐标
            firstcoordinate=lis[first]
            finalcoordinate=lis[final]
            icoordinate=lis[i]
            firstx=firstcoordinate[0]
            firsty = firstcoordinate[1]
            finalx=finalcoordinate[0]
            finaly = finalcoordinate[1]
            ix=icoordinate[0]
            iy = icoordinate[1]
            #计算first，final，i 三点组成的三角形面积
            triangle_area=firstx * finaly + ix * firsty + finalx * iy - ix * finaly - finalx * firsty - firstx * iy
            if triangle_area>max:
                max=triangle_area
                index=i
    # 处理first到final的下方，得到使first，final，i 三点组成的三角形面积最大的点i
    else:
        for i in range(final,first):
            firstcoordinate = lis[first]
            finalcoordinate = lis[final]
            icoordinate = lis[i]
            firstx = firstcoordinate[0]
            firsty = firstcoordinate[1]
            finalx = finalcoordinate[0]
            finaly = finalcoordinate[1]
            ix = icoordinate[0]
            iy = icoordinate[1]
            triangle_area = firstx * finaly + ix * firsty + finalx * iy - ix * finaly - finalx * firsty - firstx * iy
            if triangle_area > max:
                max = triangle_area
                index = i

    if index!=-1:
        temp[index]=1
        dealleft(first,index,lis,temp)
        dealleft(index,final,lis,temp)


def divide(lis,n):
    starttime = datetime.datetime.now()
    # temp用来标记位于凸包上的点
    temp = {}
    # lis_con_new为凸包集合
    lis_con_new = []
    if n==3:
        return  lis
    for i in range(n):
        temp[i]=0
    lis_con=copy.deepcopy(lis)
    lis_con.sort()
    temp[0]=1
    temp[n-1]=1
    dealleft(0,n-1,lis_con,temp)
    dealleft(n-1,0,lis_con,temp)
    for i in temp:
        if temp[i]==1:
            lis_con_new.append(lis_con[i])
    endtime = datetime.datetime.now()
    print ("分治时间---",(endtime - starttime))
    return  lis_con_new