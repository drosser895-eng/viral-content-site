// TrendSpotter Daily - Viral Content Site Scripts

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all interactive elements
    initializeViralFeatures();
    setupSmoothScrolling();
    addStickyHeader();
    setupAnimations();
    addSocialSharing();
    addEnhancedVisualEffects();
});

function initializeViralFeatures() {
    // Add viral countdown timers for urgency
    addCountdownTimers();
    
    // Highlight trending articles
    highlightTrendingPosts();
    
    // Add pop-up notifications for new content
    setupNotifications();
}

function addCountdownTimers() {
    // Add countdown to create urgency around trending content
    const countdownElements = document.querySelectorAll('.countdown');
    countdownElements.forEach(element => {
        const endDate = new Date(element.dataset.endDate).getTime();
        
        const timer = setInterval(() => {
            const now = new Date().getTime();
            const distance = endDate - now;
            
            if (distance < 0) {
                clearInterval(timer);
                element.innerHTML = '<span class="expired">EXPIRED</span>';
                return;
            }
            
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);
            
            element.innerHTML = `${hours}h ${minutes}m ${seconds}s`;
            
            // Add urgency class when time is running low
            if (distance < 3600000) { // Less than 1 hour
                element.classList.add('urgent');
            }
        }, 1000);
    });
}

function highlightTrendingPosts() {
    // Add animation to trending posts
    const trendingPosts = document.querySelectorAll('.trending');
    trendingPosts.forEach(post => {
        // Add pulsing animation to make them stand out
        post.style.animation = 'pulse 2s infinite';
    });
}

function setupNotifications() {
    // Create subtle notifications for new content
    setTimeout(() => {
        createNotification('🔥 Hot new content just dropped!', 'New trending article available');
    }, 5000);
    
    // Additional notifications for high-engagement content
    setTimeout(() => {
        createNotification('🚨 Breaking: This story is going viral!', 'See what everyone is talking about');
    }, 15000);
}

function createNotification(title, message) {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = 'notification';
    notification.innerHTML = `
        <div class="notification-content">
            <div class="notification-icon">🔔</div>
            <div class="notification-text">
                <h4>${title}</h4>
                <p>${message}</p>
            </div>
            <button class="notification-close">&times;</button>
        </div>
    `;
    
    // Add close functionality
    const closeBtn = notification.querySelector('.notification-close');
    closeBtn.addEventListener('click', () => {
        notification.remove();
    });
    
    // Add click to view functionality
    notification.addEventListener('click', () => {
        // Redirect to trending content or handle as needed
        notification.remove();
    });
    
    // Add to page
    document.body.appendChild(notification);
    
    // Auto-remove after 10 seconds
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, 10000);
}

function setupSmoothScrolling() {
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

function addStickyHeader() {
    // Enhanced sticky header with scroll detection
    let lastScrollTop = 0;
    const header = document.querySelector('header');
    
    window.addEventListener('scroll', () => {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > lastScrollTop && scrollTop > 100) {
            // Scrolling down - hide header slightly
            header.style.transform = 'translateY(-10px)';
        } else {
            // Scrolling up - show header
            header.style.transform = 'translateY(0)';
        }
        
        lastScrollTop = scrollTop;
    });
}

function setupAnimations() {
    // Intersection Observer for scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
                
                // Add staggered animations
                const elements = entry.target.querySelectorAll('.animate-on-scroll');
                elements.forEach((el, index) => {
                    setTimeout(() => {
                        el.style.opacity = '1';
                        el.style.transform = 'translateY(0)';
                    }, index * 100);
                });
            }
        });
    }, observerOptions);
    
    // Observe content sections
    document.querySelectorAll('.content-section, .post-card').forEach(section => {
        observer.observe(section);
    });
}

function addSocialSharing() {
    // Add dynamic social sharing functionality
    const shareButtons = document.querySelectorAll('.social-btn');
    shareButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const platform = this.dataset.platform;
            const url = encodeURIComponent(window.location.href);
            const title = encodeURIComponent(document.title);
            
            let shareUrl = '';
            
            switch(platform) {
                case 'facebook':
                    shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${url}`;
                    break;
                case 'twitter':
                    shareUrl = `https://twitter.com/intent/tweet?url=${url}&text=${title}`;
                    break;
                case 'reddit':
                    shareUrl = `https://www.reddit.com/submit?url=${url}&title=${title}`;
                    break;
                case 'linkedin':
                    shareUrl = `https://www.linkedin.com/shareArticle?mini=true&url=${url}&title=${title}`;
                    break;
            }
            
            if (shareUrl) {
                window.open(shareUrl, '_blank', 'width=600,height=400');
            }
        });
    });
    
    // Add copy link functionality
    const copyLinkBtn = document.createElement('button');
    copyLinkBtn.className = 'social-btn copy-link';
    copyLinkBtn.innerHTML = '🔗';
    copyLinkBtn.title = 'Copy Link';
    copyLinkBtn.addEventListener('click', copyCurrentUrl);
    
    const socialBar = document.querySelector('.social-share');
    if (socialBar) {
        socialBar.appendChild(copyLinkBtn);
    }
}

