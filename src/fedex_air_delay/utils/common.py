import os
import yaml
import json
import logger
import joblib
from typing import Any
from pathlib import Path
from box import ConfigBox
from fedex_air_delay import logger
from box.exceptions import BoxValueError
from ensure import ensure_annotations

@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    """
    reads yaml file and returns

    Args:
        path_to_yaml(str): path like input
    
    Raises:
        ValueError: if yaml file is empty
    
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully...")
        return ConfigBox(content)
    except BoxValueError:
        raise BoxValueError("yaml file is empty!!")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    creates list of directories

    Args:
        path_to_directories: list of path of directories
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at : {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    saves json data

    Args:
    path(Path): path to the json file
    data(Dict): data to be saved in the json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at : {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    loads json file data

    Args:
        path(Path): path to the json file
    
    Returns:
        ConfigBox: data as class attribute instead of a dict
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully from : {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    saves binary file

    Args:
    data(Any): data to be saved as a binary file
    path(Path): path to the binary file

    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at : {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    loads binary data

    Args:
        path(Path): path to the binary file to be loaded
    
    Returns:
        Any: object stored in the given file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from : {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    gets size of a gile in KiloBytes

    Args:
        path(Path): path to the file

    Returns:
        str: size of file in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"