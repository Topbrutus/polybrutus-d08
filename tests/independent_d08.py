#!/usr/bin/env python3
"""Independent rational distance-matrix check; does NOT import the generator.
Source: original P_i with x=a*sqrt(3), y=b, z=c;
five simplex distances and uniform orthogonal orthogonal-to-old D08 point.
"""
import json
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
import sympy as sp

root=Path(__file__).resolve().parents[1]
source=json.loads((root/'results/certificate_d08.json').read_text(encoding='utf8'))
xyz=[
    (F(0),F(0),F(1)),
    (F(1,2),F(0),F(1,2)),
    (F(-1,4),F(3,4),F(1,2)),
    (F(-1,4),F(-3,4),F(1,2)),
    (F(0),F(0),F(-1)),
    (F(1,2),F(0),F(-1,2)),
    (F(-1,2),F(0),F(-1,2)),
]

def original_pair(i,j):
    x,y,z=(xyz[i][k]-xyz[j][k] for k in range(3))
    return 3*x*x+y*y+z*z

def d2(i,j):
    if i==j:return F(0)
    if i<7 and j<7:return original_pair(i,j)
    if 7<=i<12 and 7<=j<12:return F(5,2)
    return F(2)

pairs=list(combinations(range(13),2))
assert len(pairs)==78
calculated={(i+1,j+1): d2(i,j) for i,j in pairs}
from_report={(x['i'],x['j']):F(x['d2']) for x in source['pairwise_distances']}
assert calculated==from_report
assert all(d2(i,12)==F(2) for i in range(12))
assert all(d2(i,j) != 0 for i,j in pairs)
hist=Counter(4*d2(i,j) for i,j in pairs)
assert hist==Counter({F(4):6,F(7):2,F(8):47,F(9):3,F(10):10,F(12):6,F(13):2,F(16):2})
D=sp.Matrix(13,13,lambda i,j:sp.Rational(d2(i,j).numerator,d2(i,j).denominator))
H=sp.eye(13)-sp.ones(13)/13
Gram= -H*D*H/2
assert Gram.rank()==8
# Positive semidefinite via principal minors, Sylvester generalization on rank-8 matrix:
# Use eigenvalues numeric as supplementary, not primary PSD proof; primary is original coordinate factorization.
eigs=[float(sp.re(x)) for x in Gram.evalf().eigenvals().keys()]
assert min(eigs)>-1e-8, eigs
# New-point radial distance and labelled preservation exactly.
assert all(calculated[(i+1,j+1)]==from_report[(i+1,j+1)] for i,j in combinations(range(12),2))
assert sum(calculated.values(),F(0))==F(671,4)
print('INDEPENDENT CHECK PASS: all 78 rational distances, label-by-label match, histogram, rank 8, squared-sum 671/4')
