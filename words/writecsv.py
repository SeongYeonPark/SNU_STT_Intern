import csv
from google.cloud import storage
import shutil
import os

bucket_name = 'snu_ensub_project'

def addword(spec, srt, arr):
    fname = 'glossary/' + spec + '_ko_en_g.csv'
    destination = fname
    with open('./'+fname, 'a', encoding='utf-8', newline='') as f:
        wr = csv.writer(f)
        wr.writerow([srt, arr])
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination)

    blob.upload_from_filename(fname)

def delword(spec, srt, arr):
    fname = 'glossary/'+ spec + '_ko_en_g.csv'
    tmp = '_' + spec + '_ko_en_g.csv'
    destination = fname

    shutil.copy(fname,tmp)
    tmpfr = open('./'+tmp, 'r', encoding='utf-8', newline='')
    tmpfw = open('./'+fname, 'w', encoding='utf-8', newline='')
    fr=csv.reader(tmpfr)
    fw=csv.writer(tmpfw)
    for row in fr:
        if (srt not in row[0]) or (arr not in row[1]):
            fw.writerow(row)
    tmpfr.close()
    tmpfw.close()
    os.remove('./'+ tmp)

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination)

    blob.upload_from_filename(fname)
    
