import plotly.express as px

# Get country input from the user
country = input("Enter the country name: ")

# Create a simple dataset
data = {
    'Country': [country],
    'Values': [100]
}

# Create the choropleth map
fig = px.choropleth(
    data,
    locations='Country',
    locationmode='country names',
    color='Values',
    color_continuous_scale='Inferno',
    title=f'Country Map Highlighting {country}'
)

# Show the map
fig.show()