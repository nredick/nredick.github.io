// Custom Table of Contents highlighting using Intersection Observer
document.addEventListener('DOMContentLoaded', function() {
    const toc = document.querySelector('#TableOfContents');
    if (!toc) {
        console.log('TOC element not found');
        return;
    }

    const tocLinks = toc.querySelectorAll('a[href^="#"]');
    
    // Look for Blowfish anchor elements (div.anchor with id) and their parent headings
    const anchors = document.querySelectorAll('.anchor[id]');
    const headings = Array.from(anchors).map(anchor => anchor.parentElement);
    
    console.log('Found TOC links:', tocLinks.length);
    console.log('Found anchor elements:', anchors.length);
    console.log('Found headings:', headings.length);
    
    if (tocLinks.length === 0 || anchors.length === 0) {
        return;
    }

    // Create a map of heading IDs to their TOC links
    const linkMap = new Map();
    tocLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href.startsWith('#')) {
            const id = href.substring(1);
            linkMap.set(id, link);
        }
    });

    let currentActiveId = null;

    function setActiveLink(id) {
        if (currentActiveId === id) return;
        
        // Remove active class from all links
        tocLinks.forEach(link => link.classList.remove('active'));
        
        // Add active class to current link
        const activeLink = linkMap.get(id);
        if (activeLink) {
            activeLink.classList.add('active');
            currentActiveId = id;
            console.log('Activated section:', id);
        }
    }

    // Use Intersection Observer for more reliable detection
    const observerOptions = {
        rootMargin: '-20% 0px -70% 0px', // Only trigger when heading is in the top 20-30% of viewport
        threshold: 0
    };

    const observer = new IntersectionObserver((entries) => {
        // Find the first heading that's intersecting (visible in the trigger zone)
        const visibleEntries = entries.filter(entry => entry.isIntersecting);
        
        if (visibleEntries.length > 0) {
            // Sort by position and take the topmost one
            visibleEntries.sort((a, b) => {
                return a.target.getBoundingClientRect().top - b.target.getBoundingClientRect().top;
            });
            
            const topHeading = visibleEntries[0].target;
            const anchor = topHeading.querySelector('.anchor[id]');
            if (anchor) {
                setActiveLink(anchor.id);
            }
        }
    }, observerOptions);

    // Observe all headings
    headings.forEach(heading => {
        if (heading) {
            observer.observe(heading);
        }
    });
});
