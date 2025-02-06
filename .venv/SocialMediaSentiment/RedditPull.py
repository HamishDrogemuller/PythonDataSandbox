import praw
import pandas as pd

reddit = praw.Reddit(
    client_id="VMu4VnURnEOgFR1oBTUrAQ",
    client_secret="AZyHOM2zrenMvjjCwCwe2mltTOVT0g",
    user_agent="StrixPull"
)

# List of subreddits to scrape
subreddits = ["technology", "science", "worldnews", "ArtificialIntelligence"]

# Define a function to fetch posts from multiple subreddits
def fetch_reddit_posts(subreddits, topic, limit=50):
    all_posts = []

    for subreddit in subreddits:
        print(f"Fetching posts from r/{subreddit} on topic: {topic}")
        
        subreddit_obj = reddit.subreddit(subreddit)
        posts = subreddit_obj.search(topic, limit=limit)

        for post in posts:
            all_posts.append({
                "subreddit": subreddit,
                "title": post.title,
                "text": post.selftext,
                "upvotes": post.score,
                "comments": post.num_comments,
                "created_utc": post.created_utc,
                "url": post.url
            })

    return pd.DataFrame(all_posts)

# Example: Fetch posts related to "AI" from multiple subreddits
df_reddit = fetch_reddit_posts(subreddits, "AI", 50)
print(df_reddit.head())
