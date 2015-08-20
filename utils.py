__author__ = 'chiayuanchuang'

import os
import logging
logger = logging.getLogger(__name__)

def get_env_variable(section_name, var_name, default=False):
    """
    Get the environment variable or return exception
    :param var_name: Environment Variable to lookup
    """
    try:
        return os.environ[var_name]
    except KeyError:
        import StringIO
        import ConfigParser
        PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
        env_file = os.environ.get('PROJECT_ENV_FILE', PROJECT_ROOT + "/env.cfg")
        try:
            cp = ConfigParser.RawConfigParser()
            cp.readfp(open(env_file))
            value = cp.get(section_name, var_name.lower())
            os.environ.setdefault(var_name, value)
            return value
        except:
            logger.debug("Have Exception while load env variables")
            if default is not False:
                return default
            from django.core.exceptions import ImproperlyConfigured
            error_msg = "Environment file: {env_file}, Section: {section_name}, " \
                        "Variable name: {var_name}"
            raise ImproperlyConfigured(error_msg.format(section_name = section_name,
                                                        var_name=var_name,
                                                        env_file=env_file))
