import streamlit as st
import webbrowser
import urllib.parse
import pandas as pd
import json
import datetime
import os
from search_operators import SEARCH_OPERATORS, get_operator_info, get_operator_categories
from utils import (
    load_search_history, 
    save_search_history, 
    load_favorites, 
    save_favorites,
    validate_url,
    validate_keyword,
    build_search_url
)

# Page configuration with better aesthetics
st.set_page_config(
    page_title="Advanced Google Search Operators",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI/UX
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .feature-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin-bottom: 1rem;
    }
    
    .operator-info {
        background: linear-gradient(135deg, #667eea20, #764ba220);
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        border: 1px solid #e9ecef;
    }
    
    .search-button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.75rem 2rem;
        border: none;
        border-radius: 8px;
        font-weight: bold;
        cursor: pointer;
        width: 100%;
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .stat-item {
        text-align: center;
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
        color: #667eea;
    }
    
    .category-header {
        font-size: 1.2rem;
        font-weight: bold;
        color: #333;
        margin: 1rem 0 0.5rem 0;
        padding: 0.5rem;
        background: linear-gradient(90deg, #667eea10, #764ba210);
        border-radius: 5px;
    }
    
    .tip-box {
        background: #e3f2fd;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2196f3;
        margin: 1rem 0;
    }
    
    .creator-link {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        text-decoration: none;
        font-size: 0.9rem;
        z-index: 1000;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'search_history' not in st.session_state:
    st.session_state.search_history = load_search_history()
if 'favorites' not in st.session_state:
    st.session_state.favorites = load_favorites()
if 'batch_queries' not in st.session_state:
    st.session_state.batch_queries = []

# Main header
st.markdown("""
<div class="main-header">
    <h1>🚀 Advanced Google Search Operators</h1>
    <p>Professional SEO & Research Tool with 40+ Search Operators</p>
</div>
""", unsafe_allow_html=True)

# Statistics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Operators", len(SEARCH_OPERATORS), "40+")
with col2:
    st.metric("Search History", len(st.session_state.search_history), f"+{len(st.session_state.search_history)}")
with col3:
    st.metric("Favorites", len(st.session_state.favorites), f"⭐ {len(st.session_state.favorites)}")
with col4:
    st.metric("Batch Queue", len(st.session_state.batch_queries), f"📦 {len(st.session_state.batch_queries)}")

# Sidebar for navigation with improved design
with st.sidebar:
    st.markdown("### 🎯 Navigation Center")
    mode = st.radio(
        "Select Mode",
        ["🔍 Quick Search", "📦 Batch Search", "📚 Browse by Category", "📊 Search History", "⭐ Favorites"],
        index=0,
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Quick stats in sidebar
    st.markdown("### 📈 Quick Stats")
    st.info(f"**{len(SEARCH_OPERATORS)}** operators available")
    st.info(f"**{len(st.session_state.search_history)}** searches performed")
    st.info(f"**{len(st.session_state.favorites)}** favorites saved")
    
    st.markdown("---")
    st.markdown("### 💡 Pro Tips")
    st.markdown("""
    - Use quotes for exact phrases
    - Combine operators for precision
    - Save frequent searches as favorites
    - Export results as CSV
    """)

# Main content area with improved layouts
if mode == "🔍 Quick Search":
    st.markdown("## 🔍 Quick Search Builder")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Operator selection with categories
        st.markdown("### Select Search Operator")
        
        categories = get_operator_categories()
        selected_category = st.selectbox(
            "Choose Category:",
            list(categories.keys()),
            help="Browse operators by category"
        )
        
        # Show operators in selected category
        category_operators = categories[selected_category]
        available_operators = [op for op in category_operators if op in SEARCH_OPERATORS]
        
        selected_operator = st.selectbox(
            "Select Operator:",
            available_operators,
            help="Choose the specific search operator"
        )
        
        # Get operator information
        operator_info = get_operator_info(selected_operator)
        
        # Display operator info with better styling
        st.markdown(f"""
        <div class="operator-info">
            <h4>📋 {selected_operator}</h4>
            <p><strong>Description:</strong> {operator_info['description']}</p>
            <p><strong>Type:</strong> {'🌐 URL/Domain' if operator_info['type'] == 'url' else '🔤 Keyword'}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Dynamic input field
        search_input = ""
        if operator_info['type'] == 'url':
            search_input = st.text_input(
                "🌐 Enter URL or Domain:",
                placeholder=operator_info['placeholder'],
                help="Enter a valid URL or domain name"
            )
            
            if search_input and not validate_url(search_input):
                st.error("⚠️ Please enter a valid URL or domain (e.g., example.com)")
                
        else:  # keyword type
            search_input = st.text_input(
                "🔤 Enter Search Term:",
                placeholder=operator_info['placeholder'],
                help="Enter your search keywords"
            )
            
            if search_input and not validate_keyword(search_input):
                st.error("⚠️ Please enter valid search keywords")
        
        # Additional parameters
        additional_params = {}
        if selected_operator in ["before:", "after:", "daterange:"]:
            date_input = st.date_input("📅 Select Date:", datetime.date.today())
            additional_params['date'] = date_input.strftime("%Y-%m-%d")
        
        # Search button with better styling
        st.markdown("### 🚀 Execute Search")
        search_button = st.button("🔍 Search Google (100 Results)", type="primary", use_container_width=True)
        
        if search_button and search_input:
            if operator_info['type'] == 'url' and not validate_url(search_input):
                st.error("⚠️ Please enter a valid URL before searching")
            elif operator_info['type'] == 'keyword' and not validate_keyword(search_input):
                st.error("⚠️ Please enter valid keywords before searching")
            else:
                # Build search URL
                search_url = build_search_url(selected_operator, search_input, additional_params)
                
                # Save to history
                search_entry = {
                    'timestamp': datetime.datetime.now().isoformat(),
                    'operator': selected_operator,
                    'query': search_input,
                    'url': search_url,
                    'category': selected_category
                }
                st.session_state.search_history.append(search_entry)
                save_search_history(st.session_state.search_history)
                
                # Success message and URL
                st.success("🎉 Search executed! Opening results in new tab...")
                st.markdown(f"**🔗 Search URL:** [Click here if new tab didn't open]({search_url})")
                
                # JavaScript to open in new tab
                st.markdown(f"""
                <script>
                window.open('{search_url}', '_blank');
                </script>
                """, unsafe_allow_html=True)
                
                # Add to favorites option
                col_a, col_b = st.columns(2)
                with col_a:
                    if st.button("⭐ Add to Favorites", use_container_width=True):
                        if search_entry not in st.session_state.favorites:
                            st.session_state.favorites.append(search_entry)
                            save_favorites(st.session_state.favorites)
                            st.success("✅ Added to favorites!")
                        else:
                            st.warning("⚠️ Already in favorites!")
                
                with col_b:
                    if st.button("📋 Copy URL", use_container_width=True):
                        st.code(search_url)
    
    with col2:
        st.markdown("### 💡 Operator Guide")
        
        if operator_info.get('examples'):
            st.markdown("**📝 Examples:**")
            for example in operator_info['examples']:
                st.code(example, language="")
        
        st.markdown("### 🔥 Popular Operators")
        popular_ops = {
            "site:": "Search within websites",
            "filetype:": "Find specific files",
            "intitle:": "Search page titles", 
            "\"\"": "Exact phrase match",
            "-": "Exclude terms"
        }
        
        for op, desc in popular_ops.items():
            if st.button(f"**{op}** {desc}", key=f"pop_{op}", use_container_width=True):
                st.session_state.quick_select = op
                st.rerun()

elif mode == "📦 Batch Search":
    st.markdown("## 📦 Batch Search Manager")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("### 📝 Add Multiple Queries")
        
        batch_operator = st.selectbox(
            "🎯 Select Operator for Batch:",
            list(SEARCH_OPERATORS.keys()),
            help="All queries will use this operator"
        )
        
        batch_input = st.text_area(
            "📋 Enter Search Terms (one per line):",
            height=200,
            placeholder="digital marketing\nSEO tools\ncontent strategy\nsocial media marketing",
            help="Enter multiple search terms, one per line. Max 50 queries."
        )
        
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("➕ Add to Queue", type="primary", use_container_width=True):
                if batch_input:
                    lines = [line.strip() for line in batch_input.split('\n') if line.strip()]
                    if len(lines) > 50:
                        st.error("⚠️ Maximum 50 queries allowed")
                    else:
                        for line in lines:
                            query_entry = {
                                'operator': batch_operator,
                                'query': line,
                                'timestamp': datetime.datetime.now().isoformat()
                            }
                            st.session_state.batch_queries.append(query_entry)
                        st.success(f"✅ Added {len(lines)} queries to batch queue!")
                        st.rerun()
        
        with col_b:
            if st.button("🗑️ Clear All", use_container_width=True):
                st.session_state.batch_queries = []
                st.rerun()
        
        # Display batch queue
        if st.session_state.batch_queries:
            st.markdown("### 📊 Current Batch Queue")
            
            batch_df = pd.DataFrame(st.session_state.batch_queries)
            st.dataframe(batch_df, use_container_width=True)
            
            col_x, col_y, col_z = st.columns(3)
            
            with col_x:
                if st.button("🚀 Execute All Searches", type="primary", use_container_width=True):
                    search_urls = []
                    for query in st.session_state.batch_queries:
                        search_url = build_search_url(query['operator'], query['query'])
                        search_urls.append(search_url)
                        # Add to history
                        history_entry = {
                            'timestamp': datetime.datetime.now().isoformat(),
                            'operator': query['operator'],
                            'query': query['query'],
                            'url': search_url,
                            'batch': True
                        }
                        st.session_state.search_history.append(history_entry)
                    
                    save_search_history(st.session_state.search_history)
                    
                    # JavaScript to open multiple tabs with delay
                    js_code = ""
                    for i, url in enumerate(search_urls):
                        delay = i * 1000  # 1 second delay between each
                        js_code += f"setTimeout(function() {{ window.open('{url}', '_blank'); }}, {delay});\n"
                    
                    st.markdown(f"<script>{js_code}</script>", unsafe_allow_html=True)
                    st.success(f"🎉 Executing {len(st.session_state.batch_queries)} searches with 1s delays!")
            
            with col_y:
                # Export functionality
                if st.button("💾 Export Queue", use_container_width=True):
                    df = pd.DataFrame(st.session_state.batch_queries)
                    csv = df.to_csv(index=False)
                    st.download_button(
                        label="📄 Download CSV",
                        data=csv,
                        file_name=f"batch_queries_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                        mime="text/csv",
                        use_container_width=True
                    )
            
            with col_z:
                if st.button("🔄 Shuffle Queue", use_container_width=True):
                    import random
                    random.shuffle(st.session_state.batch_queries)
                    st.rerun()
    
    with col2:
        st.markdown("### 📊 Batch Statistics")
        if st.session_state.batch_queries:
            df = pd.DataFrame(st.session_state.batch_queries)
            operator_counts = df['operator'].value_counts()
            st.bar_chart(operator_counts)
            
            st.markdown("### 🎯 Operator Distribution")
            for op, count in operator_counts.items():
                st.metric(str(op), str(count))
        else:
            st.info("📝 No queries in batch queue")
        
        st.markdown("### 💡 Batch Tips")
        st.markdown("""
        - **Limit batch size** to avoid rate limiting
        - **Use delays** between searches (automatically applied)
        - **Review queue** before executing
        - **Export queue** for backup
        - **Mix operators** for comprehensive research
        """)

elif mode == "📚 Browse by Category":
    st.markdown("## 📚 Browse Operators by Category")
    
    categories = get_operator_categories()
    
    for category, operators in categories.items():
        st.markdown(f'<div class="category-header">{category}</div>', unsafe_allow_html=True)
        
        # Create columns for operators in this category
        cols = st.columns(min(3, len(operators)))
        
        for i, operator in enumerate(operators):
            if operator in SEARCH_OPERATORS:
                with cols[i % 3]:
                    info = get_operator_info(operator)
                    
                    with st.expander(f"**{operator}** "):
                        st.markdown(f"**Description:** {info['description']}")
                        st.markdown(f"**Type:** {'🌐 URL' if info['type'] == 'url' else '🔤 Keyword'}")
                        st.markdown(f"**Example:** `{info['placeholder']}`")
                        
                        if info.get('examples'):
                            st.markdown("**Usage Examples:**")
                            for example in info['examples'][:2]:  # Show first 2 examples
                                st.code(example)
                        
                        if st.button(f"Use {operator}", key=f"use_{operator}"):
                            # Set in session state to switch to Quick Search
                            st.session_state.selected_operator = operator
                            st.session_state.selected_mode = "🔍 Quick Search"
                            st.success(f"✅ Selected {operator}! Switching to Quick Search...")
                            st.rerun()

elif mode == "📊 Search History":
    st.markdown("## 📊 Search History & Analytics")
    
    if st.session_state.search_history:
        # Convert to DataFrame with proper handling
        history_data = []
        for entry in st.session_state.search_history:
            history_data.append({
                'timestamp': entry.get('timestamp', ''),
                'operator': entry.get('operator', ''),
                'query': entry.get('query', ''),
                'category': entry.get('category', 'Unknown'),
                'url': entry.get('url', '')
            })
        
        history_df = pd.DataFrame(history_data)
        history_df['timestamp'] = pd.to_datetime(history_df['timestamp']).dt.strftime('%Y-%m-%d %H:%M:%S')
        
        # Analytics section
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### 📊 Top Operators")
            operator_counts = history_df['operator'].value_counts().head(5)
            st.bar_chart(operator_counts)
        
        with col2:
            st.markdown("### 🏷️ Categories Used")
            category_counts = history_df['category'].value_counts()
            st.bar_chart(category_counts)
        
        with col3:
            st.markdown("### 📅 Search Frequency")
            # Group by date
            history_df['date'] = pd.to_datetime(history_df['timestamp']).dt.date
            date_counts = history_df['date'].value_counts().sort_index()
            st.line_chart(date_counts)
        
        # Filters
        st.markdown("### 🔍 Filter & Search History")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            operator_filter = st.selectbox(
                "Filter by Operator:",
                ["All"] + list(history_df['operator'].unique())
            )
        
        with col2:
            category_filter = st.selectbox(
                "Filter by Category:",
                ["All"] + list(history_df['category'].unique())
            )
        
        with col3:
            search_term_filter = st.text_input("Search in Queries:")
        
        # Apply filters
        filtered_df = history_df.copy()
        
        if operator_filter != "All":
            filtered_df = filtered_df[filtered_df['operator'] == operator_filter]
        
        if category_filter != "All":
            filtered_df = filtered_df[filtered_df['category'] == category_filter]
        
        if search_term_filter:
            filtered_df = filtered_df[filtered_df['query'].str.contains(search_term_filter, case=False, na=False)]
        
        # Display results
        st.dataframe(filtered_df, use_container_width=True)
        
        # Action buttons
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("🗑️ Clear History", use_container_width=True):
                if st.button("⚠️ Confirm Clear", use_container_width=True):
                    st.session_state.search_history = []
                    save_search_history(st.session_state.search_history)
                    st.success("✅ Search history cleared!")
                    st.rerun()
        
        with col2:
            csv = filtered_df.to_csv(index=False)
            st.download_button(
                label="📄 Export CSV",
                data=csv,
                file_name=f"search_history_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
                use_container_width=True
            )
        
        with col3:
            json_data = json.dumps(st.session_state.search_history, indent=2)
            st.download_button(
                label="📋 Export JSON",
                data=json_data,
                file_name=f"search_history_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json",
                use_container_width=True
            )
        
        with col4:
            if st.button("🔄 Refresh Data", use_container_width=True):
                st.rerun()
    
    else:
        st.markdown("""
        <div class="tip-box">
            <h3>📊 No Search History Yet</h3>
            <p>Start using the search operators to build your history and see analytics here!</p>
        </div>
        """, unsafe_allow_html=True)

elif mode == "⭐ Favorites":
    st.markdown("## ⭐ Favorite Searches")
    
    if st.session_state.favorites:
        st.success(f"📌 You have {len(st.session_state.favorites)} favorite searches")
        
        # Display favorites with enhanced UI
        for idx, favorite in enumerate(st.session_state.favorites):
            with st.expander(f"⭐ {favorite['operator']} - {favorite['query'][:50]}..."):
                col1, col2, col3 = st.columns([2, 1, 1])
                
                with col1:
                    st.markdown(f"**Operator:** {favorite['operator']}")
                    st.markdown(f"**Query:** {favorite['query']}")
                    st.markdown(f"**Category:** {favorite.get('category', 'Unknown')}")
                    st.markdown(f"**Added:** {favorite.get('timestamp', 'Unknown')[:16]}")
                
                with col2:
                    if st.button(f"🔍 Search Now", key=f"search_{idx}", use_container_width=True):
                        search_url = favorite['url']
                        st.markdown(f"""
                        <script>
                        window.open('{search_url}', '_blank');
                        </script>
                        """, unsafe_allow_html=True)
                        st.success("🚀 Opening search in new tab...")
                
                with col3:
                    if st.button(f"🗑️ Remove", key=f"remove_{idx}", use_container_width=True):
                        st.session_state.favorites.pop(idx)
                        save_favorites(st.session_state.favorites)
                        st.success("✅ Removed from favorites!")
                        st.rerun()
        
        # Bulk actions
        st.markdown("### 🔧 Bulk Actions")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🚀 Execute All Favorites", type="primary", use_container_width=True):
                for favorite in st.session_state.favorites:
                    search_url = favorite['url']
                    st.markdown(f"""
                    <script>
                    setTimeout(function() {{ window.open('{search_url}', '_blank'); }}, 1000);
                    </script>
                    """, unsafe_allow_html=True)
                st.success(f"🎉 Opening {len(st.session_state.favorites)} favorite searches!")
        
        with col2:
            favorites_df = pd.DataFrame(st.session_state.favorites)
            csv = favorites_df.to_csv(index=False)
            st.download_button(
                label="💾 Export Favorites",
                data=csv,
                file_name=f"favorites_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
                use_container_width=True
            )
        
        with col3:
            if st.button("🗑️ Clear All Favorites", use_container_width=True):
                if st.button("⚠️ Confirm Clear All", use_container_width=True):
                    st.session_state.favorites = []
                    save_favorites(st.session_state.favorites)
                    st.success("✅ All favorites cleared!")
                    st.rerun()
    
    else:
        st.markdown("""
        <div class="tip-box">
            <h3>⭐ No Favorites Yet</h3>
            <p>Save your frequently used searches as favorites for quick access!</p>
            <p>Use the <strong>Add to Favorites</strong> button after performing searches.</p>
        </div>
        """, unsafe_allow_html=True)

# Footer with creator credit
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem; background: linear-gradient(90deg, #667eea20, #764ba220); border-radius: 10px; margin-top: 2rem;'>
    <h3>🚀 Advanced Google Search Operators Tool</h3>
    <p><strong>Created by <a href='https://www.linkedin.com/in/amal-alexander-305780131/' target='_blank' style='color: #667eea; text-decoration: none;'>Amal Alexander</a></strong></p>
    <p><em>Empower your searches • Boost your SEO • Find anything faster</em></p>
    <p>📧 Connect • 🔗 LinkedIn • 🌟 Star this tool</p>
</div>
""", unsafe_allow_html=True)

# Floating creator credit
st.markdown("""
<a href='https://www.linkedin.com/in/amal-alexander-305780131/' target='_blank' class='creator-link'>
    Created by Amal Alexander
</a>
""", unsafe_allow_html=True)