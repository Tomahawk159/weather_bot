from environs import Env


env = Env()
env.read_env()

geocoder_key = env('API_KEY_GEOCODER')
weather_key = env('API_KEY_WEATHER')
