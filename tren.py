import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    df_drop = pd.read_csv('air_quality_data.csv')
    df_drop['date'] = pd.to_datetime(df_drop[['year', 'month', 'day']])
    return df_drop

def app():
    df_drop = load_data()

    # Process data
    monthly_data = df_drop.groupby([df_drop['date'].dt.to_period('M')]).agg({
        'PM2.5': 'mean', 'PM10': 'mean'
    }).reset_index()
    monthly_data['date'] = monthly_data['date'].astype(str)  # Convert Period to string

    # Create Plotly line chart for PM2.5 and PM10 with contrasting colors
    fig = px.line(
        monthly_data,
        x='date',
        y=['PM2.5', 'PM10'],
        labels={'value': 'Konsentrasi Polutan', 'date': 'Tanggal'},
        title='Tren Perubahan PM2.5, PM10',
        markers=True,
        color_discrete_map={
            'PM2.5': 'cyan',  # Bright color for PM2.5
            'PM10': 'magenta'  # Bright color for PM10
        }
    )

    # Convert date strings back to datetime for adding vertical lines
    fig.update_xaxes(
        tickformat='%Y-%m',  # Format x-axis ticks as year-month
    )

    # Add vertical lines for each year with adjusted opacity using RGBA color
    years = pd.to_datetime(monthly_data['date']).dt.year.unique()
    for year in years:
        fig.add_vline(
            x=f'{year}-01', 
            line=dict(color='rgba(255, 0, 0, 0.5)', dash='dash', width=2)  # Adjust opacity using RGBA
        )

    # Update layout for a cleaner look and increase size
    fig.update_layout(
        xaxis_title='Tanggal',
        yaxis_title='Konsentrasi Polutan',
        xaxis_tickangle=-45,
        title_x=0.5,
        title_font_size=20,
        legend_title='Jenis Polutan',
        template='plotly_dark',
        width=1200,  # Increase width
        height=600   # Increase height
    )

    # Display Plotly chart
    st.plotly_chart(fig, use_container_width=True)
