import numpy as np
from CityGeoTools.metrics.data import CityInformationModel as BaseModel


city_model = BaseModel.CityInformationModel(city_name="Kaliningrad", city_crs=32634)

print(city_model.MobilityGraph)

