import streamlit as st
import plotly.graph_objects as go
import pandas as pd

@st.cache_data
def load_data():
    """Load and preprocess the air quality data."""
    df = pd.read_csv('air_quality_data.csv')
    df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
    return df

def create_scatter_plot(data, x_col, y_col, title, yaxis_title):
    """Create and return a scatter plot."""
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=data[x_col],
            y=data[y_col],
            mode='markers',
            marker=dict(size=10, color='blue'),
            name=y_col
        )
    )

    fig.update_layout(
        title=title,
        xaxis_title=x_col,
        yaxis_title=yaxis_title,
        xaxis=dict(gridcolor='lightgray'),
        yaxis=dict(gridcolor='lightgray'),
        plot_bgcolor='white'
    )

    return fig

def app():
    """Main function to run the Streamlit app."""
    # Load data
    df = load_data()

    # App title
    st.title('Visualisasi Data Kualitas Udara')

    # Selectbox for choosing the type of plot
    option = st.selectbox(
        'Pilih jenis visualisasi:',
        ['Suhu', 'Curah Hujan', 'Kecepatan Angin']
    )

    # Determine data and plot settings based on selection
    if option == 'Suhu':
        data = df[['PM2.5', 'TEMP']]
        title = 'Temperature Scatter Plot'
        yaxis_title = 'Temperature'
    elif option == 'Curah Hujan':
        data = df[['PM2.5', 'RAIN']]
        title = 'Rainfall Scatter Plot'
        yaxis_title = 'Curah Hujan'
    elif option == 'Kecepatan Angin':
        data = df[['PM2.5', 'WSPM']]
        title = 'Wind Speed Scatter Plot'
        yaxis_title = 'Kecepatan Angin'

    # Create and display the scatter plot
    fig = create_scatter_plot(data, data.columns[1], 'PM2.5', title, yaxis_title)
    st.plotly_chart(fig)

# Run the app
if __name__ == "__main__":
    app()
