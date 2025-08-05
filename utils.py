"""
Utility functions for the Google Search Operators Tool
"""

import json
import os
import re
import urllib.parse
from typing import List, Dict, Any, Optional

# File paths for persistent storage
HISTORY_FILE = "search_history.json"
FAVORITES_FILE = "favorites.json"

def load_search_history() -> List[Dict[str, Any]]:
    """
    Load search history from JSON file.
    
    Returns:
        List[Dict]: List of search history entries
    """
    try:
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading search history: {e}")
    return []

def save_search_history(history: List[Dict[str, Any]]) -> None:
    """
    Save search history to JSON file.
    
    Args:
        history (List[Dict]): List of search history entries
    """
    try:
        # Keep only the last 1000 entries to prevent file from getting too large
        history = history[-1000:] if len(history) > 1000 else history
        
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"Error saving search history: {e}")

def load_favorites() -> List[Dict[str, Any]]:
    """
    Load favorites from JSON file.
    
    Returns:
        List[Dict]: List of favorite search entries
    """
    try:
        if os.path.exists(FAVORITES_FILE):
            with open(FAVORITES_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading favorites: {e}")
    return []

def save_favorites(favorites: List[Dict[str, Any]]) -> None:
    """
    Save favorites to JSON file.
    
    Args:
        favorites (List[Dict]): List of favorite search entries
    """
    try:
        with open(FAVORITES_FILE, 'w', encoding='utf-8') as f:
            json.dump(favorites, f, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"Error saving favorites: {e}")

def validate_url(url: str) -> bool:
    """
    Validate if a string is a valid URL or domain.
    
    Args:
        url (str): URL or domain to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not url or not isinstance(url, str):
        return False
    
    url = url.strip()
    
    # Check for basic domain pattern
    domain_pattern = r'^[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*$'
    
    # Remove protocol if present
    if url.startswith(('http://', 'https://')):
        url = url.split('://', 1)[1]
    
    # Remove path if present
    url = url.split('/')[0]
    
    # Check if it matches domain pattern
    return bool(re.match(domain_pattern, url)) and len(url) <= 253

def validate_keyword(keyword: str) -> bool:
    """
    Validate if a string is a valid search keyword.
    
    Args:
        keyword (str): Keyword to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not keyword or not isinstance(keyword, str):
        return False
    
    keyword = keyword.strip()
    
    # Basic validation - not empty and reasonable length
    return len(keyword) > 0 and len(keyword) <= 500

def build_search_url(operator: str, search_term: str, additional_params: Optional[Dict[str, Any]] = None) -> str:
    """
    Build a Google search URL with the specified operator and search term.
    
    Args:
        operator (str): The search operator to use
        search_term (str): The search term or URL
        additional_params (Optional[Dict]): Additional parameters for the search
        
    Returns:
        str: Complete Google search URL
    """
    # Clean the search term
    search_term = search_term.strip()
    
    # Handle special operators that need specific formatting
    if operator in ["before:", "after:"]:
        if additional_params and 'date' in additional_params:
            query = f"{operator}{additional_params['date']} {search_term}"
        else:
            query = f"{operator}2020-01-01 {search_term}"
    elif operator == "daterange:":
        if additional_params and 'date' in additional_params:
            # For daterange, we'll use a simple year-based range
            year = additional_params['date'][:4]
            query = f"after:{year}-01-01 before:{year}-12-31 {search_term}"
        else:
            query = f"after:2020-01-01 before:2021-12-31 {search_term}"
    elif operator == "around(X):":
        # Replace X with a default value if not specified
        if "AROUND(" not in search_term.upper():
            # Assume the format is "term1 AROUND(5) term2"
            parts = search_term.split()
            if len(parts) >= 2:
                query = f"{parts[0]} AROUND(5) {' '.join(parts[1:])}"
            else:
                query = f"{search_term} AROUND(5) related"
        else:
            query = search_term
    elif operator.endswith(":"):
        # Standard operator format
        if operator in ["site:", "related:", "cache:", "link:", "info:"]:
            # These operators work better without quotes around URLs
            query = f"{operator}{search_term}"
        else:
            # For keyword-based operators, we might want to quote multi-word terms
            if " " in search_term and not (search_term.startswith('"') and search_term.endswith('"')):
                query = f"{operator}\"{search_term}\""
            else:
                query = f"{operator}{search_term}"
    else:
        # Fallback for operators without colons
        query = f"{operator} {search_term}"
    
    # URL encode the query
    encoded_query = urllib.parse.quote_plus(query)
    
    # Build the complete Google search URL with 100 results
    search_url = f"https://www.google.com/search?q={encoded_query}&num=100"
    
    return search_url

def format_search_query_for_display(operator: str, search_term: str) -> str:
    """
    Format a search query for display purposes.
    
    Args:
        operator (str): The search operator
        search_term (str): The search term
        
    Returns:
        str: Formatted query string
    """
    if operator.endswith(":"):
        return f"{operator}{search_term}"
    else:
        return f"{operator} {search_term}"

def export_to_csv(data: List[Dict[str, Any]], filename: str) -> str:
    """
    Export data to CSV format.
    
    Args:
        data (List[Dict]): Data to export
        filename (str): Name of the file
        
    Returns:
        str: CSV content as string
    """
    import pandas as pd
    
    try:
        df = pd.DataFrame(data)
        return df.to_csv(index=False)
    except Exception as e:
        print(f"Error exporting to CSV: {e}")
        return ""

def clean_search_term(search_term: str) -> str:
    """
    Clean and normalize search terms.
    
    Args:
        search_term (str): Raw search term
        
    Returns:
        str: Cleaned search term
    """
    if not search_term:
        return ""
    
    # Remove extra whitespace
    search_term = ' '.join(search_term.split())
    
    # Remove potentially harmful characters
    harmful_chars = ['<', '>', '&', '"', "'"]
    for char in harmful_chars:
        search_term = search_term.replace(char, '')
    
    return search_term.strip()

def get_search_suggestions(operator: str) -> List[str]:
    """
    Get search suggestions based on the selected operator.
    
    Args:
        operator (str): Selected search operator
        
    Returns:
        List[str]: List of search suggestions
    """
    suggestions = {
        "site:": ["reddit.com", "stackoverflow.com", "github.com", "medium.com"],
        "filetype:": ["pdf", "doc", "ppt", "xls", "txt"],
        "intitle:": ["tutorial", "guide", "how to", "tips"],
        "inurl:": ["blog", "tutorial", "guide", "documentation"],
        "related:": ["google.com", "facebook.com", "twitter.com", "linkedin.com"],
        "define:": ["artificial intelligence", "machine learning", "blockchain", "cryptocurrency"],
        "stocks:": ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"],
        "weather:": ["New York", "London", "Tokyo", "Sydney"],
        "movie:": ["latest movies", "action movies", "comedy movies", "sci-fi movies"]
    }
    
    return suggestions.get(operator, [])

def validate_batch_input(batch_input: str) -> tuple:
    """
    Validate batch input and return cleaned queries.
    
    Args:
        batch_input (str): Raw batch input
        
    Returns:
        tuple: (is_valid, cleaned_queries, error_message)
    """
    if not batch_input or not batch_input.strip():
        return False, [], "Batch input cannot be empty"
    
    lines = [line.strip() for line in batch_input.split('\n') if line.strip()]
    
    if not lines:
        return False, [], "No valid queries found"
    
    if len(lines) > 50:
        return False, [], "Maximum 50 queries allowed in batch mode"
    
    cleaned_queries = []
    for line in lines:
        cleaned = clean_search_term(line)
        if cleaned:
            cleaned_queries.append(cleaned)
    
    if not cleaned_queries:
        return False, [], "No valid queries after cleaning"
    
    return True, cleaned_queries, ""
