# PREUVE_D08 — exact affine dimension and model spectrum

## Statement

The 13 labelled points of `SPECIFICATION_D08.md` have Euclidean affine rank exactly 8. The 78 labelled pairwise squared distances determine minimal Euclidean embedding dimension 8. In particular, no faithful realization in affine dimension 7 exists.

## Affine rank and minimality

All 13 points lie in `V08=R³⊕H5⊕R` of dimension 8. Their exact labelled squared-distance matrix `M` has centered Gram matrix `B = −(1/2) H M H`, `H = I −(1/13)11^T`. Direct symbolic Gaussian elimination gives `rank(B)=8`, independent of the coordinates. As `B=(H X)(H X)^T` for the coordinate matrix `X` of the actual Euclidean realization, it is positive semidefinite. Euclidean distance matrix theory shows every realization with these labelled distances has affine dimension `rank(B)=8`. The coordinate-difference matrix independently has rank 8.

## Exact spectrum

Let `L12` be the 7D weighted graph Laplacian using all edges `w=1/d²`. Add S with constant weight `1/2` to each of 12 old vertices. The resulting `L13` is

```
L13 = [ L12 + (1/2)I12   −(1/2) 1_12 ]
      [ −(1/2)1_12^T           6      ]
```

For each old eigenvector orthogonal to `1`, its eigenvalue increases by `1/2`; the global-constant mode remains 0; the new contrast vector has eigenvalue `13/2`. Thus, if `χ12(z)` is the old Laplacian characteristic polynomial,

`χ13(z) = z (z−13/2) [χ12(z−1/2)/(z−1/2)]`.

The 7D spectrum has `χ12(z)=z(z−6)(z−11/2)^4 f6(z−5/2)`, with `f6(z)=χ_P7(z)/z`. Therefore

`χ13(z) = z (z−13/2)^2 (z−6)^4 f6(z−3)`.

Our exact symbolic calculation verifies this identity and confirms `f6(7/2) ≠ 0`, so eigenvalue `13/2` has multiplicity **exactly 2**. This is a precise result of the selected mathematical oscillator model, **not a physical observation**.

## Counter-tests

1. Perturb one labelled squared distance → histogram mismatch.
2. Duplicate the new vertex from the old group → affine rank drops to 7.
3. Bend S into an old geometric direction, maintaining norm → at least one new cross distance changes.
4. Swap P and Q labels → global histogram unchanged, but labelled canonical P-P distances no longer agree. Therefore histogram alone is insufficient.

## Nonclaims

- No novel universal theorem is asserted; this construction uses known orthogonal completion and Laplacian coning methods.
- No literal eighth physical/spacetime dimension is inferred.
- No Higgs or elementary-particle implication is inferred.
- Independent human scholarly review is still needed.
