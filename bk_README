# ---------------------------------------------------------------------------
#
# SGD-Transformer
# 
# Created on 2015-12-29 by Ming Chang,
# PhD student of Prof. Xuemei Wang at Sun Yet-sen University
# 
# ---------------------------------------------------------------------------

  This is a program to project your GeoTiff data to WGS1984, 
  reclassify to USGS 24-class and convert your data into 
  the MM5/WRF geogrid binary format.

  The structure of this program is as follow:

  input/ output/ src/ README run_me
  |      |       |
  |      |       |__ gdal_reclassify.py Makefile osgeo/ wpsingest.F write_grogrid.c
  |      |                                       |
  |      |__ The path to find outputs            |__ GDAL Plugins(May not need)
  |
  |__ The path to put your input files

  
  Notes:

  "Csh, Python(with NumPy) and GDAL(with Python bindings)" are required.
  Please check the environment of your computer first!
  
  Before run this program, you need to define something in the head
  of the "run_me" file.

  After the modify work, ./run_me and find result in output/
  
  A file named 00001-<NX>.00001-<NY> is created, where <NX> is the 
  argument nx and <NY> is the argument ny, both in i5.5 format.
  And a index file would created in the same place.

  Creat a new folder under geog path and copy these two output things inside.
  Add the rel_path(the folder name) and interp_option into your 
  WPS/geogrid/GEOGRID.TBL. Then you can calling your modified datasets 
  in your namelist.wps.

  Have fun!

# ---------------------------------------------------------------------------  
#  
#  Suggestions, comments, and corrections are welcome!
#  Please mail to changm3@mail2.sysu.edu.cn.
#
# ---------------------------------------------------------------------------
