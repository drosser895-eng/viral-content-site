#!/usr/bin/env python3
"""
TrendSpotter Daily Content Generator
Creates viral content focused on trending topics, celebrity gossip, lifestyle tips, and popular culture
"""

import os
import random
import re
from datetime import datetime
from urllib.parse import quote

# Viral content categories
CATEGORIES = {
    "celebrity-gossip": {
        "name": "Celebrity Gossip",
        "description": "Breaking celebrity news, scandals, and entertainment buzz"
    },
    "viral-videos": {
        "name": "Viral Videos",
        "description": "Trending videos and social media sensations"
    },
    "lifestyle-hacks": {
        "name": "Lifestyle Hacks",
        "description": "Money-saving tips, beauty tricks, and life improvements"
    },
    "tech-gadgets": {
        "name": "Tech & Gadgets",
        "description": "Latest tech reviews and gadget recommendations"
    },
    "health-wellness": {
        "name": "Health Myths",
        "description": "Debunking health fads and wellness trends"
    },
    "money-saving": {
        "name": "Money-Saving Tips",
        "description": "Ways to cut costs and maximize savings"
    },
    "pop-culture": {
        "name": "Pop Culture",
        "description": "Trends, memes, and cultural phenomena"
    }
}

# Affiliate product categories for revenue
AFFILIATE_PRODUCTS = {
    "beauty-products": [
        {"name": "Trending Beauty Gadget", "description": "Viral beauty tool everyone's talking about", "price": "$29.99", "rating": "4.8/5", "url": "#"},
        {"name": "Celebrity-Endorsed Skincare", "description": "The skincare routine stars swear by", "price": "$49.99", "rating": "4.7/5", "url": "#"}
    ],
    "tech-gadgets": [
        {"name": "Viral Phone Accessory", "description": "The phone accessory that went viral on TikTok", "price": "$39.99", "rating": "4.6/5", "url": "#"},
        {"name": "Smart Home Device", "description": "The smart device that makes life easier", "price": "$89.99", "rating": "4.5/5", "url": "#"}
    ],
    "lifestyle": [
        {"name": "Life-Changing Organizer", "description": "The storage solution that transforms homes", "price": "$24.99", "rating": "4.9/5", "url": "#"},
        {"name": "Kitchen Gadget", "description": "The kitchen tool that makes cooking easier", "price": "$34.99", "rating": "4.7/5", "url": "#"}
    ],
    "health-fitness": [
        {"name": "Fitness Trend", "description": "The workout trend celebrities love", "price": "$44.99", "rating": "4.4/5", "url": "#"},
        {"name": "Wellness Supplement", "description": "The supplement everyone's trying", "price": "$39.99", "rating": "4.6/5", "url": "#"}
    ]
}

