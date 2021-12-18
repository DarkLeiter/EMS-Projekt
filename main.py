import pvlib as pv
from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS

Wien = pv.location.Location(48.210033,16.363449, tz=+1, name="Wien", altitude=172)
#print(Wien)
pv.pvsystem.PVSystem(arrays=None,surface_tilt=30,surface_azimuth=180,
                     albedo=0.2,surface_type='grass',module=None,module_typ)
print(pv.irradiance.SURFACE_ALBEDOS)