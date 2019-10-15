import csv, sys
from langdetect import detect

# input specification: python language_analysis.py [country_code] [programming_language]
# country_code options: fr, ch, be, qb, sn, all
# programming_language options: js, py, java, all

# input error handling
if len(sys.argv) is not 3:
    sys.exit('Please specify a country code (fr, ch, be, qb, sn, all) and programming language (js, py, java, all).')

# get country code and programming language from input arguments
country_code = sys.argv[1]
programming_language = sys.argv[2]

# map for languages
languages = {}

# increase csv field limit
csv.field_size_limit(sys.maxsize)

for i in range(0, 10):
    # used for tracking progress through files
    print(f'*** FILE {i} ***')
    with open(f'../data/comments/comments_{i}.csv', 'r') as file:
        r = csv.reader(file)
        header = True

        for row in r:
            # skip first header row
            if header:
                header = False
                continue

            # used for tracking progress through lines
            if r.line_num % 1000 == 0:
                print(r.line_num)

            # skip if we're not doing all programming languages and this isn't the specified one
            if programming_language != 'all' and row[0] != programming_language:
                continue

            # skip if we're not doing all countries and this isn't the specified one
            if country_code != 'all' and row[1] != country_code:
                continue

            # try to detect language of comment; if none found, mark as such
            try:
                language = detect(row[2])
            except:
                language = 'n/a'

            if language in languages:
                languages[language] += 1
            else:
                languages[language] = 1

    print(languages)
