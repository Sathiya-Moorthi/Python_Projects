from urllib.request import urlretrieve, Request, urlopen

url = "https://whimsical.com/basic-to-advance-data-engineer-roadmap-HxryZaFajFKqZyQEGtkVVk"
output_file = "D:\MyProject\Data_Engineer_rodmap"

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urlopen(req) as response, open(output_file, 'wb') as out_file:
    data = response.read()
    out_file.write(data)
