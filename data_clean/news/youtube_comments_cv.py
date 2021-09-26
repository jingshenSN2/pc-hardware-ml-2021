import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC

sample = pd.read_csv('comment_sample_labeled.csv')
all_comments = pd.read_csv('../../data/comments.csv')
unlabeled = all_comments['text'].apply(lambda s: s.replace('_', ' '))

labels = sample['LABEL']
contents = sample['text'].apply(lambda s: s.replace('_', ' '))

# use CountVectorizer
cv_contents = CountVectorizer(input='content', stop_words='english')
dtm_train = cv_contents.fit_transform(contents)
colnames = cv_contents.get_feature_names()
print(f'The vocab has {len(colnames)} words, and they are: {colnames}\n\n')

# train SVM
model = LinearSVC()
model.fit(dtm_train, labels)
print(model.score(dtm_train, labels))

dtm_pred = cv_contents.transform(unlabeled)

labels_pred = model.predict(dtm_pred)
print(len(labels_pred))

# convert to dataframe
# real_dtm = cv_contents.fit_transform(unlabeled)
# colnames = cv_contents.get_feature_names()
# content_df = pd.DataFrame(real_dtm.toarray(), columns=colnames)
content_df = pd.DataFrame(dtm_pred.toarray(), columns=colnames)
content_df.insert(0, 'LABEL', value=labels_pred)
content_df.to_csv('../../data/comments_dtm_labeled.csv', index=False)

all_comments.insert(0, 'LABEL', value=labels_pred)
print(all_comments.head())
all_comments.to_csv('../../data/comments_labeled.csv', index=False)
