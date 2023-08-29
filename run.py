import os
from app import create_app
from app.config import config_dict

CONFIG_MODE = 'debug' if os.getenv('DEBUG', 'False') else 'production'

try:
    AppConfig = config_dict[CONFIG_MODE]

except KeyError:
    print('Error: Invalid <CONFIG_MODE>. Expected values [debug, production] ')

app = create_app(AppConfig)

if __name__ == "__main__":
    app.run()
