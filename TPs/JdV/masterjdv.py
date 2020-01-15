import numpy as np
def init_grid(n):
  grid = np.random.randint(2,size=(n,n))
  return grid

def get_nbneigh(grid,coord):
    irange=len(grid)
    jrange=len(grid[0])
    i=coord[0]
    j=coord[1]
    biinf=max(0,i-1)
    bisup=min(irange-1,i+1)
    bjinf=max(0,j-1)
    bjsup=min(jrange-1,j+1)
    nb_neigh=0
    # loop over neighs to count living cells
    for ii in range(biinf,bisup+1):
        for jj in range(bjinf,bjsup+1):
            if grid[ii][jj] == 1:
                nb_neigh=nb_neigh+1
    # in my count I count current cell itself substract the value
    nb_neigh=nb_neigh-grid[i][j]
    return nb_neigh

def evolution1(grid):
    irange=len(grid)
    jrange=len(grid[0])
    res_grid=[[] for i in range(irange)]
    for j in range(jrange):
        for i in range(irange):
            # by default cell_state is dead
            cell_state=0
            # loop over neighs to count living cells
            nb_neigh=get_nbneigh(grid,(i,j))
            # if 2 neighbors cell state isn't modified
            if nb_neigh==2:
                cell_state=grid[i][j]
            # if 3 neighbors cell state is alive
            elif nb_neigh==3:
                cell_state=1
            # in other case cell state is dead (default state)
            res_grid[i].append(cell_state)
    return res_grid

