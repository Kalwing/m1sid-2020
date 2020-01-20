from mpi4py import MPI
import numpy as np
my_rank = MPI.COMM_WORLD.rank
if my_rank==0:
   sendarray=np.random.rand(10)
   print("message before exchange for rank ",my_rank,": ",sendarray)
# process 0 send a numpy array to process 1
   MPI.COMM_WORLD.send(sendarray,dest=1)
# process 1 recev a message from process 0
if my_rank==1:
   recvarray=MPI.COMM_WORLD.recv(source=0)
   print("message after exchange for rank ",my_rank,": ",recvarray)
