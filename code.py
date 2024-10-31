import seaborn as sns
import matplotlib.pyplot as plt

# Data for chromosome sizes and number of genes for B. nigra
chromosome_sizes_bnigra = [54731903, 73743414, 59024541, 51417425, 67898307, 61872432, 59877746, 71984002]
num_genes_bnigra = [131, 293, 230, 237, 237, 154, 128, 203]

# Data for chromosome sizes and number of genes for S. arvensis
chromosome_sizes_sarvensis = [46408851, 43419538, 37284882, 47784266, 52171196, 49852727, 49153139, 42090328, 36737036]
num_genes_sarvensis = [129, 222, 147, 182, 236, 220, 162, 174, 150]

# Data for chromosome sizes and number of genes for S. alba
chromosome_sizes_salba = [57158731, 31689451, 31007024, 32852875, 28507362, 38871341, 29247975, 32512709, 44420566, 28290049, 30853752, 30697166]
num_genes_salba = [86, 108, 101, 128, 94, 111, 107, 90, 124, 108, 89, 100]

# Genome sizes and total RGA counts for each species
genome_sizes = [515, 450, 436]  # in MB
rga_counts = [1625, 1625, 1249]  # total RGA counts for each species
species = ['B. nigra', 'S. arvensis', 'S. alba']

# Create a 2x2 figure for four subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Plot for B. nigra
sns.regplot(x=chromosome_sizes_bnigra, y=num_genes_bnigra, scatter_kws={'s': 100}, color='blue', ax=axes[0, 0])
axes[0, 0].set_xlabel('Chromosome size')
axes[0, 0].set_ylabel('Number of RGAs')
axes[0, 0].set_title('B. nigra', fontstyle='italic')

# Plot for S. arvensis
sns.regplot(x=chromosome_sizes_sarvensis, y=num_genes_sarvensis, scatter_kws={'s': 100}, color='blue', ax=axes[0, 1])
axes[0, 1].set_xlabel('Chromosome size')
axes[0, 1].set_ylabel('Number of RGAs')
axes[0, 1].set_title('S. arvensis', fontstyle='italic')

# Plot for S. alba
sns.regplot(x=chromosome_sizes_salba, y=num_genes_salba, scatter_kws={'s': 100}, color='blue', ax=axes[1, 0])
axes[1, 0].set_xlabel('Chromosome size')
axes[1, 0].set_ylabel('Number of RGAs')
axes[1, 0].set_title('S. alba', fontstyle='italic')

# Plot for genome size vs. RGA count with regression line and legend
sns.scatterplot(x=genome_sizes, y=rga_counts, hue=species, palette='viridis', s=100, ax=axes[1, 1])
sns.regplot(x=genome_sizes, y=rga_counts, scatter=False, color='red', ax=axes[1, 1])
axes[1, 1].set_xlabel('Genome Size (MB)')
axes[1, 1].set_ylabel('Total RGA count')
axes[1, 1].set_title('RGA Count vs Genome Size')
axes[1, 1].legend(title='Species')
axes[1, 1].set_ylim(1200, 2000)  # Set y-axis limit
# Add a common title for the entire figure
# fig.suptitle('Relationship between chromosome and genome size with RGA numbers', fontsize=16)

# Show the plot
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout and space for title
plt.show()
