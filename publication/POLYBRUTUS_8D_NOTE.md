# Polybrutus 8D — Exact Conservative Lifting and a Weighted-Laplacian Spectral Certificate

**Author:** Gabriel St-Pierre — independent researcher; ORCID: 0009-0009-9297-2336  
**Date:** 20 November 2026; **type:** computational note / exact mathematical dataset (not peer reviewed).  
**Provenance:** [7D baseline DOI 10.5281/zenodo.24407952](https://doi.org/10.5281/zenodo.24407952); [canonical P-geometry](https://github.com/Topbrutus/polybrutus/blob/main/SPECIFICATION.md).  
**Disclosure:** OpenAI ChatGPT (Astra) substantially assisted the exact formulation, symbolic code, verification, drafting and consistency checks. This is AI-assisted computational research led by the human author, not a physical observation or independently peer-reviewed mathematical result.

## Abstract

We give an exact, reproducible one-step extension of the published 12-point Polybrutus 7D labelled Euclidean metric to thirteen points of minimal affine rank eight. All 66 previous labelled distances remain unchanged. The thirteenth point contributes twelve squared distances equal to `2R²`. For `R=1`, the 78 pairs occupy eight exact squared-distance families, with `4d²` histogram `4:6, 7:2, 8:47, 9:3, 10:10, 12:6, 13:2, 16:2`. We present independent exact coordinate and distance-Gram rank certificates, a rational distance-only countercheck, four negative controls, and an exact spectral recursion for a selected *illustrative*, weighted-Laplacian scalar oscillator model. In this model, eigenvalue `13/2` occurs exactly twice. This case is an application of established orthogonal-completion and Laplacian-cone ideas, not a claim of unprecedented mathematical technique or a new physical dimension.

## Construction

Let the original seven Polybrutus points `P_i` lie in `R³`, all of norm `R` (coordinates in the canonical specification). Let `H5={h∈R⁵:Σh_j=0}`, and put `Q_j=(√5/2)(e_j−1/5·1)` for five indices. The twelve points `(P_i,0)` and `(0,Q_j)` lie in `R³⊕H5`, of intrinsic dimension seven, and have exactly the published 7D labelled distances. The new thirteenth point is `S=R·e8` in `R³⊕H5⊕R`, orthogonal to all twelve old vectors. Hence all thirteen points are on a sphere of radius R, and `||S−P_i||²=||S−Q_j||²=2R²`.

For storage, the code uses 9 columns: 3 for `P`, 5 for `H5`, 1 for `S`. The five `H5` columns satisfy one constraint, leaving **eight independent affine dimensions**, not nine.

## Exact metric results

| Quantity | 7D baseline | 8D result |
|---|---:|---:|
| Vertex count | 12 | **13** |
| Labelled unordered pairs | 66 | **78** |
| Affine rank | 7 | **8** |
| Preserved labelled distances | 66 | **66/66** |
| New distances | — | **12**; each `d²=2R²` |
| Families of `k=4d²/R²` | 8 | **8** |
| Squared distance sum, R=1 | 575/4 | **671/4** |

Exact new histogram:

| `k` | 4 | 7 | 8 | 9 | 10 | 12 | 13 | 16 | total |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| multiplicity | 6 | 2 | **47** | 3 | 10 | 6 | 2 | 2 | **78** |

The exact center of mass of the thirteen vectors, in the stored coordinates, is `(0,0,1/26,0,0,0,0,0,1/13)` for `R=1`; this is not the sphere center. Note that neither the center nor the barycentre is counted as an additional vertex.

## Proof of minimum dimension

Let `M` be the exact `13×13` squared-distance matrix and `H=I−(1/13)11ᵀ`. The centered Gram matrix is `B=−(1/2)HMH`. Two methods verify `rank(B)=8`: (a) exact symbolic elimination on the distance-Gram matrix; (b) rank of the coordinate-difference matrix. Because `B=(HX)(HX)ᵀ` in our explicit Euclidean realization, B is positive semidefinite. The rank of the centered Gram matrix is determined uniquely by the **labelled pairwise distances**, proving that no lower-dimensional realization has these distances. This is an exact instance-specific certificate.

## A dimension-specific result for an illustrative oscillator network

Assign all 13 points unit masses and idealized scalar pairwise couplings `w_ij=R²/d²_ij`. For `R=1`, the Laplacian blocks have the new point uniformly connected to each of the 12 old points at weight `1/2`. Let `χ12(z)` be the characteristic polynomial of the 7D model's weighted 12-vertex Laplacian. Direct block decomposition proves:

`χ13(z) = z(z−13/2)·χ12(z−1/2)/(z−1/2)`.

With `f6(z)=χ_P7(z)/z` for the weighted Laplacian on the original seven points, the *exact* identity is

`χ13(z) = z(z−13/2)²(z−6)⁴ f6(z−3)`.

Thus a double eigenvalue `13/2` and four eigenvalues `6` appear. Exact SymPy characteristic-polynomial computations independently confirm this factorization; this double multiplicity is a mathematical feature of the chosen graph model, not proof of an experimental resonance or new physics. The coning operation and spectral shift are established mathematical techniques; we do not claim an original general law.

## Falsification checks, software provenance, and limitations

The first script independently checks 78 rational squared distances, exact Gram positivity and rank, the spectrum, and four error-injection controls. The second script reconstructs the full distance metric using rational arithmetic from the original coordinates and the simplex metric, then compares all 78 labelled pair distances against the first result. Neither input file is an empirical measurement. The tests were executed on 20 November 2026 using SymPy 1.14.0 and Python; machine-readable evidence is included in `results/certificate_d08.json`.

The result concerns affine metric dimension **8**, not an eighth dimension of spacetime; the theoretical spring network is uncalibrated. Further novelty review and human peer review have **not** been completed. This note documents one exact computational case; publication of many near-duplicate dimension steps without independent contributions would not be justified.

## Reproduction and licensing

Run `python src/verify_d08.py` and `python tests/independent_d08.py` with `sympy==1.14.0`. Outputs and the complete labelled distance matrix are in `results/certificate_d08.json`; all code uses MIT. This research note uses CC BY 4.0; cite Gabriel St-Pierre. Related work: [Polybrutus 7D](https://doi.org/10.5281/zenodo.24407952). The author is responsible for interpreting and validating the research; AI assistance is declared above.
