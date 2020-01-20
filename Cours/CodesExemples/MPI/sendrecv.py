from mpi4py import MPI
my_rank = MPI.COMM_WORLD.rank
message=-1
if my_rank==0:
   message=1
print("message before exchange for rank ",my_rank,": ",message)
# process 0 send a message to process 1
if my_rank==0:
   MPI.COMM_WORLD.send(message,dest=1)
# process 1 recev a message from process 0
if my_rank==1:
   message=MPI.COMM_WORLD.recv(source=0)
print("message after exchange for rank ",my_rank,": ",message)
