import numpy as np
import matplotlib.pyplot as plt

def laplace_solve(N, tol=1e-5):
    # Initialiserer potensialfeltet
    phi = np.zeros((N, N))

    # Randbetingelser 
    phi[:, 0] = 1  # Venstre rand
    phi[:, -1] = 1  # Høyre rand
    phi[0, :] = 0  # Topp rand
    phi[-1, :] = 0  # Bunn rand

    # Start avslapningsmetoden
    diff = tol + 1.0  # Sørger for at løkken starter
    iter = 0
    while diff > tol:
        phi_old = phi.copy()
        # Oppdater potensialfeltet bortsett fra ved grensene
        for i in range(1, N-1):
            for j in range(1, N-1):
                phi[i, j] = 0.25 * (phi_old[i+1, j] + phi_old[i-1, j] + phi_old[i, j+1] + phi_old[i, j-1])
        
        # Beregn maksimal forskjell fra den gamle konfigurasjonen
        diff = np.max(np.abs(phi - phi_old))
        iter += 1

    print(f"Konvergerte etter {iter} iterasjoner")
    return phi

# Sett rutenettstørrelse
N = 100
phi = laplace_solve(N)

# Plotting
plt.imshow(phi, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Løsning til Laplace-ligningen')
plt.show()

