# read_webp_manga
Just a simple website to read webp manga, since I can't find a reader for it and I don't feel like opening page by page or converting in other kind of format. I have also added the code that I used to download some webp images.

## Requirements
* Python 3.6+;
* requests==2.18.4;
* beautifulsoup4==4.8.2.

## How to use it

1. Download the project;
2. If you have a txt file with all of your local images paths, skip to step 5;
3. Install `requirements.txt` using `pip install -r requirements.txt`;
3. Download images from an website using the code in `assets/code/save_img_from_webpage.py`:
  * Run the code like this: `python save_img_from_webpage.py <start_num> <chapters_num> <download_path> <match_str> <prefix_url> <sufix_url>`
 4. Create a text file using the code in `assets/code/list_files_saved.py`:
  * Run this: `python list_files_saved.py <download_path>`
  * Your txt file is going to be saved in `assets/data/`
5. Open index.html on your browser;
6. Upload a txt file with paths to your images:
  * It needs to be something like: C:/Users/John/Manga/01/1.webp.

## Utilities
So far you can filter for which chapter you want to see and go to top of the page.

## Downloading images explanation
This is the documentation for `assets/code/save_img_from_webpage.py`:
* `start_num (int)`: Start download from chapter x.
* `chapters_num (int)`:  End download until chapter x.
* `download_path (str)`:  Local path to download (e.g. C:/Users/x/Downloads).
* `match_str (str)`:  Matching image format (e.g. webp, png, jpg).
* `prefix_url (str)`:  Prefix of url to download from (e.g. https:images.google.com/...).
* `sufix_url (str)`: Sufix of url to download from (e.g. .html).
