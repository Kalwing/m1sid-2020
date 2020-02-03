import numpy as np

def init_grid(n):
  # for parallel issues fix the same seed on each process 
  np.random.seed(0)
  grid = np.random.randint(2,size=(n,n))
  return grid

# obsolete
def evolution1(grid):
    irange=grid.shape[0]
    jrange=grid.shape[1]
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

# obsolete
def get_nbneigh(grid,coord):
    irange=grid.shape[0]
    jrange=grid.shape[1]
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


# obsolete
def evolution1_corr(grid):
    irange=grid.shape[0]
    jrange=grid.shape[1]
    res_grid=[[] for i in range(irange)]
    for j in range(jrange):
        for i in range(irange):
            # by default cell_state is dead
            cell_state=0
            # loop over neighs to count living cells
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
            # if 2 neighbors cell state isn't modified
            if nb_neigh==2:
                cell_state=grid[i][j]
            # if 3 neighbors cell state is alive
            elif nb_neigh==3:
                cell_state=1
            # in other case cell state is dead (default state)
            res_grid[i].append(cell_state)
    return res_grid

# obsolete
def evolution1_ndarray(grid):
    irange=grid.shape[0]
    jrange=grid.shape[1]
    res_grid=np.zeros((irange,jrange))
    for i in range(irange):
        for j in range(jrange):
            # by default cell_state is dead
            cell_state=0
            # loop over neighs to count living cells
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
            # if 2 neighbors cell state isn't modified
            if nb_neigh==2:
                cell_state=grid[i][j]
            # if 3 neighbors cell state is alive
            elif nb_neigh==3:
                cell_state=1
            # in other case cell state is dead (default state)
            res_grid[i,j]=cell_state
    return res_grid

#obsolete
def evolution2(grid):
    irange=grid.shape[0]
    jrange=grid.shape[1]
    res_grid=np.zeros((irange,jrange))
    for i in range(irange):
        for j in range(jrange):
            # by default cell_state is dead
            cell_state=0
            # loop over neighs to count living cells
            biinf=max(0,i-1)
            bisup=min(irange-1,i+1)
            bjinf=max(0,j-1)
            bjsup=min(jrange-1,j+1)
            nb_neigh=0
            # loop over neighs to count living cells
            for ii in range(biinf,bisup+1):
                for jj in range(bjinf,bjsup+1):
                    if grid[ii,jj] == 1:
                        nb_neigh=nb_neigh+1
            # in my count I count current cell itself substract the value
            nb_neigh=nb_neigh-grid[i,j]
            # if 2 neighbors cell state isn't modified
            if nb_neigh==2:
                cell_state=grid[i,j]
            # if 3 neighbors cell state is alive
            elif nb_neigh==3:
                cell_state=1
            # in other case cell state is dead (default state)
            res_grid[i,j]=cell_state
    return res_grid

def enlarge_grid(grid):
    xdim,ydim = grid.shape
    res_grid = np.zeros((xdim + 2,ydim + 2))
    res_grid[1:xdim + 1,1:ydim + 1] = grid[:,:]
    return res_grid

#obsolete
def evolution_eg(grid):
    # grid is an enlarge grid
    xdim = grid.shape[0]
    ydim = grid.shape[1]
    res_grid = np.zeros((xdim,ydim))
    # we start from 1 to xdim-1
    for i in range(1,xdim - 1):
        for j in range(1,ydim - 1):
            # by default cell_state is dead
            cell_state = 0
            # loop over neighs to count living cells
            nb_neigh = 0
            # loop over neighs to count living cells
            for ii in [i - 1,i,i + 1]:
                for jj in [j - 1,j,j + 1]:
                    if grid[ii,jj] == 1:
                        nb_neigh = nb_neigh + 1
            # in my count I count current cell itself substract the value
            nb_neigh = nb_neigh - grid[i,j]
            # if 2 neighbors cell state isn't modified
            if nb_neigh == 2:
                cell_state = grid[i,j]
            # if 3 neighbors cell state is alive
            elif nb_neigh == 3:
                cell_state = 1
            # in other case cell state is dead (default state)
            res_grid[i,j] = cell_state
    return res_grid

#obsolete
def evolution_unroll(grid):
    xdim = grid.shape[0]
    ydim = grid.shape[1]
    res_grid = np.zeros((xdim,ydim))
    for i in range(1,xdim - 1):
        for j in range(1,ydim - 1):
            nb_neigh = grid[i - 1,j - 1] + grid[i - 1,j] + grid[i - 1,j + 1] \
                     + grid[i,j - 1]     + grid[ i,j + 1] \
                     + grid[i + 1,j - 1] + grid[i + 1,j] + grid[i + 1,j + 1]  
            if nb_neigh == 2:
                res_grid[i,j] = grid[i,j]
            elif nb_neigh == 3:
                res_grid[i,j] = 1
    return res_grid

def evolution_store(grid):
    idim,jdim= grid.shape
    res_grid = np.zeros((idim,jdim))
    for i in range(1,idim-1):
        #specific case j=1 for initial storage values
        store0 = 0 # because store0=grid[i-1,0]+grid[i,0]+grid[i+1,0] all zeros
        store1 = grid[i - 1,1] + grid[i,1] + grid[i + 1,1] # j=1
        store2 = grid[i - 1,2] + grid[i,2] + grid[i + 1,2] # j+1=2
        nb_neigh = store0 + store1 + store2 - grid[i,1] # substract the element (i,j)
        if nb_neigh == 2:
            res_grid[i,1] = grid[i,1]
        elif nb_neigh == 3:
            res_grid[i,1] = 1
        # loop on j (we begin with j=2)
        for j in range(2,jdim - 1):
            # switch the storage values
            store0 = store1
            store1 = store2
            #compute the 3rd storage value
            store2 = grid[i - 1,j + 1] + grid[i,j + 1] + grid[i + 1,j + 1]   # 3rd subcolumn
            # compute nb_neigh
            nb_neigh = store0 + store1 + store2 - grid[i,j] # substract the element (i,j)
            if nb_neigh == 2:
                res_grid[i,j] = grid[i,j]
            elif nb_neigh == 3:
                res_grid[i,j] = 1
    return res_grid

def statalive(egrid):
    irange,jrange = egrid.shape
    if irange - 2 <= 0 or jrange - 2 <=0:
        return 0,0
    else:
        nalive = np.count_nonzero(egrid[1:irange - 1,1:jrange - 1])
        return nalive,100 * nalive / ((irange - 2) * (jrange - 2))

def gamelife(grid,n):
    egrid = jdv.enlarge_grid(grid)
    for iter in range(n):
        egrid = jdv.evolution_store(egrid)
        nalive,percent = statalive(egrid)
        print("{0} cellules vivantes soit {1:.2f} %".format(nalive,percent))
