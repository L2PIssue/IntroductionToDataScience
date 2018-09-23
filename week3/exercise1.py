import geopandas as gdp
import matplotlib.pyplot as plt
import pylab

fig, ax = plt.subplots()

# plot the world using world_m
world = gdp.read_file('world_m')
world.plot(ax=ax, color='violet', edgecolor='white')
pylab.savefig('world.png')

# plot another layer of information, namely the capital 
# cities of each country from the cities data-set
cities = gdp.read_file('cities')
cities.plot(ax=ax, marker='o', color='#480a60', markersize=5)
pylab.savefig('cities.png')

# perform a map projection to bring the two data-sets 
# into a shared coordinate system.
fig, bx = plt.subplots()
cities = cities.to_crs({'init': 'epsg:3395'})
world.plot(ax=bx, color='violet', edgecolor='white')
cities.plot(ax=bx, marker='o', color='#480a60', markersize=5)
pylab.savefig('cities_carrected.png')