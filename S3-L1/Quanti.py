
import matplotlib.pyplot as plt

# Definizione dei processi con le rispettive fasi
processes = {
    'P1': [(0, 1, 'active'),(4, 5, 'active') , (7, 8, 'active'),(9, 10, 'active'),(11, 12, 'active')],
    'P2': [(1, 2, 'active'), (5, 6, 'active')],
    'P3': [(2, 3, 'active')],
    'P4': [(3, 4, 'active'), (6, 7, 'active'),(8, 9, 'active'),(10, 11, 'active')]
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