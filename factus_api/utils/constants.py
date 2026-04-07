"""Load and store project constants from configuration files"""

from .json_handler import load_json

ENDPOINTS = load_json(json_file="factus_api/data/endpoints.json")
