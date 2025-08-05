"""
Google Search Operators Configuration
Comprehensive list of Google search operators with their descriptions and usage examples.
"""

SEARCH_OPERATORS = {
    "site:": {
        "description": "Search within a specific website or domain",
        "type": "url",
        "placeholder": "example.com",
        "examples": ["site:reddit.com python tutorials", "site:github.com machine learning"]
    },
    "filetype:": {
        "description": "Search for specific file types",
        "type": "keyword",
        "placeholder": "pdf machine learning",
        "examples": ["filetype:pdf machine learning", "filetype:ppt presentation tips"]
    },
    "intitle:": {
        "description": "Search for pages with specific words in the title",
        "type": "keyword",
        "placeholder": "python tutorial",
        "examples": ["intitle:python tutorial", "intitle:\"data science\""]
    },
    "allintitle:": {
        "description": "Search for pages with all specified words in the title",
        "type": "keyword",
        "placeholder": "python machine learning tutorial",
        "examples": ["allintitle:python machine learning", "allintitle:web development guide"]
    },
    "inurl:": {
        "description": "Search for pages with specific words in the URL",
        "type": "keyword",
        "placeholder": "tutorial",
        "examples": ["inurl:tutorial python", "inurl:blog machine learning"]
    },
    "allinurl:": {
        "description": "Search for pages with all specified words in the URL",
        "type": "keyword",
        "placeholder": "python tutorial",
        "examples": ["allinurl:python tutorial", "allinurl:web development"]
    },
    "intext:": {
        "description": "Search for pages with specific words in the body text",
        "type": "keyword",
        "placeholder": "machine learning",
        "examples": ["intext:machine learning", "intext:\"data science\""]
    },
    "allintext:": {
        "description": "Search for pages with all specified words in the body text",
        "type": "keyword",
        "placeholder": "python programming tutorial",
        "examples": ["allintext:python programming", "allintext:web development guide"]
    },
    "related:": {
        "description": "Find websites related to a specific URL",
        "type": "url",
        "placeholder": "example.com",
        "examples": ["related:stackoverflow.com", "related:github.com"]
    },
    "cache:": {
        "description": "View Google's cached version of a webpage",
        "type": "url",
        "placeholder": "example.com",
        "examples": ["cache:example.com", "cache:stackoverflow.com/questions/123"]
    },
    "link:": {
        "description": "Find pages that link to a specific URL",
        "type": "url",
        "placeholder": "example.com",
        "examples": ["link:stackoverflow.com", "link:github.com"]
    },
    "define:": {
        "description": "Get definitions for words or phrases",
        "type": "keyword",
        "placeholder": "artificial intelligence",
        "examples": ["define:machine learning", "define:cryptocurrency"]
    },
    "stocks:": {
        "description": "Get stock information for a company",
        "type": "keyword",
        "placeholder": "AAPL",
        "examples": ["stocks:AAPL", "stocks:GOOGL"]
    },
    "weather:": {
        "description": "Get weather information for a location",
        "type": "keyword",
        "placeholder": "New York",
        "examples": ["weather:New York", "weather:London"]
    },
    "map:": {
        "description": "Show map results for a location",
        "type": "keyword",
        "placeholder": "restaurants New York",
        "examples": ["map:restaurants New York", "map:hotels Paris"]
    },
    "movie:": {
        "description": "Search for movie information and showtimes",
        "type": "keyword",
        "placeholder": "Inception",
        "examples": ["movie:Inception", "movie:Avengers"]
    },
    "source:": {
        "description": "Search Google News for articles from a specific source",
        "type": "keyword",
        "placeholder": "CNN",
        "examples": ["source:CNN climate change", "source:BBC technology"]
    },
    "before:": {
        "description": "Search for content published before a specific date",
        "type": "keyword",
        "placeholder": "2020 machine learning",
        "examples": ["before:2020-01-01 machine learning", "before:2019 cryptocurrency"]
    },
    "after:": {
        "description": "Search for content published after a specific date",
        "type": "keyword",
        "placeholder": "2020 AI trends",
        "examples": ["after:2020-01-01 AI trends", "after:2021 web development"]
    },
    "daterange:": {
        "description": "Search for content within a specific date range",
        "type": "keyword",
        "placeholder": "machine learning trends",
        "examples": ["daterange:2020-2021 machine learning", "daterange:2019-2020 startup"]
    },
    "info:": {
        "description": "Get information about a specific URL",
        "type": "url",
        "placeholder": "example.com",
        "examples": ["info:stackoverflow.com", "info:github.com"]
    },
    "phonebook:": {
        "description": "Search for phone numbers (limited availability)",
        "type": "keyword",
        "placeholder": "John Smith New York",
        "examples": ["phonebook:John Smith", "phonebook:business name city"]
    },
    "bphonebook:": {
        "description": "Search for business phone numbers",
        "type": "keyword",
        "placeholder": "pizza New York",
        "examples": ["bphonebook:pizza New York", "bphonebook:dentist Chicago"]
    },
    "author:": {
        "description": "Search for articles by a specific author in Google Scholar",
        "type": "keyword",
        "placeholder": "John Smith",
        "examples": ["author:\"John Smith\" machine learning", "author:Einstein physics"]
    },
    "group:": {
        "description": "Search within Google Groups",
        "type": "keyword",
        "placeholder": "python programming",
        "examples": ["group:comp.lang.python", "group:alt.comp.programming"]
    },
    "inanchor:": {
        "description": "Search for pages with specific anchor text in links",
        "type": "keyword",
        "placeholder": "click here",
        "examples": ["inanchor:\"click here\"", "inanchor:download"]
    },
    "allinanchor:": {
        "description": "Search for pages with all specified words in anchor text",
        "type": "keyword",
        "placeholder": "download free software",
        "examples": ["allinanchor:download free", "allinanchor:learn python"]
    },
    "around(X):": {
        "description": "Search for pages where two terms appear within X words of each other",
        "type": "keyword",
        "placeholder": "python AROUND(5) tutorial",
        "examples": ["python AROUND(10) machine learning", "climate AROUND(3) change"]
    },
    "loc:": {
        "description": "Search for results from a specific location",
        "type": "keyword",
        "placeholder": "restaurants loc:\"New York\"",
        "examples": ["restaurants loc:\"New York\"", "events loc:\"San Francisco\""]
    },
    "location:": {
        "description": "Search for news from a specific location",
        "type": "keyword",
        "placeholder": "news location:\"California\"",
        "examples": ["news location:\"California\"", "weather location:\"London\""]
    },
    # Advanced SEO Operators
    "AROUND(X):": {
        "description": "Find pages where two terms appear within X words of each other",
        "type": "keyword", 
        "placeholder": "SEO AROUND(5) optimization",
        "examples": ["digital AROUND(3) marketing", "content AROUND(10) strategy"]
    },
    "\"\"": {
        "description": "Exact phrase search - find pages with the exact phrase",
        "type": "keyword",
        "placeholder": "\"digital marketing strategy\"",
        "examples": ["\"content marketing\"", "\"SEO best practices\""]
    },
    "*": {
        "description": "Wildcard operator - placeholder for unknown words",
        "type": "keyword", 
        "placeholder": "best * for SEO",
        "examples": ["best * for marketing", "how to * website traffic"]
    },
    "OR": {
        "description": "Search for pages containing either term",
        "type": "keyword",
        "placeholder": "SEO OR SEM",
        "examples": ["marketing OR advertising", "python OR javascript"]
    },
    "-": {
        "description": "Exclude terms from search results",
        "type": "keyword",
        "placeholder": "digital marketing -ads",
        "examples": ["python tutorials -paid", "SEO guide -2019"]
    },
    "+": {
        "description": "Include specific terms in search results",
        "type": "keyword",
        "placeholder": "+SEO +optimization",
        "examples": ["+digital +marketing tips", "+content +strategy"]
    },
    "~": {
        "description": "Search for synonyms and related terms",
        "type": "keyword",
        "placeholder": "~car information",
        "examples": ["~digital marketing", "~website optimization"]
    },
    "..": {
        "description": "Search within number ranges",
        "type": "keyword",
        "placeholder": "smartphones $200..$500",
        "examples": ["laptops $500..$1000", "camera 2020..2023"]
    },
    "imagesize:": {
        "description": "Find images of specific dimensions",
        "type": "keyword",
        "placeholder": "imagesize:1920x1080",
        "examples": ["imagesize:800x600 wallpaper", "imagesize:1024x768 screenshot"]
    },
    "safesearch:": {
        "description": "Control safe search filtering",
        "type": "keyword",
        "placeholder": "safesearch:off",
        "examples": ["safesearch:on family content", "safesearch:off research"]
    },
    "blogurl:": {
        "description": "Search within blog URLs",
        "type": "url",
        "placeholder": "blogurl:medium.com",
        "examples": ["blogurl:wordpress.com SEO", "blogurl:blogger.com marketing"]
    },
    "haschange:": {
        "description": "Find pages that have changed recently",
        "type": "keyword",
        "placeholder": "haschange:speed",
        "examples": ["haschange:update website", "haschange:new product launch"]
    },
    "inposttitle:": {
        "description": "Search within blog post titles",
        "type": "keyword",
        "placeholder": "inposttitle:SEO tips",
        "examples": ["inposttitle:marketing strategy", "inposttitle:web development"]
    },
    "inpostauthor:": {
        "description": "Search by blog post author",
        "type": "keyword",
        "placeholder": "inpostauthor:\"John Smith\"",
        "examples": ["inpostauthor:\"Neil Patel\"", "inpostauthor:\"Rand Fishkin\""]
    },
    "allintitle:": {
        "description": "All specified words must appear in title",
        "type": "keyword",
        "placeholder": "allintitle:SEO guide 2024",
        "examples": ["allintitle:digital marketing strategy", "allintitle:web development tutorial"]
    },
    "id:": {
        "description": "Search for specific page or post ID",
        "type": "keyword",
        "placeholder": "id:12345",
        "examples": ["id:wordpress-123", "id:blog-post-456"]
    }
}

