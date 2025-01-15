import streamlit as st
import requests
import datetime
import pandas as pd
import time
from io import StringIO
from config import config

# Set page configuration
st.set_page_config(
    page_title="Customer Screening Tool",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #4B5563;
        margin-bottom: 1rem;
    }
    .subheader {
        font-size: 1.5rem;
        font-weight: 600;
        color: #4B5563;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    .card {
        background-color: #1F2937;
        color: #E5E7EB;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        margin-bottom: 20px;
    }
    .result-card {
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    .match-found {
        background-color: #FEF3C7;
        border-left: 5px solid #F59E0B;
    }
    .no-match {
        background-color: #D1FAE5;
        border-left: 5px solid #10B981;
    }
    .info-box {
        background-color: #E0F2FE;
        border-left: 5px solid #3B82F6;
        padding: 10px;
        border-radius: 5px;
    }
    .warning-box {
        background-color: #FEF3C7;
        border-left: 5px solid #F59E0B;
        padding: 10px;
        border-radius: 5px;
        color: #92400e;
    }
    .success-box {
        background-color: #D1FAE5;
        border-left: 5px solid #10B981;
        padding: 10px;
        border-radius: 5px;
        color: #065f46;
    }
    .footer {
        text-align: center;
        margin-top: 30px;
        color: #6c757d;
        font-size: 0.8rem;
    }
    .stButton>button {
        background-color: #6B7280;
        color: white;
        font-weight: 500;
    }
    /* Remove white box background */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    /* Remove padding around header */
    header {
        background-color: transparent !important;
    }
    /* Text color for labels and text in dark cards */
    .card label, .card .stMarkdown {
        color: #E5E7EB !important;
    }
    .card .stSelectbox label, .card .stTextInput label, .card .stNumberInput label {
        color: #E5E7EB !important;
    }
    /* Make form text input more visible on dark background */
    .card .stTextInput input, .card .stNumberInput input, .card .stSelectbox select {
        background-color: #374151 !important;
        color: #F9FAFB !important;
        border-color: #4B5563 !important;
    }
</style>
""", unsafe_allow_html=True)

# API endpoints from config
SCREENING_API_URL = config.SCREENING_API_URL
UPLOAD_API_URL = config.UPLOAD_API_URL

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/150x80?text=Logo", use_column_width=True)
    st.markdown("### Navigation")
    page = st.radio("", ["Screen Customer", "Upload Watchlist", "Help"])
    
    st.markdown("---")
    st.markdown("### Stats")
    # These could be fetched from a stats API endpoint in a real implementation
    try:
        stats_response = requests.get(f"{config.BASE_API_URL}/stats", timeout=300)
        if stats_response.status_code == 200:
            stats = stats_response.json()
            st.metric("Screenings Today", stats.get("screenings_today", "N/A"))
            st.metric("Watchlist Size", stats.get("watchlist_size", "N/A"))
        else:
            st.metric("Screenings Today", "N/A")
            st.metric("Watchlist Size", "N/A")
    except:
        st.metric("Screenings Today", "N/A")
        st.metric("Watchlist Size", "N/A")
    
    st.markdown("---")
    st.markdown("#### Last Updated")
    st.markdown(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")

# Main content
st.markdown('<h1 class="main-header">Customer Screening Tool</h1>', unsafe_allow_html=True)

if page == "Screen Customer":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="subheader">Customer Details</h2>', unsafe_allow_html=True)
    
    with st.form(key="screening_form"):
        col1, col2 = st.columns([3, 1])
        with col1:
            name = st.text_input("Full Name *", help="Customer's full name (required)")
        with col2:
            id_number = st.text_input("ID Number", help="Optional: Passport, National ID, etc.")

        # Date of birth with a better layout
        st.markdown("Date of Birth")
        dob_col1, dob_col2, dob_col3 = st.columns(3)
        with dob_col1:
            dob_year = st.selectbox("Year", 
                                    options=[None] + list(range(datetime.date.today().year, 1900, -1)),
                                    index=0)
        with dob_col2:
            dob_month = st.selectbox("Month", 
                                    options=[None] + list(range(1, 13)),
                                    index=0,
                                    format_func=lambda x: None if x is None else datetime.date(2000, x, 1).strftime('%B'))
        with dob_col3:
            max_day = 31
            if dob_month in [4, 6, 9, 11]:
                max_day = 30
            elif dob_month == 2:
                # Simple leap year check
                if dob_year and dob_year % 4 == 0 and (dob_year % 100 != 0 or dob_year % 400 == 0):
                    max_day = 29
                else:
                    max_day = 28
            dob_day = st.selectbox("Day", options=[None] + list(range(1, max_day + 1)), index=0)
        
        col1, col2 = st.columns(2)
        with col1:
            nationality = st.selectbox("Nationality", 
                                    options=[None, "United States", "United Kingdom", "Canada", "Australia", 
                                            "Germany", "France", "Japan", "China", "Other"],
                                    index=0)
        with col2:
            risk_level = st.select_slider("Risk Level Threshold", 
                                        options=["Low", "Medium", "High", "Critical"],
                                        value="Medium",
                                        help="Set minimum risk level to flag")
        
        col_button1, col_button2, _ = st.columns([1, 1, 2])
        with col_button1:
            clear = st.form_submit_button("Clear Form")
        with col_button2:
            submitted = st.form_submit_button("Screen Customer")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Handle form submission
    if submitted:
        if not name:
            st.error("Name is required")
        else:
            try:
                payload = {
                    "name": name,
                    "id_number": id_number if id_number else None,
                    "date_of_birth": {
                        "year": int(dob_year),
                        "month": int(dob_month),
                        "day": int(dob_day)
                    } if all([dob_year, dob_month, dob_day]) else None,
                    "nationality": nationality if nationality != "Other" else None,
                    "risk_threshold": {"Low": 0.25, "Medium": 0.5, "High": 0.75, "Critical": 0.9}[risk_level]
                }

                with st.spinner('Screening customer...'):
                    # Make the actual API call
                    response = requests.post(SCREENING_API_URL, json=payload, timeout=300)
                    response.raise_for_status()
                    result = response.json()

                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.markdown('<h2 class="subheader">Screening Results</h2>', unsafe_allow_html=True)
                
                if result.get("matched", False):
                    st.markdown('<div class="result-card match-found">', unsafe_allow_html=True)
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.warning("⚠️ Match Found!")
                        st.markdown(f"**Explanation:** {result.get('explanation', 'No explanation provided')}")
                    with col2:
                        st.metric("Risk Score", f"{result.get('risk_score', 0):.2f}", 
                                delta=f"{result.get('risk_score', 0) - 0.5:.2f}", 
                                delta_color="inverse")
                    st.markdown('</div>', unsafe_allow_html=True)

                    st.markdown('<h3 class="subheader">Matched Entities</h3>', unsafe_allow_html=True)
                    for i, match in enumerate(result.get("matches", [])):
                        with st.expander(f"Match {i+1}: {match['name']} ({match.get('risk_category', 'Unknown')})"):
                            cols = st.columns(3)
                            cols[0].markdown(f"**Risk Category:** {match.get('risk_category', 'Unknown')}")
                            cols[1].markdown(f"**Match Type:** {match.get('match_type', 'Unknown')}")
                            cols[2].markdown(f"**Match Score:** {match.get('match_score', 0):.2f}")
                            
                            st.markdown("#### Actions Required")
                            action_cols = st.columns(3)
                            action_cols[0].button(f"Add to Exceptions List", key=f"exception_{i}")
                            action_cols[1].button(f"Request Enhanced Due Diligence", key=f"edd_{i}")
                            action_cols[2].button(f"Report to Compliance", key=f"report_{i}")
                else:
                    st.markdown('<div class="result-card no-match">', unsafe_allow_html=True)
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.success("✓ No matches found")
                    with col2:
                        st.metric("Risk Score", f"{result.get('risk_score', 0):.2f}")
                    st.markdown('</div>', unsafe_allow_html=True)

                st.markdown('<div class="info-box">', unsafe_allow_html=True)
                col1, col2 = st.columns(2)
                col1.write(f"**Screening ID:** {result.get('screening_id', 'N/A')}")
                col2.write(f"**Screening Time:** {result.get('screening_time', datetime.datetime.now().isoformat())[:19].replace('T', ' ')}")
                st.markdown('</div>', unsafe_allow_html=True)
                
                st.download_button(
                    "Export Results (PDF)",
                    data="Sample PDF content", 
                    file_name=f"screening_{result.get('screening_id', 'unknown')}.pdf",
                    mime="application/pdf",
                )
                
                st.markdown('</div>', unsafe_allow_html=True)

            except requests.exceptions.RequestException as e:
                st.error(f"API Error: {str(e)}")
            except Exception as e:
                st.error(f"Error during screening: {str(e)}")

elif page == "Upload Watchlist":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="subheader">Upload Watchlist</h2>', unsafe_allow_html=True)
    
    # Help text
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown("""
    Upload your CSV watchlist with the following columns:
    - `unique_id` (required): Unique identifier for each entity
    - `name` (required): Full name of the person or entity
    - `date_of_birth` (optional): Date of birth in YYYY-MM-DD format
    - `nationality` (optional): Country of citizenship
    - `risk_category` (optional): PEP, SAN, etc.
    
    **Note:** If a `unique_id` already exists, the existing entry will be updated with new information.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    upload_col1, upload_col2 = st.columns([3, 1])
    with upload_col1:
        uploaded_file = st.file_uploader("Choose CSV file", type="csv")
    with upload_col2:
        st.download_button(
            "Download Template",
            data="unique_id,name,date_of_birth,nationality,risk_category\n001,John Smith,1980-01-15,US,PEP\n002,Jane Doe,1975-05-20,UK,SAN\n", 
            file_name="watchlist_template.csv",
            mime="text/csv",
        )
    
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            required_cols = {"unique_id", "name"}
            
            if not required_cols.issubset(df.columns):
                st.error(f"CSV must contain columns: {', '.join(required_cols)}")
            else:
                st.success(f"Valid file uploaded with {len(df)} entries")
                
                # Data validation
                validation_issues = []
                
                # Check for duplicate unique_ids within the file
                duplicate_ids = df[df.duplicated(subset=['unique_id'], keep=False)]['unique_id'].unique()
                if len(duplicate_ids) > 0:
                    validation_issues.append(f"Duplicate unique_ids found in file: {', '.join(map(str, duplicate_ids))}")
                
                # Check for missing names
                missing_names = df[df['name'].isna() | (df['name'] == '')].shape[0]
                if missing_names > 0:
                    validation_issues.append(f"{missing_names} entries have missing names")
                
                # Check date format if date_of_birth column exists
                if 'date_of_birth' in df.columns:
                    invalid_dates = 0
                    for idx, date_str in enumerate(df['date_of_birth'].dropna()):
                        try:
                            datetime.datetime.strptime(str(date_str), "%Y-%m-%d")
                        except ValueError:
                            invalid_dates += 1
                    if invalid_dates > 0:
                        validation_issues.append(f"{invalid_dates} entries have invalid date formats (should be YYYY-MM-DD)")
                
                if validation_issues:
                    st.markdown('<div class="warning-box">', unsafe_allow_html=True)
                    st.markdown("**Validation Issues Found:**")
                    for issue in validation_issues:
                        st.markdown(f"- {issue}")
                    st.markdown("These issues may cause errors during upload.")
                    st.markdown('</div>', unsafe_allow_html=True)
                
                # Preview data
                st.markdown('<h3 class="subheader">Data Preview</h3>', unsafe_allow_html=True)
                st.dataframe(df.head(10), use_container_width=True)
                
                # Show statistics
                st.markdown('<h3 class="subheader">Data Statistics</h3>', unsafe_allow_html=True)
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Total Entries", len(df))
                col2.metric("Unique IDs", df['unique_id'].nunique())
                
                # Count risk categories if available
                if "risk_category" in df.columns:
                    risk_counts = df["risk_category"].value_counts()
                    col3.metric("PEP Entries", risk_counts.get("PEP", 0))
                    col4.metric("SAN Entries", risk_counts.get("SAN", 0))
                
                # Upload options
                st.markdown('<h3 class="subheader">Upload Options</h3>', unsafe_allow_html=True)
                col1, col2 = st.columns(2)
                with col1:
                    batch_size = st.number_input("Batch Size", min_value=1, max_value=1000, value=100, 
                                               help="Number of records to process at once")
                with col2:
                    continue_on_error = st.checkbox("Continue on Errors", value=True,
                                                  help="Continue processing even if some records fail")
                
                if st.button("Process Watchlist", type="primary"):
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    try:
                        with st.spinner('Uploading watchlist...'):
                            # Convert DataFrame to list of dictionaries
                            data = df.to_dict('records')
                            
                            # Clean the data (remove NaN values)
                            cleaned_data = []
                            for record in data:
                                cleaned_record = {}
                                for key, value in record.items():
                                    if pd.isna(value) or value == '':
                                        cleaned_record[key] = None
                                    else:
                                        cleaned_record[key] = value
                                cleaned_data.append(cleaned_record)
                            
                            status_text.text("Sending data to API...")
                            response = requests.post(
                                UPLOAD_API_URL,
                                json={"watchlist": cleaned_data},
                                timeout=300  # 5 minute timeout for large uploads
                            )
                            response.raise_for_status()
                            result = response.json()
                        
                        progress_bar.progress(100)
                        status_text.text("Upload completed!")
                        
                        # Display results
                        st.markdown('<div class="success-box">', unsafe_allow_html=True)
                        st.markdown("**Upload Results:**")
                        
                        col1, col2, col3 = st.columns(3)
                        col1.metric("Created", result.get('created_count', 0))
                        col2.metric("Updated", result.get('updated_count', 0))
                        col3.metric("Errors", result.get('error_count', 0))
                        
                        st.markdown(f"**Message:** {result.get('message', 'Upload completed')}")
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                        if result.get('error_count', 0) > 0:
                            st.warning(f"Some records failed to process. Check the server logs for details.")

                    except requests.exceptions.RequestException as e:
                        st.error(f"API Error: {str(e)}")
                        progress_bar.empty()
                        status_text.empty()
                    except Exception as e:
                        st.error(f"Error processing file: {str(e)}")
                        progress_bar.empty()
                        status_text.empty()

        except Exception as e:
            st.error(f"Error reading file: {str(e)}")
    
    st.markdown('</div>', unsafe_allow_html=True)

else:  # Help & Documentation
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="subheader">Help & Documentation</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Quick Start Guide
    
    ### Screening a Customer
    1. Navigate to the "Screen Customer" tab
    2. Enter the customer's full name (required)
    3. Enter additional details if available (date of birth, ID number)
    4. Click "Screen Customer" to submit
    5. Review the results and take appropriate action
    
    ### Uploading a Watchlist
    1. Navigate to the "Upload Watchlist" tab
    2. Download the template if needed
    3. Prepare your CSV file with required columns:
       - `unique_id`: Unique identifier (required)
       - `name`: Full name (required)
       - `date_of_birth`: YYYY-MM-DD format (optional)
       - `nationality`: Country code or name (optional)
       - `risk_category`: PEP, SAN, etc. (optional)
    4. Upload your file and review the preview
    5. Click "Process Watchlist" to add to the database
    
    ### Troubleshooting
    
    #### Common Upload Issues:
    - **Duplicate unique_id error**: The system now handles duplicates by updating existing records
    - **Invalid date format**: Use YYYY-MM-DD format for dates
    - **Missing required fields**: Ensure all records have `unique_id` and `name`
    - **Large file timeouts**: Consider splitting large files into smaller batches
    
    #### API Errors:
    - Check that the backend service is running
    - Verify the API endpoints in your config file
    - Check network connectivity
    
    ### Data Quality Tips:
    - Remove duplicate unique_ids from your CSV before upload
    - Use consistent date formats (YYYY-MM-DD)
    - Standardize risk categories (PEP, SAN, etc.)
    - Clean names to remove extra spaces or special characters
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2025 Customer Screening Tool - All Rights Reserved</div>', unsafe_allow_html=True)