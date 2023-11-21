import numpy as np
from CityGeoTools.metrics.data import CityInformationModel as BaseModel


city_model = BaseModel.CityInformationModel(city_name="Kaliningrad", city_crs=32634)

print(city_model.MobilityGraph)

city_model.update_layer(attr_name="Buildings", file_name="full_data.geojson")

print(city_model.Buildings)

city_model.update_layer(attr_name="Cafes", file_name="Urban_data_analysis/data/Инфраструктура досуга/Питание/cafe.geojson")


city_model.methods.services_clusterization.message