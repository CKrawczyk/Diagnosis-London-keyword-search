import pandas
import nltk
from search_text import search

MAX_NUMBER = 2000

subjects = pandas.read_csv('diagnosis-london-subjects.csv')
subjects.metadata = subjects.metadata.apply(eval)

csv_input_files = [
    'DL_keywords_A',
    'DL_keywords_B',
    'DL_keywords_C',
    'DL_keywords_D',
]

for input_file in csv_input_files:
    keywords = pandas.read_csv('{0}.csv'.format(input_file), header=None)[0].tolist()
    result = pandas.DataFrame(search(*keywords, max_number=MAX_NUMBER))
    result.columns = ['file_name', 'keyword_score']

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
    result.to_csv('subject_file_names_{0}.csv'.format(input_file), index=False)
