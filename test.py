
processed_file = pd.read_csv('output.tsv', sep='\t')
desired_output = pd.read_csv('task1_output.tsv', sep='\t')

if filecmp.cmp('output.tsv', 'task1_output.tsv'):
    print("OK")
    exit()
else:
    if not processed_file.columns.equals(desired_output.columns):
        print("NOT OK - Different columns(order or names)")
    if len(processed_file) != len(desired_output):
        print("NOT OK - Different number of records")
    else:
        print("NOT OK - Lack of specific information")
