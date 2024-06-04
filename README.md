# tidio-python

This repository contains method of parsing URLs to extract data. The input data is provided in the file task1_input.tsv. The goal is to produce a .tsv file identical to task1_output.tsv

# Repository Contents
- Parsing.py: The main script to parse URLs and generate the output file
- test.py: A script to test the functionality of Parsing.py
- task1_input.tsv: The input file containing the URLs to be parsed
- task1_output.tsv: The expected output file for comparison
- requirements.txt: A list of required packages

# Task Description
The main goal is to parse URLs and extract specific parameters. The URLs are structured as follows:
```
https://www.tidio.com/?utm_source=source1&utm_medium=cpc&utm_campaign=999999999&utm_content=9999999utm_term=+fake_term+chat&a_bucket=bucket1&a_type=type1&a_source=source1&a_v=2&a_g_campaignid=999999999&a_g_keyword=+fake_term&a_g_adgroupid=999999999&a_g_creative=999999999
```

# Query parameters Mapping is done according to the following key:
```python
mapping_dict = {
        'a_bucket': 'ad_bucket',
        'a_type': 'ad_type',
        'a_source': 'ad_source',
        'a_v': 'schema_version',
        'a_g_campaignid': 'ad_campaign_id',
        'a_g_keyword': 'ad_keyword',
        'a_g_adgroupid': 'ad_adgroup_id', #should be ad_group_id?
        'a_g_creative': 'ad_creative'
    }
```

# Installation

1.Clone the repository
```bash
git clone https://github.com/Jakub-Be/tidio-python.git
cd tidio-python
```

2.Create a virtual environment and activate it:
```bash
python -m venv venv
.\venv\Scripts\activate
```

3.Install the required packages:
```bash
pip install -r requirements.txt
```

# Usage and testing

1.Run the main script to parse the URLs and generate the output file:
```bash
python Parsing.py [path to a folder with input file]
```

2.To verify the correctness of the solution, run the test script:
```bash
python test.py
```