# Viral content templates
ARTICLE_TEMPLATES = [
    {
        "title": "You Won't Believe What {celebrity} Just Did With Their Net Worth!",
        "category": "celebrity-gossip",
        "hook": "The world was shocked when {celebrity} made an unexpected decision about their massive fortune. The move has sparked controversy and debate across social media platforms.",
        "analysis": "This surprising decision breaks from typical celebrity financial behavior. Industry experts are divided on whether this is a savvy move or a risky gamble. The implications could affect other celebrities' approaches to wealth management.",
        "trends": "This story ties into larger trends about celebrity philanthropy and changing attitudes toward wealth in the digital age. More stars are choosing unconventional paths with their money, reflecting shifting cultural values.",
        "impact": "The ripple effects of this decision extend beyond just one celebrity. It could influence how other high-profile individuals approach their finances and charitable giving.",
        "takeaway": "This situation shows that even the wealthy face complex decisions about their money. It's a fascinating case study in celebrity culture and financial planning.",
        "actions": [
            "Follow the ongoing story as it develops",
            "Share your opinion on social media",
            "Research more about celebrity financial strategies",
            "Consider your own financial decisions",
            "Watch for reactions from other celebrities",
            "Look for similar patterns in other industries"
        ],
        "sources": [
            {"title": "Entertainment Weekly Report", "url": "https://example.com", "date": "2024-01-15"},
            {"title": "Financial Times Celebrity Wealth Study", "url": "https://example.com", "date": "2024-02-01"}
        ]
    },
    {
        "title": "The {gadget} That Went Viral on TikTok: Is It Worth the Hype?",
        "category": "tech-gadgets",
        "hook": "Social media has been buzzing about the {gadget}, but does it actually live up to its viral reputation? We tested it out to find the truth.",
        "analysis": "After extensive testing, we found that the {gadget} delivers on some promises but falls short on others. The marketing has definitely outpaced the actual functionality in several areas.",
        "trends": "This product exemplifies the growing trend of social media-driven purchases. Consumers are increasingly influenced by viral content when making buying decisions.",
        "impact": "The success of this product has inspired dozens of copycats and alternatives. It's become a case study in viral marketing effectiveness.",
        "takeaway": "While the {gadget} has merit, buyers should be aware of its limitations. It's perfect for certain use cases but overhyped for others.",
        "actions": [
            "Watch video reviews before purchasing",
            "Compare with similar products",
            "Look for discount codes online",
            "Read customer reviews carefully",
            "Wait for sales before buying",
            "Check return policies before ordering"
        ],
        "sources": [
            {"title": "Tech Review Roundup", "url": "https://example.com", "date": "2024-01-20"},
            {"title": "Consumer Reports Analysis", "url": "https://example.com", "date": "2024-02-05"}
        ]
    },
    {
        "title": "The Simple {hack_type} Hack That Will Save You Hours Each Week",
        "category": "lifestyle-hacks",
        "hook": "You've probably heard whispers about this simple {hack_type} trick, but does it actually work? We tried it for a week to see if it could revolutionize our daily routine.",
        "analysis": "The hack proved surprisingly effective for our test group. Most participants reported significant time savings and increased productivity. The simplicity of the method makes it accessible to almost anyone.",
        "trends": "This hack fits into the broader 'life optimization' trend that's sweeping social media. People are constantly seeking ways to improve efficiency and save time.",
        "impact": "Beyond just time savings, this hack could have significant impacts on stress levels and work-life balance. Small changes can lead to substantial improvements.",
        "takeaway": "Sometimes the simplest solutions are the most effective. This hack proves that innovation doesn't have to be complicated to be valuable.",
        "actions": [
            "Try the hack for yourself this week",
            "Document your time savings",
            "Share your results with friends",
            "Look for similar optimizations",
            "Combine with other productivity tips",
            "Teach it to family members"
        ],
        "sources": [
            {"title": "Productivity Research Study", "url": "https://example.com", "date": "2024-01-25"},
            {"title": "Time Management Experts Survey", "url": "https://example.com", "date": "2024-02-10"}
        ]
    }
]

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def generate_celebrity():
    """Generate a random celebrity for content"""
    celebrities = [
        "Taylor Swift", "Drake", "Beyoncé", "Kim Kardashian", "Ryan Reynolds",
        "Blake Lively", "Brad Pitt", "Angelina Jolie", "Justin Bieber", "Selena Gomez",
        "Ariana Grande", "Dwayne Johnson", "Chris Evans", "Scarlett Johansson",
        "Leonardo DiCaprio", "Margot Robbie", "Tom Holland", "Zendaya", "BTS",
        "Bad Bunny", "Harry Styles", "Emma Watson", "Chris Hemsworth", "Gal Gadot"
    ]
    return random.choice(celebrities)

def generate_gadget():
    """Generate a random gadget for content"""
    gadgets = [
        "Miracle Kitchen Gadget", "Revolutionary Phone Charger", "Game-Changing Fitness Tracker",
        "Innovative Smart Mirror", "Life-Changing Air Fryer", "Breakthrough Sleep Device",
        "Viral Phone Case", "Trending Coffee Maker", "Popular Streaming Device", 
        "Must-Have Wireless Earbuds", "TikTok-Famous Car Accessory", "Instagram-Worthy Blender"
    ]
    return random.choice(gadgets)

def generate_hack_type():
    """Generate a random hack type for content"""
    hack_types = [
        "Organization", "Cleaning", "Beauty", "Cooking", "Productivity", 
        "Finance", "Fitness", "Relationship", "Career", "Travel"
    ]
    return random.choice(hack_types)

