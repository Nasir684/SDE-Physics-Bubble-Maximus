"""

Theorem 1.2: Scaling Law and Critical Exponent in SDE Bubble Maximus
Extension of Theorem 1.1: Infinite Instability and Finite-Time Blow-Up
Mathematical Infinity as Physical Light at 10^4K

Author: Nasir Khan
Independent Researcher, Wana, South Waziristan (Ex-FATA),
Khyber Pakhtunkhwa, Pakistan
ORCID: 0009-0002-6006-0796
Email: nasirk684@gmail.com
GitHub: Nasir684/SDE-Physics-Bubble-Maximus
Zenodo DOI: 10.5281/zenodo.22731095 (v2)
Preprints DOI: 10.20944/preprints202509.233321.v1
MDPI Manuscript: mmphys-4595483 (Under Review, Modern Mathematical Physics)
MDPI Preprints ID: 233321

Affiliation: Founder, Bubble Maximus Research Group, Wana
Date: 14 September 2026
Version: Theorem 1.2 Draft v1.0

"""
import numpy as np
import matplotlib.pyplot as plt

# ---- Theorem 1.1 SDE Core (Replace with your exact SDE if different) ----
def simulate_bubble(sigma, dt=1e-5, T_max=2.0, R0=1.0):
    """
    SDE: dR = -5.0 * R^3 dt + sigma * R^2 dW
    Finite-time blow-up detection -> Temperature conversion
    """
    N = int(T_max/dt)
    R = R0
    for i in range(N):
        dW = np.sqrt(dt) * np.random.randn()
        drift = -5.0 * R**3
        diff = sigma * R**2
        R_new = R + drift*dt + diff*dW
        if R_new <= 0 or R_new > 1e6 or np.isnan(R_new):
            blow_up_time = i*dt
            temp = 1e4 * (1.0 + sigma**2) / (blow_up_time + 0.01)
            return blow_up_time, temp
        R = R_new
    return T_max, 0.0

# ---- Theorem 1.2: Scaling Law (Bigger Simulation) ----
sigmas = [0.2, 0.5, 1.0, 1.5, 2.0, 3.0]
results = []

print("=== Theorem 1.2 Scaling Simulation Started ===")
print("Author: Nasir Khan, Wana, ORCID 0009-0002-6006-0796")
for sigma in sigmas:
    times = []
    temps = []
    for run in range(20):
        t_blow, T = simulate_bubble(sigma)
        times.append(t_blow)
        temps.append(T)
    avg_time = np.mean(times)
    avg_temp = np.mean(temps)
    results.append((sigma, avg_time, avg_temp))
    print(f"sigma={sigma} -> avg blow-up={avg_time:.4f}s, avg T={avg_temp:.0f}K")

# ---- Plot Fig.1 for Paper 2 ----
sigmas_plot, t_plot, T_plot = zip(*results)
plt.figure(figsize=(8,6))
plt.loglog(sigmas_plot, T_plot, 'o-', linewidth=2, markersize=8)
plt.xlabel('Noise Intensity sigma', fontsize=12)
plt.ylabel('Temperature T (K)', fontsize=12)
plt.title('Theorem 1.2: Scaling Law T ~ sigma^alpha\nBubble Maximus', fontsize=13)
plt.grid(True, which="both", ls="--", alpha=0.6)
plt.savefig('theorem_1_2_scaling.png', dpi=300, bbox_inches='tight')
print("\nSaved: theorem_1_2_scaling.png")

# ---- Critical Exponent Fit ----
coeffs = np.polyfit(np.log(sigmas_plot), np.log(T_plot), 1)
alpha = coeffs[0]
print(f"\n*** THEOREM 1.2 RESULT ***")
print(f"Scaling: T ~ sigma^{alpha:.2f}")
print(f"Critical exponent alpha = {alpha:.2f}")
print(f"DOI: 10.5281/zenodo.22731095")
print(f"MDPI: mmphys-4595483")
