"""
Contains utility functions
"""

import re
from pathlib import Path
import yaml
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations

from blogforge_ai import logger

def safe_slug(title: str) -> str:
    s = title.strip().lower()
    s = re.sub(r"[^a-z0-9 _-]+", "", s)
    s = re.sub(r"\s+", "_", s).strip("_")
    return s or "blog"

@ensure_annotations
def read_yaml(path_to_file:Path) ->ConfigBox:
    """
    read the yaml file and return

    Args:
        path_to_file(str): Path of yaml file

    Raises:
        ValueError: if yaml file is empty
        e: otherwise

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_file,'r+') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Yaml file: {path_to_file} is loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"Yaml file: {path_to_file} is empty")
    except Exception as e:
        raise e

def load_config_file(load_from_file: str):
    """
    Load application configuration from CONFIG_FILE_PATH.

    Args:
        load_from_file (str):
            Path of the module (__file__) requesting the configuration.

    Raises:
        FileNotFoundError:
            If CONFIG_FILE_PATH does not exist.

    Returns:
        ConfigBox:
            Loaded configuration.
    """
    from blogforge_ai.constants import CONFIG_FILE_PATH
    config_path = Path(CONFIG_FILE_PATH)
    try:
        if not config_path.is_file():
            logger.error(
                f"Configuration file not found: {config_path}. "
                f"Requested by: {load_from_file}"
            )
            raise FileNotFoundError(
                f"Configuration file not found: {config_path}"
            )
        logger.info(
            f"Loading configuration from: {config_path}. "
            f"Requested by: {load_from_file}"
        )
        config = read_yaml(config_path)
        logger.info(
            f"Configuration loaded successfully. "
            f"Requested by: {load_from_file}"
        )
        return config
    except FileNotFoundError as e:
        raise
    except Exception as err:
        logger.exception(
            f"Failed to load configuration from {config_path}. "
            f"Requested by: {load_from_file}"
            f"Due to: {err}"
        )
        raise

def load_prompts_file(load_from_file: str):
    """
    Load prompts from the PROMPT_FILE_PATH.

    Args:
        load_from_file (str):
            Path of the module (__file__) requesting the prompts.

    Raises:
        FileNotFoundError:
            If PROMPT_FILE_PATH does not exist.

    Returns:
        ConfigBox:
            Loaded prompts.
    """
    from blogforge_ai.constants import PROMPT_FILE_PATH
    prompts_path = Path(PROMPT_FILE_PATH)
    try:
        if not prompts_path.is_file():
            logger.error(
                f"Prompts file not found: {prompts_path}. "
                f"Requested by: {load_from_file}"
            )
            raise FileNotFoundError(
                f"Prompts file not found: {prompts_path}"
            )
        logger.info(
            f"Loading prompts from: {prompts_path}. "
            f"Requested by: {load_from_file}"
        )
        prompts = read_yaml(prompts_path)
        logger.info(
            f"Prompts loaded successfully. "
            f"Requested by: {load_from_file}"
        )
        return prompts
    except FileNotFoundError as e:
        raise
    except Exception as err:
        logger.exception(
            f"Failed to load prompts from {prompts}. "
            f"Requested by: {load_from_file}"
            f"Due to: {err}"
        )
        raise

