# SPECIFICATION_D08 — labelled Euclidean metric

Scale `R>0`. For computational verification set `R=1`.

## Original P vertices

Use the seven precise `P1..P7` coordinates of [Polybrutus 0.1.0](https://github.com/Topbrutus/polybrutus/blob/main/SPECIFICATION.md):

```
P1 = (0,0,1)
P2 = (sqrt(3)/2,0,1/2)
P3 = (-sqrt(3)/4,3/4,1/2)
P4 = (-sqrt(3)/4,-3/4,1/2)
P5 = (0,0,-1)
P6 = (sqrt(3)/2,0,-1/2)
P7 = (-sqrt(3)/2,0,-1/2)
```

## Orthogonal 4-simplex Q

Let `H5={x∈R^5 : sum(x)=0}` and `u=(1,1,1,1,1)`. For `j=1,…,5` let

`Q_j=(sqrt(5)/2)(e_j-u/5)`.

Embed `P_i` into `R^3⊕H5` as `(P_i,0)` and `Q_j` as `(0,Q_j)`. This is a **7-dimensional** direct sum. All 12 vectors have squared norm 1 and the original labelled 66 pairwise distances.

## D08 new point and explicit ambient embedding

In `V08=R^3⊕H5⊕R` let `S=(0,0,1)` be the unit vector along the last `R` summand. It is orthogonal to all previous vectors. `V08` has dimension `3+4+1=8`.

For simple exact programmatic coordinates, the scripts represent `H5` using five components and store vectors in **nine columns** with one linear constraint. This is a *redundant coordinate storage format*, not nine dimensions.

The 13 labels are `P1..P7, Q1..Q5, S`. Squared lengths: `d(P_i,Q_j)^2=2`, `d(P_i,S)^2=2`, `d(Q_j,S)^2=2`, `d(Q_i,Q_j)^2=5/2` for `i≠j`; original P-P distances are unchanged. Thus `78` labels-pairs, with `k=4d²` histogram `(4:6,7:2,8:47,9:3,10:10,12:6,13:2,16:2)`.

Scaling by R multiplies every squared distance by R².
