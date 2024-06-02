from urllib.parse import urlparse, parse_qs
import pandas as pd

data = read_csv('task1_input.tsv', sep='\t')

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

for index, row in data.iterrows():
    parsed_url = urlparse(row['url'])
    query_params_dict = parse_qs(parsed_url.query)
    for query_param_name, mapped_column in mapping_dict.items():
        data.at[index, mapped_column] = query_params_dict.get(query_param_name, [''])[0]

data.to_csv('output.tsv', sep='\t', index=False)
