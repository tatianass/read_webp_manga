"""Creates a list of all files that are in folders and subfolders"""
import os

main_dir = '<pick_main_path>'

map_dir = []
for dir in os.listdir(main_dir):
	for img in os.listdir(main_dir + dir):
		map_dir.append(main_dir + dir + "/" + img)

with open('../data/list_paths.txt', 'w') as f:
	for row in map_dir:
		f.write(str(row) + ',')