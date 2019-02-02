"""
Hardy-Cross method
Bruce Wernick
10 October 2017 15:38:10
"""

def sign(a):
  if a<0: return -1
  return 1

def max_error(mesh):
  e=0.0
  for m in mesh:
    if abs(m[1])>e:
      e=abs(m[1])
  return e

def flows(edge):
  s=''
  for i in range(1,len(edge)):
    s+='%8.4f'%(edge[i][1])
  return s

def edge_dp(edge):
  'process edges (2r|q| and rq^2)'
  for e in edge:
    r=e[0] # resistance
    q=e[1] # flow
    rq=r*abs(q) # resistance x flow
    e[2]=2.0*rq # slope
    e[3]=rq*q # dp = r|q|q
  return edge

def mesh_dp(edge,mesh):
  'process meshes'
  for m in mesh:
    m[0]=0.0
    m[1]=m[3] # assign fixed gain
    for e in m[4]:
      i=abs(e) # edge index
      sgn=sign(e)
      m[0]+=edge[i][2] # sum(slope)
      m[1]+=sgn*edge[i][3] # sum(sign*dp)
  return mesh

def mesh_dq(mesh):
  'calculate the mesh correction'
  for m in mesh:
    m[2]=-m[1]/m[0] # -sum(dp)/2sum(rq)
  return mesh

def edge_flow(edge,mesh):
  'update the edge flows (se = signed edge)'
  for m in mesh:
    dm=m[2]
    for se in m[4]:
      i=abs(se)
      sgn=sign(se)
      edge[i][1]+=sgn*dm # sign*dq
  return edge


# ------------------------------------------------------------------------------

if __name__=="__main__":

  ## edge list
  ##    r    q   2rq   dp
  e=[[   0,   0,   0,   0],
     [ 3.0, 4.0, 0.0, 0.0],
     [ 4.0, 6.0, 0.0, 0.0],
     [10.0, 1.0, 0.0, 0.0],
     [15.0, 1.0, 0.0, 0.0],
     [2.0, 3.0, 0.0, 0.0],
     [6.0, 2.0, 0.0, 0.0],
     [ 5.0, 5.0, 0.0, 0.0]]

  ##    ---o
  ##      / \
  ##     1   2
  ##    /     \
  ##   o-3-o-4-o
  ##    \  |  /
  ##     5 6 7
  ##      \|/
  ##    ---o

  ## mesh list (created manually)
  ##  2rq   dp  dq  gain  [(edge,dir)...]
  m=[[0.0, 0.0, 0.0, 0.0, [-1,2,4,-3]],
     [0.0, 0.0, 0.0, 0.0, [3,6,-5]],
     [0.0, 0.0, 0.0, 0.0, [-4,7,-6]]]

  ## graph defined by [inode,onode,edge] triple
  #g=[(1,2,1),(1,4,2),(2,3,3),(4,3,4),(2,5,5),(3,5,6),(4,5,7)]
  ## graph defined by adjacency list
  #g=[(1,1,2),(2,1,3,5),(3,2,4,5),(4,1,3,5),(5,2,3,4)]

  i=0
  while 1:
    e = edge_dp(e)
    m = mesh_dp(e,m)
    m = mesh_dq(m)
    e = edge_flow(e,m)
    print('%4d %s'%(i,flows(e)), end=' ')
    mx = max_error(m)
    print('%0.4f'%mx, end=' ')
    print()
    if mx < 1.0e-3:break
    i += 1
    if i > 100:break
