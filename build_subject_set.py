import pandas
from search_text import search

MAX_NUMBER = 500

keywords = pandas.read_csv('example_keywords.csv', header=None)[0].tolist()
result = pandas.DataFrame(search(*keywords, max_number=MAX_NUMBER))
result.columns = ['file_name', 'keyword_score']

subjects = pandas.read_csv('diagnosis-london-subjects.csv')
subjects.metadata = subjects.metadata.apply(eval)

# all existing subject
subject_id_lut = {}
for sdx, subject in subjects.iterrows():
    if 'ocr' in subject.metadata:
        file_name = subject.metadata['ocr']
    elif 'filename' in subject.metadata:
        file_name = subject.metadata['filename'] + '.txt'
    subject_id_lut[file_name] = subject.subject_id

# list subject_id if available
result['subject_id'] = [subject_id_lut[file] if file in subject_id_lut else None for file in result.file_name]
result.to_csv('subject_file_names.csv', index=False)

# This is the best I can do for now
# Once all subjects have been uploaded this script should also create and link a new subject set
