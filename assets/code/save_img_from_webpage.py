"""Saves images from an webpage"""

from bs4 import BeautifulSoup, SoupStrainer
import requests
import os
import urllib

match_str = '.webp'

# This for is for pages that follow a pattern for chapters
# e.g. https://manga/01, https://manga/02 ...
# Pick from 1 to max of chapters + 1
for i in range(1, 64):
	url = f"<https://manga/>{i}"

	page = requests.get(url)    
	data = page.text
	soup = BeautifulSoup(data)
	save_path = f"<download_path>/{i:02d}/"

	# Create dir to save images
	os.mkdir(save_path)
	for link in soup.find_all('img'):
		src = link.get('src')
		if match_str in src:
			file_name = os.path.basename(src)[0:-1]
			urllib.request.urlretrieve(src, os.path.join(save_path, file_name))
