from urllib.parse import urlparse, parse_qs
import pandas as pd

input = pd.read_csv('task1_input.tsv', sep='\t')
output = pd.DataFrame()

for url in data['url']:
  parsed_url = urlparse(url)
  query_params = parse_qs(parsed_url.query)

  row = {'URL': url}
  row.update(query_params)
  output = output._append(row, ignore_index=True)

print(output)
