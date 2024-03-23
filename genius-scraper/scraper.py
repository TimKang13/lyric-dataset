import requests
import config
import sys
import csv
from bs4 import BeautifulSoup


def get_artist_id(artist_name):

	artist_id = None
	params = {'q': artist_name}
	response = requests.get(base_url+'/search', params=params, headers=headers)
	json = response.json()

	for hit in json["response"]["hits"]:
		if (hit["result"]["primary_artist"]["name"]==artist_name) and (hit["type"]=="song"):
			artist_id = hit["result"]["primary_artist"]["id"]
			break

	if artist_id:
		print("Collecting songs for", artist_name, ": Artist ID", artist_id)
		return artist_id
	else:
		print("Artist", artist_name, "not found.")
		return -1


def get_song_urls(artist_id):

	urls = []
	
	page_count = 1
	end_of_pages = False
	while not(end_of_pages):

		# get results of current page
		temp_url = base_url+'/artists/'+str(artist_id)+'/songs?per_page=50&page='+str(page_count)
		response = requests.get(temp_url, headers=headers)
		response.encoding = 'utf-8'
		json = response.json()

		for song in json["response"]["songs"]:

			if song["primary_artist"]["id"]==artist_id:

				urls.append(song["path"])
		
		if json["response"]["next_page"]==None:
			end_of_pages=True
		else:
			page_count+=1

	print(len(urls), "songs found")

	return urls


def get_lyrics(song_urls):

	lyrics = []

	for url in song_urls:

		page = requests.get("https://genius.com" + url)

		if page:

			html = BeautifulSoup(page.text, "html.parser")
			[h.extract() for h in html("script")]

			text = ""
			div = html.find("div", class_=lambda value: value and value.startswith("Lyrics__Container-"))
			if div: 
				text = div.get_text(separator="\n", strip=True)
				lyrics.append(text)
			else:
				print("The desired div was not found.")
				
		if (len(lyrics)/2)%100==0:
			print(int(len(lyrics)/2), "/", len(song_urls), "lyrics processed")
	
	return lyrics 


if __name__ == '__main__':

	# artist input
	if len(sys.argv[1:])==0:
		print("You must pass a parameter for artist name e.g. \"The Beatles\"")
		sys.exit(0)
	
	for artist_name in sys.argv[1:]:

		# api key and authorisation
		base_url = "http://api.genius.com"
		#api_key = config.access_token
		api_key = "VZWLZcTi0Sm-oU144kwvBucqs7L6Jqk_N7MoeUU54nDArQWafEoFYgNSOISWDQhm"
		auth_string = 'Bearer ' + api_key
		headers = {'Authorization': auth_string}

		# get lyrics
		artist_id = get_artist_id(artist_name)
		if artist_name == -1:
			continue
		song_urls = get_song_urls(artist_id)
		lyrics = get_lyrics(song_urls)
		print(len(lyrics))
		filename = artist_name.replace(" ", "_") + ".csv"

		with open(filename, mode='w', newline='', encoding='utf-8') as file:
			writer = csv.writer(file)
		
		# Iterate over the array of strings
			for index, string in enumerate(lyrics, start=1):
			# Write each string in a new row. csv.writer expects an iterable for each row,
			# so we wrap the string in a list to make it a single-column row.
				writer.writerow([index, artist_name, string])


