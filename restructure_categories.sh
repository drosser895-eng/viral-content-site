#!/bin/bash
# Restructure category pages for proper GitHub Pages routing

BUILD_DIR="/Users/davidrosser/clawd/viral-content-site/_build"

# Create category directories and move HTML files to index.html inside each
for category_file in "$BUILD_DIR"/category/*.html; do
    if [ -f "$category_file" ]; then
        category_name=$(basename "$category_file" .html)
        category_dir="$BUILD_DIR/category/$category_name"
        
        # Create directory
        mkdir -p "$category_dir"
        
        # Move the html file to index.html inside the directory
        mv "$category_file" "$category_dir/index.html"
        
        echo "Moved $category_name to directory structure"
    fi
done

echo "Category pages restructured for clean URLs"