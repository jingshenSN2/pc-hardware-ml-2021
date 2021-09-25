import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

sample = pd.read_csv('comment_sample_labeled.csv')

labels = sample['LABEL']
contents = sample['text'].apply(lambda s: s.replace('_', ' '))

# use CountVectorizer
cv_contents = CountVectorizer(input='content', stop_words='english')
dtm = cv_contents.fit_transform(contents)

colnames = cv_contents.get_feature_names()
print(f'The vocab has {len(colnames)} words, and they are: {colnames}\n\n')

# convert to dataframe
content_df = pd.DataFrame(dtm.toarray(), columns=colnames)
content_df.insert(0, 'LABEL', value=labels)
print(content_df.head())
content_df.to_csv('content_sample_labeled.csv', index=False)
