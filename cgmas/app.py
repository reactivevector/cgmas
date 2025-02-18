import os

from cgmas.app_factory import create_app
from cgmas.blueprints.health import HEALTH_BP
from cgmas.blueprints.hello import HELLO_BP
from cgmas.blueprints.message import MESSAGE_BP
from cgmas.file.file import load_yaml_file

from .config import AppConfig, setup_app_config

APP = create_app()

# setup config
config_dir: str = os.path.join(os.path.dirname(__file__), os.pardir, 'config')
app_config: dict = load_yaml_file(os.path.join(config_dir, 'app.yaml'))
app_config['logging'] = {'config_file_path': os.path.join(config_dir, 'logging.yaml')}
app_config: AppConfig = AppConfig.model_validate(app_config)
setup_app_config(app_config)

# register blueprints
APP.register_blueprint(HELLO_BP)
APP.register_blueprint(HEALTH_BP)
APP.register_blueprint(MESSAGE_BP)

if __name__ == '__main__':
	APP.run(debug=True)
