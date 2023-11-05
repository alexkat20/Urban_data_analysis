import sys
import os
import numpy as np
from CityGeoTools.metrics.data import CityInformationModel as BaseModel

city_model = BaseModel.CityInformationModel(city_name="Kaliningrad", city_crs=3857)

print(city_model)

