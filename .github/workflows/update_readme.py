import feedparser
import os

README_FILE = "README.md"

def update_readme(blog_posts):
    with open(README_FILE, "r") as file:
        content = file.read()

    new_content = content.replace(
        "<!-- BLOG-POST-LIST:START -->\n<!-- BLOG-POST-LIST:END -->",
        f"<!-- BLOG-POST-LIST:START -->\n{blog_posts}\n<!-- BLOG-POST-LIST:END -->"
    )

    with open(README_FILE, "w") as file:
        file.write(new_content)

if __name__ == "__main__":
    blog_posts = fetch_blog_posts()
    update_readme(blog_posts)
