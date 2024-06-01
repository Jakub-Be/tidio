from urllib.parse import urlparse, parse_qs

url = "https://www.tidio.com/?utm_source=source1&utm_medium=cpc&utm_campaign=999999999&utm_content=9999999utm_term=+fake_term+chat&a_bucket=bucket1&a_type=type1&a_source=source1&a_v=2&a_g_campaignid=999999999&a_g_keyword=+fake_term&a_g_adgroupid=999999999&a_g_creative=999999999"

parsed_url = urlparse(url)
query_params = parse_qs(parsed_url.query)

print(query_params)