def generate_article(topic=None):
    """Generate a complete viral article based on templates"""
    if topic:
        # Use provided topic if available
        template = topic
    else:
        # Select random template
        template = random.choice(ARTICLE_TEMPLATES)
    
    # Fill in template variables
    title = template['title'].format(
        celebrity=generate_celebrity(),
        gadget=generate_gadget(),
        hack_type=generate_hack_type()
    )
    
    hook = template['hook'].format(
        celebrity=generate_celebrity(),
        gadget=generate_gadget(),
        hack_type=generate_hack_type()
    )
    
    analysis = template['analysis'].format(
        celebrity=generate_celebrity(),
        gadget=generate_gadget(),
        hack_type=generate_hack_type()
    )
    
    category_key = template['category']
    category_info = CATEGORIES[category_key]
    
    # Generate slug
    slug = slugify(title)
    
    # Generate meta description
    meta_description = f"{hook[:100]}... Breaking news and viral content about {category_info['description'].lower()}"
    
    # Select random affiliate products for this post
    affiliate_category = random.choice(list(AFFILIATE_PRODUCTS.keys()))
    selected_affiliates = random.sample(AFFILIATE_PRODUCTS[affiliate_category], min(3, len(AFFILIATE_PRODUCTS[affiliate_category])))
    
    article = {
        "title": title,
        "slug": slug,
        "meta_description": meta_description,
        "date": datetime.now().strftime("%B %d, %Y"),
        "category": category_key,
        "category_name": category_info["name"],
        "hook": hook,
        "analysis": analysis,
        "trends": template["trends"].format(
            celebrity=generate_celebrity(),
            gadget=generate_gadget(),
            hack_type=generate_hack_type()
        ),
        "impact": template["impact"].format(
            celebrity=generate_celebrity(),
            gadget=generate_gadget(),
            hack_type=generate_hack_type()
        ),
        "takeaway": template["takeaway"].format(
            celebrity=generate_celebrity(),
            gadget=generate_gadget(),
            hack_type=generate_hack_type()
        ),
        "actions": template["actions"],
        "sources": template["sources"],
        "affiliate_products": selected_affiliates,
        "related_posts": []  # Will be populated later
    }
    
    return article

