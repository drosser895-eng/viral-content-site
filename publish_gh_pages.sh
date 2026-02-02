#!/bin/bash
# Script to publish the _build directory to gh-pages branch for GitHub Pages (Viral Content site)

set -e  # Exit on any error

REPO_PATH="/Users/davidrosser/clawd/viral-content-site"
BUILD_PATH="$REPO_PATH/_build"
LOG_FILE="$REPO_PATH/logs/deploy.log"

# Create logs directory if it doesn't exist
mkdir -p "$REPO_PATH/logs"

# Log the start of the deployment
echo "$(date): Starting GitHub Pages deployment" >> "$LOG_FILE"

# Safety checks
if [ ! -d "$BUILD_PATH" ]; then
    echo "$(date): ERROR - Build directory does not exist: $BUILD_PATH" >> "$LOG_FILE"
    exit 1
fi

echo "$(date): Build verification passed" >> "$LOG_FILE"

# Create a temporary directory for the gh-pages branch
TEMP_DIR=$(mktemp -d)

# Clone the repo into the temp directory with only the gh-pages branch
if git clone -b gh-pages "https://github.com/drosser895-eng/viral-content-site.git" "$TEMP_DIR" 2>/dev/null; then
    echo "$(date): Successfully cloned gh-pages branch" >> "$LOG_FILE"
else
    # If gh-pages branch doesn't exist, create it
    echo "$(date): gh-pages branch doesn't exist, creating it" >> "$LOG_FILE"
    git clone "https://github.com/drosser895-eng/viral-content-site.git" "$TEMP_DIR"
    cd "$TEMP_DIR"
    git checkout --orphan gh-pages
    git reset --hard
    git commit --allow-empty -m "Initial gh-pages commit"
    git push -u origin gh-pages
    cd "$REPO_PATH"
fi

# Copy the contents of _build to the temp directory
cp -r "$BUILD_PATH"/* "$TEMP_DIR/"

# Add CNAME file if needed (uncomment and modify if you have a custom domain)
# echo "trendspotter-daily.com" > "$TEMP_DIR/CNAME"

# Commit and push to gh-pages
cd "$TEMP_DIR"
git add .
if git diff --quiet && git diff --staged --quiet; then
    echo "$(date): No changes to deploy" >> "$LOG_FILE"
else
    git config user.name "David Rosser"
    git config user.email "davidrosser@users.noreply.github.com"
    git commit -m "Update GitHub Pages [ci skip] - $(date)"
    git push origin gh-pages
    
    if [ $? -eq 0 ]; then
        echo "$(date): Successfully deployed to GitHub Pages" >> "$LOG_FILE"
        echo "$(date): Deployment completed successfully" >> "$LOG_FILE"
    else
        echo "$(date): ERROR - Failed to push to GitHub Pages" >> "$LOG_FILE"
        exit 1
    fi
fi

cd "$REPO_PATH"
rm -rf "$TEMP_DIR"

echo "$(date): GitHub Pages deployment script finished" >> "$LOG_FILE"