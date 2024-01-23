from bs4 import BeautifulSoup
import requests
import time

def soupify(url):

	headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9,This is a personal project to learn Python',
    }

	try:
		response = requests.get(url, headers)

		if response.status_code == 200:
			time.sleep(0.5)
			soup = BeautifulSoup(response.text, 'html.parser')
			return soup
		else:
			print(f'RESPONSE ERROR Getting this HTTP response: {response.status_code}')
		
	except requests.RequestException as e:
		print(f'Error in soupify()! {e}')	
		return None

def bglyrics_dotcom():
	selector_css = 'li.song a[href]'
	start_url='https://www.bluegrasslyrics.com/'

	hrefs = [a for a in soupify(start_url).select(selector_css)]
	lyric_content = [f'{a["href"]}' for a in hrefs]

	return lyric_content

def tradmusic_co_uk():
	start_url='https://www.traditionalmusic.co.uk/bluegrass-lyrics/bgl00.html'
	stage_1_selector_css = 'div.mainlinkCopy4  a[href^="bg"]'
	stage_2_selector_css = 'div.songlinks a[href]'
	stage_3_selector_css = 'pre'

	stage_1 = [i for i in soupify(start_url).select(stage_1_selector_css)]
	stage_2 = [start_url[:-10]+i['href'] for i in stage_1]
	stage_3 = [soupify(i).select(stage_2_selector_css) for i in stage_2]
	for i in stage_3:
		for j in i:
			song_url = start_url[:-10]+j['href']
			lyric_content = soupify(song_url).select(stage_3_selector_css)

	return lyric_content	


def main():
	data = bglyrics_dotcom()+tradmusic_co_uk()

if __name__ == "__main__":
	main()


	