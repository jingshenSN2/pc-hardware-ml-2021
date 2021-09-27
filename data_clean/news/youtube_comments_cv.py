import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC

sample = pd.read_csv('comment_sample_labeled.csv')
all_comments = pd.read_csv('../../data/comments.csv')
unlabeled = all_comments['text']

labels = sample['LABEL']
contents = sample['text']
print('Rows of train set: ', len(labels))
print('Rows of train set labeled 1: ', sum(labels))

# use CountVectorizer
cv_contents = CountVectorizer(input='content', stop_words='english')
dtm_train = cv_contents.fit_transform(contents)
colnames = cv_contents.get_feature_names()
print(f'The vocab has {len(colnames)} words, and they are: {colnames}\n')

# train SVM
model = LinearSVC()
model.fit(dtm_train, labels)
print('SVM model accuracy on train set:', model.score(dtm_train, labels))

dtm_pred = cv_contents.transform(unlabeled)

labels_pred = model.predict(dtm_pred)
print('Rows of all data: ', len(labels_pred))
print('Rows of all data labeled 1: ', sum(labels_pred))

# convert to dataframe
# real_dtm = cv_contents.fit_transform(unlabeled)
# colnames = cv_contents.get_feature_names()
# content_df = pd.DataFrame(real_dtm.toarray(), columns=colnames)
content_df = pd.DataFrame(dtm_pred.toarray(), columns=colnames)
content_df.insert(0, 'LABEL', value=labels_pred)
# content_df.to_csv('../../data/comments_dtm_labeled.csv', index=False)
# too large file, don't commit

all_comments.insert(0, 'LABEL', value=labels_pred)
print('20 comments with label 0:')
[print('\t', row) for row in all_comments[all_comments['LABEL'] == 0]['text'].sample(20, random_state=501)]
print('20 comments with label 1:')
[print('\t', row) for row in all_comments[all_comments['LABEL'] == 1]['text'].sample(20, random_state=501)]
all_comments.to_csv('../../data/comments_labeled.csv', index=False)
