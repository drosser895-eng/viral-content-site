#!/usr/bin/env python3
"""
Script to convert existing posts to the new directory/index.html structure
"""
import os
import shutil
from pathlib import Path

def convert_posts_to_directory_structure():
    """Convert all existing .html post files to directory/index.html structure"""
    posts_dir = Path("posts")
    
    for category_dir in posts_dir.iterdir():
        if not category_dir.is_dir():
            continue
            
        for post_file in category_dir.glob("*.html"):
            # Extract the slug from the filename
            slug = post_file.stem  # removes the .html extension
            
            # Create the new directory structure
            new_dir = category_dir / slug
            new_dir.mkdir(exist_ok=True)
            
            # Move the file to index.html in the new directory
            new_file = new_dir / "index.html"
            shutil.move(str(post_file), str(new_file))
            
            print(f"Converted: {post_file.name} -> {new_dir}/index.html")

if __name__ == "__main__":
    convert_posts_to_directory_structure()
    print("Post conversion complete!")