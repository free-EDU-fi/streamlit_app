

import streamlit as st

# Initialize session state for authentication
if 'username' not in st.session_state:
    st.session_state.username = ''
if 'password' not in st.session_state:
    st.session_state.password = ''
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

st.title("Interactive Data Visualization Dashboard")

# Simple user authentication
users = {"user1": "password1", "user2": "password2"}

def authenticate(username, password):
    return username in users and users[username] == password

def login():
    if authenticate(st.session_state.username, st.session_state.password):
        st.session_state.authenticated = True
        st.success("Successfully logged in!")
    else:
        st.error("Invalid username or password")

if not st.session_state.authenticated:
    st.text_input("Username", key='username')
    st.text_input("Password", type="password", key='password')
    st.button("Login", on_click=login)
else:
    st.write("Welcome, you are logged in!")
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.username = ''
        st.session_state.password = ''
        st.experimental_rerun()

if st.session_state.authenticated:
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from io import StringIO

    # Sample data strings for demonstration
    sample_data_1 = """
Date,Product,Sales,Profit
2024-01-01,Product A,100,20
2024-01-02,Product B,150,30
2024-01-03,Product C,200,50
2024-01-04,Product A,130,25
2024-01-05,Product B,170,35
"""

    sample_data_2 = """
Student,Math,Science,English
Alice,85,92,88
Bob,78,85,82
Charlie,90,95,94
David,70,75,72
Eva,88,89,85
"""

    sample_data_3 = """
Day,Temperature,Humidity,Wind Speed
Monday,25,60,15
Tuesday,22,55,10
Wednesday,28,65,20
Thursday,30,70,25
Friday,26,63,18
"""

    # Function to convert sample data to DataFrame
    def load_sample_data(data_str):
        return pd.read_csv(StringIO(data_str))

    # Sidebar for sample data selection
    st.sidebar.title("Sample Data")
    sample_selection = st.sidebar.selectbox("Select a sample dataset", ["None", "Sales Data", "Student Scores", "Weather Data"])

    df = None
    if sample_selection == "Sales Data":
        df = load_sample_data(sample_data_1)
    elif sample_selection == "Student Scores":
        df = load_sample_data(sample_data_2)
    elif sample_selection == "Weather Data":
        df = load_sample_data(sample_data_3)

    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

    if df is not None:
        st.write("Data Preview:", df.head())
        st.write("Data Summary:", df.describe())

        # Visualization options based on user selection
        columns = df.columns.tolist()

        # Scatter Plot
        x_axis = st.selectbox("Select X-axis column for scatter plot", columns)
        y_axis = st.selectbox("Select Y-axis column for scatter plot", columns)
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax)
        st.pyplot(fig)

        # Histogram
        hist_column = st.selectbox("Select column for histogram", columns)
        fig, ax = plt.subplots()
        sns.histplot(df[hist_column], kde=True, ax=ax)
        st.pyplot(fig)

        # Bar Chart
        bar_x = st.selectbox("Select X-axis column for bar chart", columns)
        bar_y = st.selectbox("Select Y-axis column for bar chart", columns)
        fig, ax = plt.subplots()
        sns.barplot(data=df, x=bar_x, y=bar_y, ax=ax)
        st.pyplot(fig)

        # Box Plot
        box_x = st.selectbox("Select X-axis column for box plot", columns)
        box_y = st.selectbox("Select Y-axis column for box plot", columns)
        fig, ax = plt.subplots()
        sns.boxplot(data=df, x=box_x, y=box_y, ax=ax)
        st.pyplot(fig)

        # Line Chart
        if 'Date' in df.columns:
            st.write("Line Chart")
            line_y = st.selectbox("Select Y-axis column for line chart", columns)
            df['Date'] = pd.to_datetime(df['Date'])
            df.sort_values('Date', inplace=True)
            fig, ax = plt.subplots()
            sns.lineplot(data=df, x='Date', y=line_y, ax=ax)
            st.pyplot(fig)

        # Correlation Heatmap
        numeric_df = df.select_dtypes(include='number')
        if not numeric_df.empty:
            st.write("Correlation Heatmap")
            fig, ax = plt.subplots()
            sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=ax)
            st.pyplot(fig)
        else:
            st.write("No numeric columns available for correlation heatmap.")
    
import pandas as pd
from io import StringIO
import streamlit as st

@st.cache_data
def load_data(data):
    return pd.read_csv(StringIO(data))

if st.session_state.authenticated:
    # More complex data interactions
    # ...

    # Sample data for demonstration
    sample_data = """
Date,Product,Sales
2024-01-01,Product A,100
2024-01-02,Product B,150
"""

    df = load_data(sample_data)
    st.write("Loaded Data:", df.head())

    # Example interaction using session state
    if 'counter' not in st.session_state:
        st.session_state.counter = 0
    if st.button('Increase counter'):
        st.session_state.counter += 1
    st.write('Counter value:', st.session_state.counter)

roles = {"user1": "admin", "user2": "viewer"}

if st.session_state.authenticated:
    user_role = roles.get(st.session_state.username, "viewer")
    if user_role == "admin":
        st.write("Admin Panel: Access to all data and configurations.")
    else:
        st.write("Viewer Panel: Limited access, only viewing is permitted.")
