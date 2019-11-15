import json

data = '[{ "nama" : "Hadi", "alamat" : "Gandasuli Brebes" },' \
       '{ "nama" : "Yanto", "alamat" : "Tegal" }]'

result = json.loads(data)

for x in result:
    print(x['nama'])