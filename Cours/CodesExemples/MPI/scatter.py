from mpi4py import MPI
import numpy as np
rank=MPI.COMM_WORLD.rank
nbproc=MPI.COMM_WORLD.size
if rank==0:
   a=np.random.rand(nbproc)
   print("before scatter:",a)
   b=MPI.COMM_WORLD.scatter(a,0)
else:
   b=MPI.COMM_WORLD.scatter(None,0)
print("after scatter:",b)
