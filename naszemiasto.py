import requests
import sys
from bs4 import BeautifulSoup

url = sys.argv[1]

domain = '/'.join(url.split("/")[:3])  # https + domain name
n = 0

def save(items):
	with open("images.txt", "w", encoding="utf-8") as f:
		f.write('\n'.join(items))

images = []
try:
	while True:
		n += 1
		print(f"[*] Fetching page {n}... ", end='')
		r = requests.get(url)
		print("fetched... ", end='')
		soup = BeautifulSoup(r.text, "html.parser")
		a = soup.find("a", {"id": "material-galeria-nastepne"})
		img = soup.find("figure", {"class": "galZdjecie"}).find("img")
		if not img:
			print("[!] Image not found! Exiting...")
			break

		print("image found!")
		images.append(img['src'].split('?')[0])
		if not a:
			break

		url = domain + a['href']
finally:
	save(images)

print("Done. Check images.txt")