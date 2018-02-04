import seaborn as sns
%matplotlib inline

matrix = [[] for x in languages]
for i, lang1 in enumerate(languages):
    for lang2 in languages:
        matrix[i].append(score(corpus[i], lang2))
matrix = pd.DataFrame(matrix, columns=languages)
sns.set(rc={'figure.figsize':(14,9)})
sns.heatmap(matrix, center=100, yticklabels=languages)
