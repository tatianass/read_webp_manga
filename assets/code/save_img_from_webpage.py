"""Saves images from an webpage"""

from bs4 import BeautifulSoup, SoupStrainer
import requests
import os
import urllib
import sys

def save_images(
	start_num: int, 
	chapters_num: int, 
	download_path: str, 
	match_str: str, 
	prefix_url: str, 
	sufix_url: str
):
	"""
		# This for is for pages that follow a pattern for chapters
		# e.g. https://manga/01, https://manga/02 ...
		# Pick from 1 to max of chapters + 1
		Args:
			start_num (int): Start download from chapter x.
			chapters_num (int):  End download until chapter x.
			download_path (str):  Local path to download (e.g. C:/Users/x/Downloads).
			match_str (str):  Matching image format (e.g. webp, png, jpg).
			prefix_url (str):  Prefix of url to download from (e.g. https:images.google.com/...).
			sufix_url (str): Sufix of url to download from (e.g. .html).

	"""
	
	for i in range(start_num, chapters_num+1):
		url = f"{prefix_url}{i}{sufix_url}"

		page = requests.get(url)    
		data = page.text
		soup = BeautifulSoup(data)
		save_path = f"{download_path}/{i:02d}/"

		# Create dir to save images
		os.mkdir(save_path)
		for link in soup.find_all('img'):
			src = link.get('src')
			if '.'+match_str in src:
				file_name = os.path.basename(src)[0:-1]
				urllib.request.urlretrieve(src, os.path.join(save_path, file_name))

if __name__ == '__main__':
	start_num = int(sys.argv[1])
	chapters_num = int(sys.argv[2])
	download_path = str(sys.argv[3])
	match_str = str(sys.argv[4])

	prefix_url = str(sys.argv[5])

	sufix_url = ''
	try:
		sufix_url = str(sys.argv[6])
	except Exception as e:
		sufix_url = ''

	save_images(start_num, chapters_num, download_path, match_str, prefix_url, sufix_url)