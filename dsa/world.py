import pygal
from pygal.maps.world import World

# Create a world map
worldmap = World()

# Add some data
worldmap.title = 'Population of the world in 2024'
worldmap.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

# Render the map to a file
worldmap.render_to_file('world_population.svg')
