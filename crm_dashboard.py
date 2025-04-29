
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
leads_df = pd.read_csv('fake_leads.csv')
opps_df = pd.read_csv('fake_opportunities.csv')
activities_df = pd.read_csv('fake_activities.csv')
accounts_df = pd.read_csv('fake_accounts.csv')

# Streamlit app
st.title('🚀 CRM Sales Dashboard')

# --- LEADS SECTION ---
st.header('Leads Overview')
st.metric(label="Total Leads", value=len(leads_df))
lead_sources = leads_df['LeadSource'].value_counts()
st.bar_chart(lead_sources)

# --- OPPORTUNITIES SECTION ---
st.header('Opportunities Overview')
st.metric(label="Total Opportunities", value=len(opps_df))
st.metric(label="Total Pipeline Value ($)", value=opps_df['Amount'].sum())

# Opportunities by Stage
stage_counts = opps_df['Stage'].value_counts()
fig_stage = px.bar(stage_counts, x=stage_counts.index, y=stage_counts.values,
                   labels={'x': 'Stage', 'y': 'Number of Opportunities'},
                   title="Opportunities by Stage")
st.plotly_chart(fig_stage)

# --- ACTIVITIES SECTION ---
st.header('Sales Activities Overview')
activity_types = activities_df['ActivityType'].value_counts()
st.bar_chart(activity_types)

# --- ACCOUNTS SECTION ---
st.header('Accounts Overview')
industries = accounts_df['Industry'].value_counts()
st.bar_chart(industries)

st.success('Dashboard loaded successfully 🚀')
    