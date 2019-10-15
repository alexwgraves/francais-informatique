import csv, sys, re

# input error handling; must specify input file number
if len(sys.argv) is not 2:
    sys.exit('Please specify an input file number (0-9).')

# get file number from input arguments
file_num = sys.argv[1]

# increase csv field limit
csv.field_size_limit(sys.maxsize)

def extract_comments(contents, language):
    comments = []
    comment_delims = ['#'] if language == 'py' else ['//', '/*', '*']
    # iterate through lines in file contents, checking for comments
    for line in contents.split('\n'):
        line_trimmed = line.strip()
        for delim in comment_delims:
            # output the line with the comment deliminator removed
            if line_trimmed.startswith(delim):
                comment = line_trimmed.split(delim)[1]
                # ensure that this comments contains letters
                if re.search('[a-zA-Z]', comment) is not None:
                    comments.append(comment.strip())
    return comments

with open(f'../data/files/file_contents_{file_num}.csv', 'r') as file, \
     open(f'../data/comments/comments_{file_num}.csv', 'w') as output:
    # null bytes error handling
    r = csv.reader(line.replace('\0', '') for line in file)
    header = True

    # make writer and write header row
    w = csv.writer(output)
    w.writerow(['prog_lang', 'country_code', 'comment'])

    for row in r:
        # skip first header row
        if header:
            header = False
            continue

        # get programming language from file name
        file_name = row[0]
        language = file_name.split('.')[-1]

        # extract comments from file
        contents = row[1]
        comments = extract_comments(contents, language)

        # write comments to output csv, specifying programming language and country
        country = row[2]
        for comment in comments:
            w.writerow([language, country, comment])
