import seaborn as sns
%matplotlib inline

matrix = []
for i, lang1 in enumerate(languages):
    matrix.append(scoresV2(corpus[i])[1].tolist()[0])
matrix = pd.DataFrame(np.array(matrix), columns=languages)
sns.set(rc={'figure.figsize':(20,12)})
sns.set(font_scale=2)
matrix=(matrix-matrix.mean())/matrix.std()
sns.heatmap(matrix, center=1.5, yticklabels=languages, cmap="viridis_r")
