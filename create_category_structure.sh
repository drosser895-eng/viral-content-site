#!/bin/bash
# Script to create proper category directory structure in main directory
# This will fix the 404 errors on category pages

set -e

echo "Creating proper category directory structure..."

# Define categories
categories=(
    "pop-culture"
    "celebrity-gossip" 
    "lifestyle-hacks"
    "money-saving"
    "tech-gadgets"
    "health-wellness"
    "viral-videos"
)

# Create category directories if they don't exist
for category in "${categories[@]}"; do
    mkdir -p "category/$category"
    
    # Create index.html for each category
    cat > "category/$category/index.html" << EOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$category - TrendSpotter</title>
    <meta name="description" content="Latest viral content about $category">
    <link rel="stylesheet" href="/css/style.css">
    <script src="/js/main.js"></script>
</head>
<body>
    <header>
        <h1><a href="/">TrendSpotter</a></h1>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <h2>$category</h2>
        <div class="articles-list">
            <!-- Articles will be populated by JavaScript -->
        </div>
    </main>
    
    <footer>
        <p>&copy; 2026 TrendSpotter. All rights reserved.</p>
    </footer>
</body>
</html>
EOF
done

echo "Category directory structure created successfully!"