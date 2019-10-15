import csv, sys, os
from langdetect import detect
from multiprocessing import Pool

# input specification: python language_analysis.py [country_code] [programming_language]
# country_code options: fr, ch, be, qb, sn, all
# programming_language options: js, py, java, all

# this version of language_analysis uses multiprocessing for faster analysis on GCP

# input error handling
if len(sys.argv) is not 3:
    sys.exit('Please specify a country code (fr, ch, be, qb, sn, all) and programming language (js, py, java, all).')

# get country code and programming language from input arguments
country_code = sys.argv[1]
programming_language = sys.argv[2]

# increase csv field limit
csv.field_size_limit(sys.maxsize)

def detect_file(i):
    # used for tracking progress through files
    print('*** FILE '+ str(i) + ' ***')

    # map for languages
    languages = {}

    with open('data/comments/comments_'+ str(i) + '.csv', 'r') as file:
        r = csv.reader(file)

        for row in r:
            # skip first header row
            if r.line_num is 1:
                continue

            # used for tracking progress through lines
            if r.line_num % 100000 == 0:
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

    return languages

# pool size is based on number of CPUs
pool_size = os.cpu_count()
pool = Pool(pool_size)

results = pool.map(detect_file, range(10))
pool.close()

# sum up per-file language results
languages_all = {}
for result in results:
    for language in result:
        if language in languages_all:
            languages_all[language] += result[language]
        else:
            languages_all[language] = result[language]
print(languages_all)
