import feedparser
# used to take rss and make it a readable format 

def get_latest_torrents():
    """
    Fetches the latest English-translated anime releases from Nyaa.si's RSS feed.
    """
    # Nyaa.si RSS URL filtered for: Category = Anime, Sub-category = English-translated
    rss_url = "https://nyaa.si/?page=rss&c=1_2&f=0"
    
    # Parse the XML feed into a Python dictionary
    feed = feedparser.parse(rss_url)
    
    releases = []
    
    # Loop through the first 10 entries to see what the data looks like
    for entry in feed.entries[:10]:
        release_data = {
            "title": entry.title,
            "link": entry.link
        }
        releases.append(release_data)
        
    return releases

# This block only runs if you execute this specific file directly
if __name__ == "__main__":
    print("Fetching the latest releases...\n")
    latest = get_latest_torrents()
    
    for item in latest:
        print(f"Title: {item['title']}")
        print(f"Link:  {item['link']}\n")