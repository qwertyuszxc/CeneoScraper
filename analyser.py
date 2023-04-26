import os
import pandas as pd
from matplotlib import pyplot as plt

print(*[filename.split('.')[0]for filename in os.listdir('./opinions')], sep = '\n')

product_code = input('Dodaj kod produktu: ')

opinions = pd.read_json(f"./opinions/{product_code}.json")
#opinions.score = opinions.score.map(lambda x: float(x[:-2].replace(',','.')))
opinions.score = opinions.score.map(lambda x: float(x.split('/')[0].replace(',','.')))

opinions_count = len(opinions.index)
opinions_count = opinions.shape[0]
#pros_count = sum([False if len(p) == 0 else True for p in opinions.pros])
#cons_count = sum([False if len(c) == 0 else True for c in opinions.cons])
#pros_count = opinions.pros.map(lambda p: False if len(p) == 0 else True).sum()
#cons_count = opinions.cons.map(lambda c: False if len(c) == 0 else True).sum()
pros_count = opinions.pros.map(bool).sum()
cons_count = opinions.cons.map(bool).sum()
avg_score = opinions.score.map(lambda x: float(x.split('/')[0].replace(',','.')))
print(f'''Dla produktu o kodzie {product_code} destępnych jest {opinions_count} opinii,
Dla {pros_count} opinii dostępna jest liczna zalet,
a dla {cons_count} dostępna liczba wad.
Średnia ocena pproduktu to {avg_score}
''')

score = opinions.score.value_counts().reindex(list(np.arange(0,5.5,0.5))), fill_value = 0 
print(score)
score.plot.bar(color = 'hotpink')
plt.title('Histogram ocen')
plt.xlabel('Liczba gwiazdek')
plt.ylabel('Liczba opinii')
plt.xticks(rotation = 0)
for index, value in enumerate(score):
    plt.text(index, value+0.5, str(value), ha='center')
#plt.show()
try:
    os.mkdir('/opinions')
except FileExistsError:
    pass
plt.savefig(f'./plots/{product_code}')
plt.close()

recommendation = opinions['recommendation'].value_counts(dropna= False).sort_index()
print(recommendation)

recommendation.plot.pie(
label='',
autopct ="",
lables = ['Nie polecam', 'Polecam', 'Nie mam zdania'],
colors = ['crimson', 'forestgreen', 'Gray']
)

plt.legend(bbox_to_anchor=(0.5,0.5))
plt.savefig(f'./plots/{product_code}_recommendation.png')
plt.show()