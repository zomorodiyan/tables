# define variables
label = ['c1','c2','c3','c4']
in_ =  [['a','x',1,2],\
        ['b','x',3,4],\
        ['c','x',5,6]]
desired_out = [['x','a','c3',1],\
        ['x','a','c4',2],\
        ['x','b','c3',3],\
        ['x','b','c4',4],\
        ['x','c','c3',5],\
        ['x','c','c4',6]]

# generate output
out = []
for row in in_:
  for i in range(2,4): # {2,3}: indexes of {c3,c4}
    out.append([row[1],row[0],label[i],row[i]])

# assert output is right
for i in range(len(out)):
  for j in range(len(out[0])):
    assert(out[i][j]==desired_out[i][j])

