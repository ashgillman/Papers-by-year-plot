import subprocess
import re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import pylab as pl
import yaml

scholar = '/scholar.py/scholar.py'
lookup_file = 'lookup.yml'
years = np.arange(1990, 2015+1)
years = np.arange(2013, 2015+1)

with open(lookup_file) as f:
    data = yaml.safe_load(f)

    ps = []

    for key, search in data.items():
        print(key, ':')

        results = []

        for year in years:
            query = [scholar, '--title-only', '--txt-globals',
                     '--before', str(year), '--after', str(year)]
            for type, terms in search.items():
                query.extend(['--{}'.format(type), '{}'.format(terms)])
            print(' '.join(query))

            query_result = subprocess.check_output(query).decode('utf-8')

            for line in query_result.split('\n'):
                if '[G]' in line:
                    if 'Results' in line:
                        result = int(re.search('\d+', line).group(0))
                        print(result)
                        results.append(result)

        ps.append(pl.bar(years, results))

    pl.ylabel('Results')
    pl.title('No. papers published by year and subject')
    pl.xticks(tuple(years))
    pl.legend(tuple(data.keys()))

    pl.savefig('img.png')