def get_operator_info(operator_name):
    """
    Get detailed information about a specific search operator.
    
    Args:
        operator_name (str): The name of the search operator
        
    Returns:
        dict: Information about the operator including description, type, and examples
    """
    return SEARCH_OPERATORS.get(operator_name, {
        "description": "Unknown operator",
        "type": "keyword",
        "placeholder": "search term",
        "examples": []
    })

def get_operators_by_type(operator_type):
    """
    Get all operators of a specific type.
    
    Args:
        operator_type (str): Either 'url' or 'keyword'
        
    Returns:
        dict: Dictionary of operators matching the specified type
    """
    return {
        name: info for name, info in SEARCH_OPERATORS.items()
        if info.get('type') == operator_type
    }

def get_operator_categories():
    """
    Get operators organized by categories for better UI organization.
    
    Returns:
        dict: Operators organized by functional categories
    """
    categories = {
        "🌐 Site & Domain": ["site:", "related:", "info:", "cache:", "link:", "blogurl:"],
        "📄 Content & Files": ["filetype:", "define:", "imagesize:", "haschange:"],
        "🔍 Page Elements": ["intitle:", "allintitle:", "inurl:", "allinurl:", "intext:", "allintext:", "inposttitle:", "inpostauthor:"],
        "📅 Time-based": ["before:", "after:", "daterange:"],
        "📰 News & Sources": ["source:", "location:"],
        "🎯 SEO Advanced": ["AROUND(X):", "\"\"", "*", "OR", "-", "+", "~", "..", "inanchor:", "allinanchor:"],
        "📊 Special Searches": ["stocks:", "weather:", "map:", "movie:", "safesearch:", "id:"],
        "👥 People & Contact": ["phonebook:", "bphonebook:", "author:", "group:"],
        "📍 Location": ["loc:", "location:"]
    }
    return categories
