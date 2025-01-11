import matplotlib.pyplot as plt
import pandas as pd
data = {
    "Dimension": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    "NSM": [
        0.07999015415159418, 0.0787309643529303, 0.07804871461526289,
        0.07508713974934818, 0.07430264741139186, 0.07279921474131537,
        0.071515482860545, 0.07175299895100253, 0.07073172598960507,
        0.07072163088170468, 0.07023652894732062, 0.06985919656710579,
        0.07020088271739072, 0.06768563246474235, 0.0654087080403189
    ]
}

bounds_data = {
    "Dimension": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    "lower bound": [
        0.080187537, 0.077874985, 0.07608708, 0.074654327, 0.073474906, 0.072483503,
        0.071636064, 0.070901661, 0.070257874, 0.069688002, 0.069179323, 0.068721956,
        0.068308096, 0.067931488, 0.067587055
    ],
    "upper bound": [
        0.080267223, 0.079723711, 0.078822518, 0.078731261, 0.077779975, 0.076858058,
        0.075654034, 0.075552237, 0.074856027, 0.074026177, 0.073098569, 0.072400247,
        0.071672217, 0.071008692, 0.070399705
    ]
}

# 创建 DataFrame
df = pd.DataFrame(data)
df_bounds=pd.DataFrame(bounds_data)

# 绘制
plt.scatter(df['Dimension'], df['NSM'],color='blue',label='NSM Data',marker='o')
plt.plot(df_bounds['Dimension'],df_bounds['lower bound'],color='red',linestyle='--',label='Lower bound')
plt.plot(df_bounds['Dimension'],df_bounds['upper bound'],color='red',linestyle='--',label='Upper bound')

plt.title('n-Dimension Lattice NSM and Bounds Comparsion')
plt.xlabel('Dimension')
plt.ylabel('Value')


plt.legend()
plt.grid(True)
plt.show()

fix, ax=plt.subplots(figsize=(4,4))
ax.axis('tight')
ax.axis('off')
table=ax.table(cellText=df.values,colLabels=df.columns,loc='center')
for (i,j),cell in table.get_celld().items():
    cell.set_text_props(ha='center',va='center')

plt.show()
