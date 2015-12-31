from osgeo import gdal
import numpy
import math
import sys

# This is a python script to reclassify the data. 
# Need supplied by GDAL and numPy.

def reclassify(source,output):
    src_ds = gdal.Open(source)
    data = src_ds.ReadAsArray(0,0,src_ds.RasterXSize,src_ds.RasterYSize)
    driver = gdal.GetDriverByName("GTiff")
    dst_ds = driver.CreateCopy(output, src_ds, 0 , [ 'COMPRESS=LZW' ])
    for i,row in enumerate(data):
        for j,column in enumerate(row):
            data[i,j]=nclass(data[i,j])

    dst_ds.GetRasterBand(1).WriteArray(data)
    dst_ds.SetProjection(src_ds.GetProjection())
    dst_ds.SetGeoTransform(src_ds.GetGeoTransform())

    driver = None
    dst_ds = None
    src_ds = None

#This just returns the new class.
def nclass(oldclass):
    newclass=[0]*45
    newclass[1]=1
    newclass[2]=1
    newclass[3]=1
    newclass[4]=1
    newclass[5]=1
    newclass[6]=1
    newclass[7]=1
    newclass[8]=1
    newclass[9]=1
    newclass[10]=1
    newclass[11]=1
    newclass[12]=2
    newclass[13]=3
    newclass[14]=3
    newclass[15]=6
    newclass[16]=6
    newclass[17]=6
    newclass[18]=2
    newclass[19]=6
    newclass[20]=6
    newclass[21]=6
    newclass[22]=6
    newclass[23]=11
    newclass[24]=14
    newclass[25]=15
    newclass[26]=7
    newclass[27]=9
    newclass[28]=9
    newclass[29]=9
    newclass[30]=19
    newclass[31]=19
    newclass[32]=19
    newclass[33]=19
    newclass[34]=24
    newclass[35]=17
    newclass[36]=17
    newclass[37]=17
    newclass[38]=17
    newclass[39]=17
    newclass[40]=16
    newclass[41]=16
    newclass[42]=16
    newclass[43]=16
    newclass[44]=16
    return newclass[oldclass]

if len(sys.argv)==3:
      reclassify(sys.argv[1],sys.argv[2])
