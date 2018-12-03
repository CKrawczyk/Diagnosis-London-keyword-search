# Diagnosis London text search
This code provides a way to index and search the text files for the Diagnosis London data set. A version of [Text Rank](https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf) (via the [Summa](https://summanlp.github.io/textrank/) package) is used to create the index.

## Make the index
1. Create a `text` folder in this directory and place the OCR text files in it
2. run `python index_text.py`

This will result in an `index_normalized.json` file being created.

## Search the text
1. Create a `csv` file containing one keyword/phrase per line
2. Edit line 9 of `build_subject_set.py` to be a list of input files
3. Edit line 4 to reflect the maximum number of subjects it search should produce
3. Download the `diagnosis-london-subjects.csv` from the Project Builder (so we can get the subject ID for any existing subjects on the project)
4. Run `python build_subject_set.py`

This will results in one `subject_file_names_<original input file name>.csv` file for each input `csv` each with three columns:

1. `file_name`: The name of the text file
2. `keyword_score`: The relevance score (between 0 and 1)
3. `subject_id`: The Panoptes subject ID if the text file has already been uploaded to the system.
