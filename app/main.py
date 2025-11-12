import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, filter_countries, top_regions

st.set_page_config(page_title="Solar Dashboard", layout="wide")
st.title("🌞 Solar Energy Insights Dashboard")


df_all = load_data()


countries = df_all['Country'].unique().tolist()
selected_countries = st.sidebar.multiselect(
    "Select countries to visualize:",
    options=countries,
    default=countries
)

metric_options = ['GHI','DNI','DHI']
selected_metric = st.sidebar.selectbox(
    "Select metric to visualize:",
    options=metric_options
)

df_filtered = filter_countries(df_all, selected_countries)


st.subheader(f"{selected_metric} Comparison Across Countries")
fig, ax = plt.subplots()
sns.boxplot(x='Country', y=selected_metric, data=df_filtered, ax=ax)
st.pyplot(fig)

st.subheader("Top Regions by Average GHI")
top_df = top_regions(df_filtered)
st.table(top_df)


st.subheader("Summary Statistics")
st.dataframe(df_filtered.groupby('Country')[metric_options].describe().T)
