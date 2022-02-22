####sudoku_generator--right fill the random number and remove some of it to generator
#%%
#general generator for sudoku as and cube[3x3]--9*9 to cube [n*n]--n^2*n^2
#define the cube, begin with n, the size of the sudoku is n^2 
# sample(range(a),k)  choose the random k elements from a population
from random import sample
#'''inital the cube var'''
cube = 3
line = cube*cube


# p = range(3)
# print(sample(range(100),10))
# # sample()
# #sample(p,len(p))

base  = 3
side  = base*base

# pattern for a baseline valid solution
print (pattern(r,c): return (base*(r%base)+r//base+c)%side)

# randomize rows, columns and numbers (of valid base pattern)
from random import sample
def shuffle(s): return sample(s,len(s)) 
rBase = range(base) 
rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
print(cols)
# %%
