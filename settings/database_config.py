from environs import Env


env = Env()
env.read_env()

name_user_db = env('NAME_USER_DB')
pass_db = env('PASSWORD_DB')

url = f'postgresql://{name_user_db}:{pass_db}@localhost:5432/postgres'
