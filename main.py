# This is a sample Python script.
import pandas as pd
import os
os.environ['PROJ_LIB'] = '/Users/avinash/anaconda3/envs/map-plot/share/proj'
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import gmplot

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Code adapted from https://python-graph-gallery.com/315-a-world-map-of-surf-tweets/ and http://qingkaikong.blogspot.com/2016/02/plot-earthquake-heatmap-on-basemap-and.html


def print_hi(name):
    # read the data (on the web)
    data = pd.read_csv('/Users/avinash/Downloads/data.adm.csv', sep=",")

    data['lon1'] = data['bounding_box'].apply(lambda x: x.split()[0].split(",")[0])
    data['lat1'] = data['bounding_box'].apply(lambda x: x.split()[0].split(",")[1])
    data['lon2'] = data['bounding_box'].apply(lambda x: x.split()[1].split(",")[0])
    data['lat2'] = data['bounding_box'].apply(lambda x: x.split()[1].split(",")[1])

    data['avg_lon'] = (data['lon1'].apply(lambda x: float(x)) + data['lon2'].apply(lambda x: float(x)) )/2.0
    data['avg_lat'] = (data['lat1'].apply(lambda x: float(x)) + data['lat2'].apply(lambda x: float(x))) /2.0

    # declare the center of the map, and how much we want the map zoomed in
    gmap = gmplot.GoogleMapPlotter(0, 0, 2)
    # plot heatmap
    gmap.heatmap(data['avg_lat'], data['avg_lon'])
    gmap.draw("Vaccine_heatmap.html")

    # # Set the dimension of the figure
    # my_dpi = 96
    # plt.figure(figsize=(2600 / my_dpi, 1800 / my_dpi), dpi=my_dpi)
    #
    # # Make the background map
    # m = Basemap(llcrnrlon=-180, llcrnrlat=-65, urcrnrlon=180, urcrnrlat=80)
    # m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
    # m.fillcontinents(color='grey', alpha=0.3)
    # m.drawcoastlines(linewidth=0.1, color="white")
    #
    # # Add a point per position
    # m.scatter(data['avg_lon'], data['avg_lat'], alpha=0.4, cmap="Set1")
    #
    # # Save as png
    # plt.savefig('#315_Tweet_Surf_Bubble_map1.png', bbox_inches='tight')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
