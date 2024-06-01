from urllib.parse import urlparse, parse_qs
from pandas import read_csv

data = read_csv('task1_input.tsv', sep='\t')

for url in data['url']:
  parsed_url = urlparse(url)
  query_params = parse_qs(parsed_url.query)
  print(f"Params: {query_params}")
