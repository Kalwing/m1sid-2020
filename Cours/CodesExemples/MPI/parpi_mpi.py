from mpi4py import MPI
import numpy as np
import time
def picks(n):
    count_inside=0
    for i in range(n):
        x,y=np.random.random(2)*2-1
        if x*x+y*y <=1: count_inside+=1
    return count_inside

def compute_pi(n):
    return 4*picks(n)/n

def par_picks(n):
  comm=MPI.COMM_WORLD
  rank=comm.Get_rank()
  size=comm.Get_size()
  nlocal=int(n/size)
  localcount=picks(nlocal)
  count=localcount
  if rank!=0:
     comm.send(localcount,dest=0)
  if rank==0:
     for irank in range(1,size):
        rcount=comm.recv(source=irank)
        count+=rcount
  return count

def par_compute_pi(n):
    return 4*par_picks(n)/n


for n in range(1,1000000,100000):
  t0=time.time()
  pmcpi=par_compute_pi(n)
  t1=time.time()
  print(n,pmcpi,abs(pmcpi-np.pi)/np.pi,t1-t0)
