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
    newclass=[0]*25
    newclass[1]=1
    newclass[2]=2
    newclass[3]=3
    newclass[4]=4
    newclass[5]=5
    newclass[6]=6
    newclass[7]=7
    newclass[8]=8
    newclass[9]=9
    newclass[10]=10
    newclass[11]=11
    newclass[12]=12
    newclass[13]=13
    newclass[14]=14
    newclass[15]=15
    newclass[16]=16
    newclass[17]=17
    newclass[18]=18
    newclass[19]=19
    newclass[20]=20
    newclass[21]=21
    newclass[22]=22
    newclass[23]=23
    newclass[24]=24
    return newclass[oldclass]

if len(sys.argv)==3:
      reclassify(sys.argv[1],sys.argv[2])
