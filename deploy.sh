#!/bin/bash
# Deployment script for TrendSpotter Daily - Viral Content Website

# Configuration
SOURCE_DIR="/Users/davidrosser/clawd/viral-content-site"
BUILD_DIR="/Users/davidrosser/clawd/viral-content-site/_build"
DEPLOY_DIR="/var/www/html"  # Adjust to your actual web server directory

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Starting TrendSpotter Daily Viral Content Deployment${NC}"

# Create build directory
mkdir -p $BUILD_DIR

# Copy static assets
echo -e "${GREEN}Copying static assets...${NC}"
cp -r $SOURCE_DIR/css $BUILD_DIR/
cp -r $SOURCE_DIR/js $BUILD_DIR/
cp -r $SOURCE_DIR/posts $BUILD_DIR/
cp $SOURCE_DIR/index.html $BUILD_DIR/
cp $SOURCE_DIR/sitemap.xml $BUILD_DIR/ 2>/dev/null || echo "No sitemap.xml found, will be generated"
cp $SOURCE_DIR/feed.rss $BUILD_DIR/ 2>/dev/null || echo "No feed.rss found, will be generated"

# Create category pages
mkdir -p $BUILD_DIR/category

for category in celebrity-gossip viral-videos lifestyle-hacks tech-gadgets health-wellness money-saving pop-culture; do
    cat > $BUILD_DIR/category/${category}/index.html << EOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${category//-/ } - TrendSpotter Daily</title>
    <meta name="description" content="Viral content about ${category//-/ } on TrendSpotter Daily">
    <link rel="stylesheet" href="/css/style.css">
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-VIRALADS123"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-VIRALADS123');
    </script>
</head>
<body>
    <header>
        <div class="container">
            <div>
                <h1>TrendSpotter Daily</h1>
                <p>Your Source for Viral News, Celebrity Gossip & Lifestyle Trends</p>
            </div>
            <div class="viral-badge">🔥 VIRAL NOW!</div>
        </div>
    </header>
    
    <div class="trending-bar">
        🔥 BREAKING: Major celebrity news just dropped! • Latest tech gadget goes viral! • Life-changing hack revealed! 🔥
    </div>
    
    <nav>
        <div class="container">
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/category/celebrity-gossip/">Celebrity Gossip</a></li>
                <li><a href="/category/viral-videos/">Viral Videos</a></li>
                <li><a href="/category/lifestyle-hacks/">Lifestyle Hacks</a></li>
                <li><a href="/category/tech-gadgets/">Tech & Gadgets</a></li>
                <li><a href="/category/health-wellness/">Health Myths</a></li>
                <li><a href="/category/money-saving/">Money-Saving Tips</a></li>
                <li><a href="/category/pop-culture/">Pop Culture</a></li>
            </ul>
        </div>
    </nav>
    
    <main>
        <div class="container">
            <h1>${category//-/ } Content</h1>
            <p class="hook">Check out the hottest ${category//-/ } content that's taking the internet by storm!</p>
            
            <div class="post-grid">
                <!-- Dynamic content would go here -->
                <div class="post-card">
                    <h3>No articles yet in this category</h3>
                    <p>Check back soon for new viral content about ${category//-/ }.</p>
                </div>
            </div>
        </div>
    </main>
    
    <footer>
        <div class="container">
            <p>&copy; 2026 TrendSpotter Daily. All rights reserved.</p>
            <p>
                <a href="/privacy-policy/">Privacy Policy</a> | 
                <a href="/terms-of-service/">Terms of Service</a> | 
                <a href="/contact/">Contact</a> | 
                <a href="/affiliate-disclosure/">Affiliate Disclosure</a>
            </p>
        </div>
    </footer>
    
    <script src="/js/main.js"></script>
</body>
</html>
EOF
done

# Create affiliate disclosure page
cat > $BUILD_DIR/affiliate-disclosure.html << EOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Affiliate Disclosure - TrendSpotter Daily</title>
    <meta name="description" content="Our affiliate disclosure policy for TrendSpotter Daily">
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <header>
        <div class="container">
            <div>
                <h1>TrendSpotter Daily</h1>
                <p>Your Source for Viral News, Celebrity Gossip & Lifestyle Trends</p>
            </div>
            <div class="viral-badge">🔥 VIRAL NOW!</div>
        </div>
    </header>
    
    <div class="trending-bar">
        🔥 BREAKING: Major celebrity news just dropped! • Latest tech gadget goes viral! • Life-changing hack revealed! 🔥
    </div>
    
    <nav>
        <div class="container">
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/category/celebrity-gossip/">Celebrity Gossip</a></li>
                <li><a href="/category/viral-videos/">Viral Videos</a></li>
                <li><a href="/category/lifestyle-hacks/">Lifestyle Hacks</a></li>
                <li><a href="/category/tech-gadgets/">Tech & Gadgets</a></li>
                <li><a href="/category/health-wellness/">Health Myths</a></li>
                <li><a href="/category/money-saving/">Money-Saving Tips</a></li>
                <li><a href="/category/pop-culture/">Pop Culture</a></li>
            </ul>
        </div>
    </nav>
    
    <main>
        <div class="container">
            <h1>Affiliate Disclosure</h1>
            
            <p>TrendSpotter Daily is a participant in the Amazon Services LLC Associates Program, an affiliate advertising program designed to provide a means for sites to earn advertising fees by advertising and linking to Amazon.com.</p>
            
            <p>In addition, we may earn commissions through other affiliate programs when you click on links and make purchases. These commissions help support our work in bringing you the latest viral content and trends.</p>
            
            <p>We only recommend products that we believe will add value to our readers' lives. Our editorial content is not influenced by affiliate partnerships.</p>
            
            <p>As an Amazon Associate, I earn from qualifying purchases made through links on this site. This does not impact the price you pay for any product.</p>
            
            <p>For any questions regarding our affiliate partnerships, please contact us through our <a href="/contact/">Contact</a> page.</p>
        </div>
    </main>
    
    <footer>
        <div class="container">
            <p>&copy; 2026 TrendSpotter Daily. All rights reserved.</p>
            <p>
                <a href="/privacy-policy/">Privacy Policy</a> | 
                <a href="/terms-of-service/">Terms of Service</a> | 
                <a href="/contact/">Contact</a> | 
                <a href="/affiliate-disclosure/">Affiliate Disclosure</a>
            </p>
        </div>
    </footer>
    
    <script src="/js/main.js"></script>
</body>
</html>
EOF

# Create privacy policy page
cat > $BUILD_DIR/privacy-policy.html << EOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy - TrendSpotter Daily</title>
    <meta name="description" content="Our privacy policy for TrendSpotter Daily">
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <header>
        <div class="container">
            <div>
                <h1>TrendSpotter Daily</h1>
                <p>Your Source for Viral News, Celebrity Gossip & Lifestyle Trends</p>
            </div>
            <div class="viral-badge">🔥 VIRAL NOW!</div>
        </div>
    </header>
    
    <div class="trending-bar">
        🔥 BREAKING: Major celebrity news just dropped! • Latest tech gadget goes viral! • Life-changing hack revealed! 🔥
    </div>
    
    <nav>
        <div class="container">
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/category/celebrity-gossip/">Celebrity Gossip</a></li>
                <li><a href="/category/viral-videos/">Viral Videos</a></li>
                <li><a href="/category/lifestyle-hacks/">Lifestyle Hacks</a></li>
                <li><a href="/category/tech-gadgets/">Tech & Gadgets</a></li>
                <li><a href="/category/health-wellness/">Health Myths</a></li>
                <li><a href="/category/money-saving/">Money-Saving Tips</a></li>
                <li><a href="/category/pop-culture/">Pop Culture</a></li>
            </ul>
        </div>
    </nav>
    
    <main>
        <div class="container">
            <h1>Privacy Policy</h1>
            
            <p>Your privacy is important to us. This privacy policy explains what personal data we collect and how we use it.</p>
            
            <h2>Information Collection and Use</h2>
            <p>We collect information from you when you visit our site and interact with our content. This may include your IP address, browser type, and pages visited.</p>
            
            <h2>Log Files</h2>
            <p>Like many other sites, we use log files. These files log visitors when they visit websites. The information collected includes internet protocol (IP) addresses, browser type, Internet Service Provider (ISP), date/time stamp, referring/exit pages, and number of clicks.</p>
            
            <h2>Cookies and Web Beacons</h2>
            <p>We use cookies to store information about visitors' preferences, record user-specific information on which pages the user accesses or visits, customize web page content based on visitors' browser type or other information that the visitor sends via their browser.</p>
            
            <h2>Third Party Disclosure</h2>
            <p>We do not sell, trade, or rent users' personal identification information to others.</p>
            
            <h2>Third party links</h2>
            <p>Occasionally, at our discretion, we may include or offer third party products or services on our website. These third party sites have separate and independent privacy policies. We therefore have no responsibility or liability for the content and activities of these linked sites.</p>
            
            <h2>Google Analytics</h2>
            <p>We use Google Analytics to help analyze how visitors use our site. Google Analytics collects standard internet log information and visitor behavior information in an anonymous form.</p>
            
            <h2>Consent</h2>
            <p>By using our site, you consent to our privacy policy.</p>
        </div>
    </main>
    
    <footer>
        <div class="container">
            <p>&copy; 2026 TrendSpotter Daily. All rights reserved.</p>
            <p>
                <a href="/privacy-policy/">Privacy Policy</a> | 
                <a href="/terms-of-service/">Terms of Service</a> | 
                <a href="/contact/">Contact</a> | 
                <a href="/affiliate-disclosure/">Affiliate Disclosure</a>
            </p>
        </div>
    </footer>
    
    <script src="/js/main.js"></script>
</body>
</html>
EOF

# Create contact page
cat > $BUILD_DIR/contact.html << EOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us - TrendSpotter Daily</title>
    <meta name="description" content="Contact TrendSpotter Daily for questions and inquiries">
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <header>
        <div class="container">
            <div>
                <h1>TrendSpotter Daily</h1>
                <p>Your Source for Viral News, Celebrity Gossip & Lifestyle Trends</p>
            </div>
            <div class="viral-badge">🔥 VIRAL NOW!</div>
        </div>
    </header>
    
    <div class="trending-bar">
        🔥 BREAKING: Major celebrity news just dropped! • Latest tech gadget goes viral! • Life-changing hack revealed! 🔥
    </div>
    
    <nav>
        <div class="container">
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/category/celebrity-gossip/">Celebrity Gossip</a></li>
                <li><a href="/category/viral-videos/">Viral Videos</a></li>
                <li><a href="/category/lifestyle-hacks/">Lifestyle Hacks</a></li>
                <li><a href="/category/tech-gadgets/">Tech & Gadgets</a></li>
                <li><a href="/category/health-wellness/">Health Myths</a></li>
                <li><a href="/category/money-saving/">Money-Saving Tips</a></li>
                <li><a href="/category/pop-culture/">Pop Culture</a></li>
            </ul>
        </div>
    </nav>
    
    <main>
        <div class="container">
            <h1>Contact Us</h1>
            
            <p>Have questions, suggestions, or want to pitch a story? We'd love to hear from you!</p>
            
            <h2>Email</h2>
            <p>For general inquiries: <a href="mailto:hello@trendspotter-daily.com">hello@trendspotter-daily.com</a></p>
            <p>For business inquiries: <a href="mailto:business@trendspotter-daily.com">business@trendspotter-daily.com</a></p>
            
            <h2>Social Media</h2>
            <p>Follow us on social media for the latest updates:</p>
            <ul>
                <li>Twitter: <a href="https://twitter.com/trendspotterdaily">@trendspotterdaily</a></li>
                <li>Instagram: <a href="https://instagram.com/trendspotterdaily">@trendspotterdaily</a></li>
                <li>Facebook: <a href="https://facebook.com/trendspotterdaily">TrendSpotter Daily</a></li>
            </ul>
            
            <h2>Newsletter</h2>
            <p>Subscribe to our newsletter for exclusive content and early access to trending stories!</p>
        </div>
    </main>
    
    <footer>
        <div class="container">
            <p>&copy; 2026 TrendSpotter Daily. All rights reserved.</p>
            <p>
                <a href="/privacy-policy/">Privacy Policy</a> | 
                <a href="/terms-of-service/">Terms of Service</a> | 
                <a href="/contact/">Contact</a> | 
                <a href="/affiliate-disclosure/">Affiliate Disclosure</a>
            </p>
        </div>
    </footer>
    
    <script src="/js/main.js"></script>
</body>
</html>
EOF

echo -e "${GREEN}Static pages created successfully${NC}"

# Run content generator to populate with content
echo -e "${YELLOW}Generating initial viral content...${NC}"
cd $SOURCE_DIR
python3 content_generator.py

# Copy generated content to build directory
cp -r $SOURCE_DIR/posts $BUILD_DIR/ 2>/dev/null || echo "No posts directory yet, will be created"

# Copy generated index page and other files
cp $SOURCE_DIR/index.html $BUILD_DIR/ 2>/dev/null || echo "No index.html generated yet"
cp $SOURCE_DIR/sitemap.xml $BUILD_DIR/ 2>/dev/null || echo "No sitemap.xml generated yet"
cp $SOURCE_DIR/feed.rss $BUILD_DIR/ 2>/dev/null || echo "No feed.rss generated yet"

echo -e "${GREEN}Initial viral content generated${NC}"

# Set up cron job for automatic content generation
(crontab -l 2>/dev/null; echo "0 8,14,20 * * * cd $SOURCE_DIR && python3 content_generator.py") | crontab -

echo -e "${GREEN}Cron job set up for viral content generation at 8 AM, 2 PM, and 8 PM${NC}"

echo -e "${GREEN}Deployment complete!${NC}"
echo -e "${YELLOW}Next steps:${NC}"
echo -e "1. Customize the site name and identity in the templates"
echo -e "2. Add your Google Analytics ID (replace G-VIRALADS123)"
echo -e "3. Add your affiliate program IDs"
echo -e "4. Deploy the contents of $BUILD_DIR to your web server"
echo -e "5. Verify your domain with Google Search Console"