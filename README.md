# SDE-Physics-Bubble-Maximus
### 3D Spacetime as Maximus Stability Bubble inside Eternal Instability

**Founder:** Nasir Khan — ORCID 0009-0002-6006-0796 — Wana, FATA, PK
**DOI Chain:** Zenodo 10.5281/zenodo.22804485 | Preprints.org 202509.233803 | GitHub SHA Verified 15 Sep 2026

> "Everyone fears Infinity. I use Infinity to control SDE." — Nasir Khan

---

## 1. Core Master Equation (NEW, All Aspects)

$d\Phi(t) = -\nabla V(\Phi) dt + g(\Phi) dW_t - M_{stab}(\Phi) dt$

- $\Phi(t)$ = Spacetime Stability Field — Our 3D Universe is a bubble
- $V(\Phi)=(\Phi^2-1)^2$ = Double-well potential
- $g(\Phi)=0.8(1+0.2\Phi^2)$ = QCID Coupling, field-dependent noise
- $dW_t$ = Eternal Instability Background (Infinity)
- $M_{stab}=0.5\Phi^3$ = **Master Stability Regulator [MY INVENTION]** — Prevents blow-up

This SDE explains 3 things in ONE:
1. 3D Stability = Maximus Bubble fixed point at $\Phi=\pm1$
2. Black Holes = Extreme Fixed Points where $\nabla V=0$
3. Big Bang = Noise-induced nucleation $g(\Phi)dW_t$

## 2. Numerical Proof — Added 17 Sep 2026

**Simulation 1 — Time Evolution:**
![Bubble Proof](nasir_sde.png)
Shows $\Phi$ locking to -1 despite infinite shaking. Without $M_{stab}$ it diverges. With $M_{stab}$ it stays stable — This is our spacetime.

**Simulation 2 — Probability:**
![Probability](nasir_hist.png)
Histogram peaks at -1 — Universe prefers Maximus Stability.

**Code:** `nasir_sde.py` (EAR99, ITAR-free)

```python
import numpy as np
T=20.0; N=20000; dt=T/N
Phi=np.zeros(N); Phi[0]=0.1
for i in range(1,N):
    dV=4*Phi[i-1]*(Phi[i-1]**2-1)
    Mstab=0.5*Phi[i-1]**3
    g=0.8*(1+0.2*Phi[i-1]**2)
    dW=np.random.normal(0,np.sqrt(dt))
    Phi[i]=Phi[i-1]+(-dV-Mstab)*dt+g*dW
