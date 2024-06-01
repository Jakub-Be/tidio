from urllib.parse import urlparse, parse_qs
import pandas as pd

input = pd.read_csv('task1_input.tsv', sep='\t')
rows = []

for url in data['url']:
  parsed_url = urlparse(url)
  query_params = parse_qs(parsed_url.query)

  row = {'url': url}
  for key, value in query_params.items():
    row[key] = value[0]
  rows.append(row)

output = pd.DataFrame(rows)
output.to_csv('output.tsv', sep='\t', index=False)

print(output)