function copyCurrentUrl() {
    navigator.clipboard.writeText(window.location.href).then(() => {
        // Show feedback
        const feedback = document.createElement('div');
        feedback.textContent = 'Link copied!';
        feedback.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: #4CAF50;
            color: white;
            padding: 10px 15px;
            border-radius: 4px;
            z-index: 10000;
            animation: fadeInOut 3s ease;
        `;
        document.body.appendChild(feedback);
        
        setTimeout(() => {
            feedback.remove();
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy: ', err);
    });
}

// Additional viral content features
function addEngagementFeatures() {
    // Add reading progress indicator
    const progressBar = document.createElement('div');
    progressBar.id = 'reading-progress';
    progressBar.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 0%;
        height: 4px;
        background: linear-gradient(90deg, #FF6B35, #F7931E);
        z-index: 9999;
        transition: width 0.1s ease;
    `;
    document.body.appendChild(progressBar);
    
    window.addEventListener('scroll', () => {
        const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (winScroll / height) * 100;
        progressBar.style.width = scrolled + "%";
    });
    
    // Add floating "Share" button for mobile
    if (window.innerWidth <= 768) {
        const floatingShare = document.createElement('div');
        floatingShare.id = 'floating-share';
        floatingShare.innerHTML = '📱 Share';
        floatingShare.style.cssText = `
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: #FF6B35;
            color: white;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            cursor: pointer;
            z-index: 9998;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            font-size: 12px;
        `;
        floatingShare.addEventListener('click', () => {
            if (navigator.share) {
                navigator.share({
                    title: document.title,
                    url: window.location.href
                });
            } else {
                copyCurrentUrl();
            }
        });
        document.body.appendChild(floatingShare);
    }
}

// Enhanced visual effects
function addEnhancedVisualEffects() {
    // Add hover effects to all links
    const links = document.querySelectorAll('a');
    links.forEach(link => {
        link.addEventListener('mouseenter', function() {
            this.style.transition = 'all 0.3s ease';
            this.style.textShadow = '0 0 8px rgba(255, 107, 53, 0.5)';
        });
        
        link.addEventListener('mouseleave', function() {
            this.style.textShadow = 'none';
        });
    });
    
    // Add parallax effect to header
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const rate = scrolled * -0.5;
        const header = document.querySelector('header');
        if (header) {
            header.style.backgroundPosition = `center ${rate}px`;
        }
    });
    
    // Add image lazy loading with fade-in effect
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                img.classList.add('loaded');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
    
    // Add scroll-triggered animations to text elements
    const textElements = document.querySelectorAll('p, h2, h3, .category-tag, .date');
    const textObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                entry.target.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                textObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });
    
    textElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        textObserver.observe(el);
    });
}

// Initialize additional features after DOM content loads
setTimeout(addEngagementFeatures, 1000);

// Add viral content tracking
function trackEngagement() {
    // Track scroll depth
    let scrollDepth = 0;
    window.addEventListener('scroll', () => {
        const currentScroll = (window.scrollY + window.innerHeight) / document.body.offsetHeight;
        if (currentScroll > scrollDepth) {
            scrollDepth = currentScroll;
            // Could send to analytics here
        }
    });
    
    // Track time on page
    const startTime = Date.now();
    window.addEventListener('beforeunload', () => {
        const timeSpent = Date.now() - startTime;
        // Could send to analytics here
    });
}

// Initialize engagement tracking
trackEngagement();

// Add keyboard shortcuts for power users
document.addEventListener('keydown', (e) => {
    if (e.ctrlKey || e.metaKey) {
        switch(e.key) {
            case 'ArrowLeft':
                e.preventDefault();
                history.back();
                break;
            case 'ArrowRight':
                e.preventDefault();
                history.forward();
                break;
        }
    }
});

// Add dynamic content loading indicators
function addLoadingIndicators() {
    const contentSections = document.querySelectorAll('.content-section');
    contentSections.forEach(section => {
        // Add shimmer effect while content loads
        const shimmerDiv = document.createElement('div');
        shimmerDiv.className = 'shimmer';
        shimmerDiv.style.cssText = `
            height: 20px;
            margin: 10px 0;
            border-radius: 4px;
        `;
        section.appendChild(shimmerDiv);
        
        // Remove after content loads
        setTimeout(() => {
            shimmerDiv.remove();
        }, 1000);
    });
}

// Initialize loading indicators
addLoadingIndicators();