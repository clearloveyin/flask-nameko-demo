from dotenv import load_dotenv
import os
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.flaskenv')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from create_app import create_app

app = create_app()


if __name__ == '__main__':
    app.run()