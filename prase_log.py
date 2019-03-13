import json

f = open('apcahe_log.log', 'r')
for line in f:
    ip = line.split('- -')[0]
    date = line.split(']')[0].split('[')[1].split(':')[0]
    url = line.split('] ')[1]
    # outfile = open('output.txt',)
    print "{IP:",ip,",Date:",date,",URL:",url,"}"