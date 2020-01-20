from mpi4py import MPI
# COMM_WORLD is the default communicator
my_rank = MPI.COMM_WORLD.rank
# each communicator have a size ie the total number of processes
nbprocs = MPI.COMM_WORLD.size
print("Greetings from process ",my_rank," amongst ",nbprocs," processes") 
