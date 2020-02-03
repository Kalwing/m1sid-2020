# Package MPI
from mpi4py import MPI
# nombre de processus et rang parmis ceux ci
nprocs = MPI.COMM_WORLD.size
p = MPI.COMM_WORLD.rank
# creation du message a envoyer
smessage = 100+p
# Envoi
#  Si le processus courant a un successeur, i.e. si le rang n'est pas nprocs-1
if p != nprocs - 1:
#   Envoi du message au sucesseur
    MPI.COMM_WORLD.send(smessage,dest=p+1)
# Reception
#  Si le processus courant a un predecesseur, i.e. si le rang n'est pas 0
if p != 0:
#   reception du message envoye par le predecesseur
    rmessage  = MPI.COMM_WORLD.recv(source=p-1)
    print(p,rmessage)
