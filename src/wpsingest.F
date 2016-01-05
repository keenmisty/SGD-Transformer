program geogrid_change_data
implicit none

integer :: i,j
integer :: isigned, endian, wordsize
integer :: nx, ny, nz
real :: scalefactor
real*8 :: xllcorner, yllcorner, cellsize, missvalue
character :: head12
real, allocatable :: rarray(:,:), iarray(:,:)

isigned = 0
endian = 0
wordsize = 1
scalefactor = 1.0
nz = 1


! read in the ascii new landuse data
open (10, file = 'asciidata.asc')

!read in the header
read(10,*) head12, nx
read(10,*) head12, ny
read(10,*) head12, xllcorner
read(10,*) head12, yllcorner
read(10,*) head12, cellsize
read(10,*) head12, missvalue

allocate(rarray(nx,ny))
allocate(iarray(nx,ny))

!read in the data
do j = 1,ny
read(10,*) iarray(:,j)
end do

! reverse the data so that it begins at the lower-left corner
do j = 1,ny
rarray(:,j) = iarray(:,ny-(j-1))
enddo

!set the missing values
do j = 1, ny
do i = 1, nx
if ( rarray(i,j) < 0 ) then
rarray(i,j) = -99 ! set negative terrain to be zero since those are near
!coastal or river 
!banks
end if
end do
end do


call write_geogrid(rarray, nx, ny, nz, isigned, endian, scalefactor, wordsize)

end program

