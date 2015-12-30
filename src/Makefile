.SUFFIXES:
.SUFFIXES:	.o .c .F

OBJS=	write_geogrid.o

CMDS=	write.exe

RM=	rm -f

CC=	gcc
F90=	gfortran
CFLAGS= -D_UNDERSCORE -DBYTESWAP -DLINUX -DIO_NETCDF-DIO_BINARY -DIO_GRIB1  -D_GEOGRID -O
FFLAGS=	-ffree-form -ffree-line-length-none

all:	$(CMDS)

write.exe:$(OBJS)
	$(F90) $(FFLAGS) wpsingest.F $(OBJS)
.c.o:
	$(CC) $(CFLAGS) -c $(<)
clean:
	$(RM) $(OBJS) $(CMDS) *.mod *~ *.o
