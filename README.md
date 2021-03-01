# Text Analysis and Information Extraction From Online Gonverment Sources

This is a tool to extract information about monetary transactions
from the greek gonverment decisions and compare them to their submited date, type
of decision and other available data information. 

This program was created as a thesis project from Ismini Veneti, for the
Harokopio University of Athens.


## Data
The data is extracted from the [diavgeia](https://www.diavgeia.gov.gr/) project, and later
saved in [feather](https://github.com/wesm/feather) format to be
reused whenever it's needed.

## How it works

The program uses [spaCy](https://github.com/explosion/spaCy) NER to
extract the monetary information from the subjects of a decision. Using
[doccano](https://github.com/doccano/doccano), a custom labeled dataset was
created and added to the existing model (el_core_news_lg). The new model
(CNERD) was used to extract the monetary information from the subject of
the decisions in the [diavgeia](https://www.diavgeia.gov.gr/) API, and saved
alongside the existing metadata. 

After that, the results may be provided to create a bar for the total exchanged 
currency compared to the selected metadata.


## Roadmap
In the future, this program we will add more tools and extract more
information from a single decision.

## License
[Apache-2.0](https://choosealicense.com/licenses/apache-2.0/)
