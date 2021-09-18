import requests
import sys
from bs4 import BeautifulSoup
import re

url = sys.argv[1]
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

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
		r = requests.get(url,headers=header)
		print("fetched... ", end='')
		soup = BeautifulSoup(r.text, "html.parser")
		a = soup.find("a", {"class": "atomsGalleryButtonsNavigation__right"})
		img = soup.find("source", {"srcset" : re.compile("xlarge\.jpg")})
		if not img:
			print("[!] Image not found! Exiting...")
			break

		print("image found!")
		images.append(img['srcset'].split('?')[0])
		if not a:
			break

		url = domain + a['href']
finally:
	save(images)

print("Done. Check images.txt")