def save_article_to_file(article, base_dir="posts"):
    """Save the generated article as an HTML file"""
    os.makedirs(os.path.join(base_dir, article['category']), exist_ok=True)
    
    # Read the post template
    with open('templates/post.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Format the content
    content_html = f"""
    <article class="content-section">
        <h1>{article['title']}</h1>
        <div class="date">{article['date']}</div>
        <span class="category-tag">{article['category_name']}</span>
        
        <div class="hook">
            {article['hook']}
        </div>
        
        <h2 class="section-title">The Full Story</h2>
        <div class="thematic-analysis">
            <p>{article['analysis']}</p>
        </div>
        
        <h2 class="section-title">Trending Now</h2>
        <div class="storytelling-insights">
            <p>{article['trends']}</p>
        </div>
        
        <h2 class="section-title">Why This Matters</h2>
        <div class="production-breakdown">
            <p>{article['impact']}</p>
        </div>
        
        <h2 class="section-title">Bottom Line</h2>
        <div class="listener-takeaway">
            <p>{article['takeaway']}</p>
            <h3>What You Should Do Next:</h3>
            <ul class="actions-list">
                {''.join([f'<li>{action}</li>' for action in article['actions']])}
            </ul>
        </div>
        
        <div class="affiliate-disclaimer">
            <strong>Featured Products:</strong> Some links in this post are affiliate links. If you purchase through these links, we may earn a small commission at no extra cost to you. This helps support our content creation.
            <div style="margin-top: 1rem;">
                <h3>Related Products You Might Like:</h3>
                <div class="product-grid">
                    {''.join([f'''
                    <div class="product-card">
                        <h4>{prod["name"]}</h4>
                        <p>{prod["description"]}</p>
                        <p class="price">{prod["price"]} • Rating: {prod["rating"]}</p>
                        <a href="{prod["url"]}" class="btn">Check Price</a>
                    </div>
                    ''' for prod in article['affiliate_products']])}
                </div>
            </div>
        </div>
        
        <h2 class="section-title">Sources & References</h2>
        <div class="sources">
            <ul>
                {''.join([f'<li><a href="{source["url"]}">{source["title"]}</a> ({source["date"]})</li>' for source in article['sources']])}
            </ul>
        </div>
        
        <div class="related-posts">
            <h3>More Trending Content</h3>
            <p>Explore more articles in the <a href="/category/{article['category']}/">{article['category_name']}</a> category.</p>
        </div>
    </article>
    """
    
    # Replace template variables
    html_content = template.replace('{{TITLE}}', article['title'])
    html_content = html_content.replace('{{META_DESCRIPTION}}', article['meta_description'])
    html_content = html_content.replace('{{CONTENT}}', content_html)
    
    # Save the article
    filename = os.path.join(base_dir, article['category'], f"{article['slug']}.html")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return filename

def update_index_page(new_post=None):
    """Update the index page with the latest posts"""
    # Read index template
    with open('templates/index.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Get list of recent posts
    post_links = []
    
    for category in CATEGORIES:
        category_dir = os.path.join('posts', category)
        if os.path.exists(category_dir):
            posts = sorted(os.listdir(category_dir), reverse=True)[:5]  # Get 5 most recent from each category
            for post in posts[:3]:  # Take 3 from each category
                if post.endswith('.html'):
                    slug = post[:-5]  # Remove .html
                    # Need to extract title from the file
                    post_path = os.path.join(category_dir, post)
                    with open(post_path, 'r', encoding='utf-8') as pf:
                        content = pf.read()
                        # Extract title from the content
                        import re
                        title_match = re.search(r'<h1>(.*?)</h1>', content)
                        title = title_match.group(1) if title_match else slug.replace('-', ' ').title()
                    
                    post_links.append({
                        'title': title,
                        'url': f"/posts/{category}/{slug}/",
                        'date': datetime.now().strftime("%B %d, %Y"),
                        'category': CATEGORIES[category]['name']
                    })
    
    # Limit to 9 most recent posts
    post_links = post_links[:9]
    
    # Create HTML for post grid
    posts_html = ""
    for post in post_links:
        posts_html += f"""
        <div class="post-card">
            <span class="category-tag">{post['category']}</span>
            <h3><a href="{post['url']}">{post['title']}</a></h3>
            <div class="date">{post['date']}</div>
            <p>Trending content that's capturing attention...</p>
        </div>
        """
    
    # Replace in template
    html_content = template.replace('{{POSTS}}', posts_html)
    
    # Save index page
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

def generate_sitemap():
    """Generate sitemap.xml for SEO"""
    urls = [
        {"loc": "https://trendspotter-daily.com/", "lastmod": datetime.now().strftime("%Y-%m-%d"), "changefreq": "daily", "priority": "1.0"},
        {"loc": "https://trendspotter-daily.com/affiliate-disclosure/", "lastmod": datetime.now().strftime("%Y-%m-%d"), "changefreq": "monthly", "priority": "0.8"},
    ]
    
    # Add category pages
    for cat_key, cat_info in CATEGORIES.items():
        urls.append({
            "loc": f"https://trendspotter-daily.com/category/{cat_key}/",
            "lastmod": datetime.now().strftime("%Y-%m-%d"),
            "changefreq": "hourly",
            "priority": "0.9"
        })
    
    # Add posts
    for category in CATEGORIES:
        category_dir = os.path.join('posts', category)
        if os.path.exists(category_dir):
            posts = os.listdir(category_dir)
            for post in posts:
                if post.endswith('.html'):
                    slug = post[:-5]
                    urls.append({
                        "loc": f"https://trendspotter-daily.com/{category}/{slug}/",
                        "lastmod": datetime.now().strftime("%Y-%m-%d"),
                        "changefreq": "weekly",
                        "priority": "0.7"
                    })
    
    # Create sitemap XML
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for url in urls:
        sitemap_xml += f'  <url>\n'
        sitemap_xml += f'    <loc>{url["loc"]}</loc>\n'
        sitemap_xml += f'    <lastmod>{url["lastmod"]}</lastmod>\n'
        sitemap_xml += f'    <changefreq>{url["changefreq"]}</changefreq>\n'
        sitemap_xml += f'    <priority>{url["priority"]}</priority>\n'
        sitemap_xml += f'  </url>\n'
    
    sitemap_xml += '</urlset>'
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap_xml)

def generate_rss_feed():
    """Generate RSS feed for the site"""
    # This would typically pull from actual posts, but for now we'll create a template
    rss_content = '''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
  <title>TrendSpotter Daily</title>
  <link>https://trendspotter-daily.com</link>
  <description>Your Source for Viral News, Celebrity Gossip & Lifestyle Trends</description>
  <language>en-us</language>
  <pubDate>{pub_date}</pubDate>
  <lastBuildDate>{build_date}</lastBuildDate>
  <generator>Custom RSS Generator</generator>
</channel>
</rss>'''.format(
        pub_date=datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z"),
        build_date=datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")
    )
    
    with open('feed.rss', 'w', encoding='utf-8') as f:
        f.write(rss_content)

def main():
    """Generate a new viral article and update the site"""
    print("Generating new viral content article...")
    
    # Generate a new article
    article = generate_article()
    filename = save_article_to_file(article)
    
    print(f"Generated article: {filename}")
    
    # Update the index page
    update_index_page(article)
    print("Updated index page with new article")
    
    # Generate sitemap
    generate_sitemap()
    print("Generated sitemap.xml")
    
    # Generate RSS feed
    generate_rss_feed()
    print("Generated RSS feed")
    
    print("\nSite generation complete!")
    print("Files created:")
    print(f"- Article: {filename}")
    print("- Index page: index.html")
    print("- Sitemap: sitemap.xml")
    print("- RSS feed: feed.rss")

if __name__ == "__main__":
    main()