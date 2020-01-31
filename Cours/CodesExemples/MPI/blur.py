from mpi4py import MPI
import numpy as np

def get_description(file):
    """
    Read the header part of the file
    
    And leave the file at the end of header (start of values)
    """
    # return to begining
    file.seek(0)
    nline=0
    description={}
    while nline <3:
        line=file.readline()
        if line[0]== '#':
            continue
        nline+=1
        if nline == 1:
            description['format']=line.strip()
        elif nline == 2:
            description['dimension']=int(line.split()[1]),int(line.split()[0])
        elif nline ==3:
            description['deep']=int(line.strip())
    return description
        
def read_values(file, description):
    """
    Read all the values directly
    """
    # pre-allocate the array
    nx,ny = description['dimension']
    values = np.empty((nx*ny))
    i = 0
    for line in file:
        if line[0]== '#':
            continue
        vals = line.split()
        nvals = len(vals)
        values[i:i+nvals] = [int(v) for v in vals]
        i += nvals
    return values.reshape((nx,ny))

def read_file(filename):
    """
    Read an image in the PGM format and return a ndarray (2D)
    """
    # open the file once
    with open(filename,'r',encoding="utf-8") as file:

        # read the header part
        description = get_description(file)

        # read the values
        values = read_values(file,description)
    return values

def compute_wtf(neighbors):
    return np.average(neighbors)


filename='test.pgm'
# First read the domain
image=read_file(filename)
# Get global dimension
xdim,ydim=np.shape(image)
# compute local dimension
lxdim=xdim//2
lydim=ydim//2
# Define repartition
ULC=0 # Upper Left Corner
URC=1 # Upper Right Corner
LLC=2 # Lower Left Corner
LRC=3 # Lower Right Corner
# Compute each initial corner
rank=MPI.COMM_WORLD.rank
if rank == ULC:
    xcorner,ycorner=0,0
if rank == URC:
    xcorner,ycorner=0,lydim
if rank == LLC:
    xcorner,ycorner=lxdim,0
if rank == LRC:
    xcorner,ycorner=lxdim,lydim
# create the storage for local image
local_image=np.zeros((lxdim+2,lydim+2))
# put the partial impage in the local storage (for convenience from 1 to ldim instead from 0 to ldim-1)yy
local_image[1:lxdim+1,1:lydim+1]=image[xcorner:xcorner+lxdim,ycorner:ycorner+lydim]
# define interface (I) and ghost (G) region for left(L)/right(R) top(T)/bottom(B) 
# right frontier
IR,GR=lydim,lydim+1
# left frontier
IL,GL=1,0
# bottom frontier
IB,GB=lxdim,lxdim+1
# top frontier
IT,GT=1,0
# for convenience we use buffer for send/receive data
nlocal=max(lxdim,lydim)
sbuffer=np.ones(nlocal+2)
rbuffer=np.ones(nlocal+2)
print("local image for rank:",rank," before\n",local_image)
# Upper Left Corner exchange with Upper Right Corner and Lower Left Corner
if rank == ULC:
   #send IR to URC
   sbuffer[0:lxdim+2]=local_image[:,IR]
   MPI.COMM_WORLD.Send([sbuffer, MPI.INT], dest=URC)
   #receive GR from URC
   MPI.COMM_WORLD.Recv([rbuffer, MPI.INT], source=URC)
   local_image[:,GR]=rbuffer[0:lxdim+2]

   #send IB to LLC
   sbuffer[0:lydim+2]=local_image[IB,:]
   MPI.COMM_WORLD.Send([sbuffer, MPI.INT], dest=LLC)
   #reveive GB from LLC
   MPI.COMM_WORLD.Recv([rbuffer, MPI.INT], source=LLC)
   local_image[GB,:]=rbuffer[0:lydim+2]
# Upper Right Corner exchange with Upper Left Corner and Lower Right Corner
if rank == URC:
   #send IL to ULC
   sbuffer[0:lxdim+2]=local_image[:,IL]
   MPI.COMM_WORLD.Send([sbuffer, MPI.INT], dest=ULC)
   #receive GL from ULC
   MPI.COMM_WORLD.Recv([rbuffer, MPI.INT], source=ULC)
   local_image[:,GL]=rbuffer[0:lxdim+2]

   #send IB to LRC
   sbuffer[0:lydim+2]=local_image[IB,:]
   MPI.COMM_WORLD.Send([sbuffer, MPI.INT], dest=LRC)
   #reveive GB from LRC
   MPI.COMM_WORLD.Recv([rbuffer, MPI.INT], source=LRC)
   local_image[GB,:]=rbuffer[0:lydim+2]
# Lower Left Corner exchange with Upper Left Corner and Lower Right Corner
if rank == LLC:
   # receive GT from ULC
   MPI.COMM_WORLD.Recv([rbuffer, MPI.INT], source=ULC)
   local_image[GT,:]=rbuffer[0:lydim+2]
   # send IT to ULC
   sbuffer[0:lydim+2]=local_image[IT,:]
   MPI.COMM_WORLD.Send([sbuffer, MPI.INT], dest=ULC)

   # send IR to LRC
   sbuffer[0:lxdim+2]=local_image[:,IR]
   MPI.COMM_WORLD.Send([sbuffer, MPI.INT], dest=LRC)
   # receive GR from LRC
   MPI.COMM_WORLD.Recv([rbuffer, MPI.INT], source=LRC)
   local_image[:,GR]=rbuffer[0:lxdim+2]

# Lower Right Corner exchange with Upper Right Corner and Lower Left Corner
if rank == LRC:
   #receive GT from URC
   MPI.COMM_WORLD.Recv([rbuffer, MPI.INT], source=URC)
   local_image[GT,:]=rbuffer[0:lydim+2]
   #send IL to LLC
   sbuffer[0:lxdim+2]=local_image[:,IL]
   MPI.COMM_WORLD.Send([sbuffer, MPI.INT], dest=LLC)
   #send IT to URC
   sbuffer[0:lydim+2]=local_image[IT,:]
   MPI.COMM_WORLD.Send([sbuffer, MPI.INT], dest=URC)
   #receive GL from LLC
   MPI.COMM_WORLD.Recv([rbuffer, MPI.INT], source=LLC)
   local_image[:,GL]=rbuffer[0:lxdim+2]
print("local image for rank:",rank," after\n",local_image)
