import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

dane = np.sort([186, 176, 158, 180, 186, 168, 168, 164, 178, 170, 189, 195, 172,
                187, 180, 186, 185, 168, 179, 178, 183, 179, 170, 175, 186, 159,
                161, 178, 175, 185, 175, 162, 173, 172, 177, 175, 172, 177, 180])


fit = stats.norm.pdf(dane, np.mean(dane), np.std(dane))
# np.mean(dane) -> mean of dane, np.std(dane) -> standard deviation
line_at_max = np.linspace(np.min(fit), np.max(fit), 10)
means = []
for i in range(0, len(line_at_max)):
    means.append(np.mean(dane))
size = 14

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.title(r'$ f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp{-\frac{(x-\mu)^2}{2\sigma^2}} $', fontsize=size - 1)
plt.xlabel(r'$x$', fontsize=size)
plt.ylabel(r'$f(x)$', fontsize=size)
plt.plot(dane, fit, '-o')
plt.plot(means, line_at_max, lw=2)
plt.savefig('Gauss')
plt.show()
