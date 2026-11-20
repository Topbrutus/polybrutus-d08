# Polybrutus 8D — exact conservative one-step lifting

## Official public release

- **Zenodo DOI:** [10.5281/zenodo.24408344](https://doi.org/10.5281/zenodo.24408344) (verified public record).
- **Archived source tag:** [`v0.1.0`](https://github.com/Topbrutus/polybrutus-d08/tree/v0.1.0), commit `356973b71ec14aa5881a8e26edd375efdb84f0af`.
- **Zenodo files:** two-page scientific note PDF, exact certificate JSON for 78 pairs, GitHub tag source archive.
- **GitHub Actions:** [`Verify D08 certificate`](https://github.com/Topbrutus/polybrutus-d08/actions/workflows/verify.yml), run `44836421518`: success.
- **Scope:** exact mathematical model and illustrative spectrum; neither a new dimension of physical spacetime nor a claim of priority for the orthogonal-join construction.


**Gabriel St-Pierre**, independent researcher  
**Status:** 8D exact computational certificate; geometry is a mathematical model, not an eighth physical dimension.  
**AI assistance:** OpenAI ChatGPT (Astra) substantially assisted construction, mathematical checking, source code, tests, documentation, and drafting. Scientific peer review has not occurred.

## Results checked with two independently implemented programs

- Preserve the seven canonical points and five regular-simplex vertices of the published **Polybrutus 7D** configuration [DOI:10.5281/zenodo.24407952](https://doi.org/10.5281/zenodo.24407952), without moving any of them.
- Add one unit vector in a new direction orthogonal to the original 7D linear subspace.
- **13 unit-radius vertices, 78 unordered pairs, 8-dimensional affine span** and 8 exact squared-distance families.
- **66/66 labelled distances retained**; the new vertex contributes **12 distances with square equal to 2**.
- Complete normalized histogram (`k=4d²/R²`): `{4:6,7:2,8:47,9:3,10:10,12:6,13:2,16:2}`.
- **Exact affine-rank certificate:** independent coordinate-difference and centered squared-distance Gram computations give rank 8. The Gram matrix is exactly positive semidefinite by the factorization `G = (H X)(H X)^T`.
- **One-step oscillator model result:** the illustrative all-to-all weighted graph with edge weights `w_ij=R²/d²_ij` has an exact double eigenvalue `13/2`; no physical experiment is claimed.

The main research note is [`publication/POLYBRUTUS_8D_NOTE.md`](publication/POLYBRUTUS_8D_NOTE.md). Reproduce:

```sh
python -m pip install sympy==1.14.0
python src/verify_d08.py
python tests/independent_d08.py
```

All computations default to `R=1`; general `R>0` is obtained by multiplying all coordinates by `R`, preserving the dimension and normalized histogram.

## Scientific limits

This example is an **instance of a standard orthogonal extension/cone operation** and is not claimed to establish a new general theorem. The dimension refers to the minimal affine embedding of **labelled Euclidean distances**, not the physical dimension of spacetime. The oscillator law is a selected ideal model, not data or evidence of new particles. Whether this dimension-specific data merits a separate scientific deposit is an editorial question. The title intentionally does not claim novelty.

## Provenance

- Canonical seven-point definition: https://github.com/Topbrutus/polybrutus/blob/main/SPECIFICATION.md
- Prior 7D exact certificate: https://doi.org/10.5281/zenodo.24407952
- Owner and research program: Gabriel St-Pierre (Topbrutus)
- Reproduction scripts: MIT license (`LICENSE`); research note: CC BY 4.0, credited to Gabriel St-Pierre. 

No private conversation archives or authentication materials belong in this repository.
