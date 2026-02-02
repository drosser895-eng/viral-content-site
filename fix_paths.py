#!/usr/bin/env python3
"""
Script to fix absolute paths in viral-content-site templates for GitHub Pages compatibility
"""
import os
import re

def fix_absolute_paths_in_templates():
    """Fix absolute paths in templates to work with GitHub Pages project paths"""
    
    # Base directory
    base_dir = "/Users/davidrosser/clawd/viral-content-site"
    
    # Templates to fix
    templates = [
        os.path.join(base_dir, "templates", "post.html"),
        os.path.join(base_dir, "templates", "index.html"),
        os.path.join(base_dir, "templates", "category.html")  # if it exists
    ]
    
    # Additional files in build that might have been generated with absolute paths
    build_files = [
        os.path.join(base_dir, "_build", "index.html"),
        os.path.join(base_dir, "_build", "category", "celebrity-gossip", "index.html"),
        os.path.join(base_dir, "_build", "category", "tech-gadgets", "index.html"),
        os.path.join(base_dir, "_build", "category", "lifestyle-hacks", "index.html"),
        os.path.join(base_dir, "_build", "category", "viral-videos", "index.html"),
        os.path.join(base_dir, "_build", "category", "health-wellness", "index.html"),
        os.path.join(base_dir, "_build", "category", "money-saving", "index.html"),
        os.path.join(base_dir, "_build", "category", "pop-culture", "index.html")
    ]
    
    all_files = templates + build_files
    
    for file_path in all_files:
        if os.path.exists(file_path):
            print(f"Processing {file_path}")
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace absolute paths with relative paths or base-aware paths
            # For CSS and JS files
            content = re.sub(r'href="/css/', 'href="../css/', content)
            content = re.sub(r'src="/js/', 'src="../js/', content)
            content = re.sub(r'href="/images/', 'href="../images/', content)
            
            # For navigation links, we'll use relative paths assuming the site structure
            # For category links, replace absolute paths with relative paths
            content = re.sub(r'href="/category/', 'href="../category/', content)
            content = re.sub(r'href="/posts/', 'href="../posts/', content)
            
            # Special handling for main navigation (home, contact, etc.)
            content = re.sub(r'href="/">', 'href="./">', content)  # Home link
            content = re.sub(r'href="/contact/', 'href="../contact', content)
            content = re.sub(r'href="/privacy-policy/', 'href="../privacy-policy', content)
            content = re.sub(r'href="/affiliate-disclosure/', 'href="../affiliate-disclosure', content)
            
            # Write the updated content back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"  Fixed absolute paths in {file_path}")

if __name__ == "__main__":
    fix_absolute_paths_in_templates()
    print("Absolute path fixing complete!")