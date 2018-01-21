#! usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots()
ax.axis("equal")
ax.pie([24, 18],
        labels = ["Femmes", "Hommes"],
        autopct="%1.1f pourcents")
plt.title("Un superbe graphique")
plt.show()

