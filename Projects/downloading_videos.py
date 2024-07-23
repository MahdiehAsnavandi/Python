import requests
from bs4 import BeautifulSoup
import os
import requests 
from urllib.parse import urlparse

def get_base_url(url):
    try:
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}/"
        return base_url
    except Exception as e:
        print(f"Error parsing URL: {str(e)}")
        return None
    
def download_video(video_url, video_path):
    try:
        # Send a GET request to the video URL
        response = requests.get(video_url, stream=True)
        response.raise_for_status()  # Check for request errors

        # Open a file to write the video content
        output_filename = video_path + os.path.basename(video_url).split('name=')[-1]
        with open(output_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Downloaded: {output_filename}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download video: {str(e)}")

def get_video_url(page_url):
    response = requests.get(page_url, cookies={'sessionid': 'z9bmkb9nk2u02aspg3u4pxbb817rbj83'})
    soup = BeautifulSoup(response.text, 'html.parser')
    video_tag = soup.find('video')
    if video_tag:
        source_tag = video_tag.find('source')
        if source_tag and source_tag.has_attr('src'):
            return source_tag['src']
    return None

def main(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    a_tags = soup.find_all('a', {"class": "flex p-10 border-0 border-b-hawkes-blue border-solid bg-white justify-between rounded-none cursor-pointer"})
    video_urls = []

    base_url = get_base_url(page_url)
    for a in a_tags:
        if 'href' in a.attrs:
            href = base_url + a['href']
            if href.startswith('http'):
                video_url = get_video_url(href)
                if video_url:
                    video_urls.append(video_url)
    
    video_path = 'videos/'
    if not os.path.exists(video_path):
        os.makedirs(video_path)

    for video_url in video_urls:
        download_video(video_url, video_path)

if __name__ == "__main__":
    # Replace with your initial page URL
    page_url = open('page_url.txt', 'r').read()
    main(page_url)
