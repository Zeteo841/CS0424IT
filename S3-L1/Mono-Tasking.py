
import matplotlib.pyplot as plt

# Definizione dei processi con le rispettive fasi
processes = {
    'P1': [(0, 3, 'active'), (3, 5, 'pause'), (5, 6, 'active')],
    'P2': [(6, 8, 'active'), (8,9, 'pause')],
    'P3': [(9, 10, 'active')],
    'P4': [(10, 14, 'active'), (14, 15, 'pause')]
}

# Mappatura colori per i tipi di fase
colors = {
    'active': 'yellow',
    'pause': 'green'
}

fig, ax = plt.subplots(figsize=(10, 6))

# Creazione delle barre del diagramma di Gantt
for i, (process, phases) in enumerate(processes.items()):
    for (start, end, phase) in phases:
        ax.barh(process, end - start, left=start, color=colors[phase], edgecolor='black')

# Configurazione dell'asse
ax.set_xlabel('Tempo')
ax.set_ylabel('Processo')
ax.set_xticks(range(16))
ax.grid(True)

# Mostra il grafico
plt.show()