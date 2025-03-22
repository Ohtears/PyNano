import os
import importlib
from pathlib import Path

file_type_registry = {}

def register_file_type(extension):
    def decorator(cls):
        file_type_registry[extension.lower()] = cls
        return cls
    return decorator

def get_file_class_by_extension(filename):
    for ext, cls in file_type_registry.items():
        if filename.lower().endswith(ext):
            return cls
    raise ValueError(f"Unsupported file type: {filename}")

def load_all_file_types():
    """
    Dynamically import all file type modules from Models/FileTypes/.
    Each file will auto-register its class via the @register_file_type decorator.
    """
    filetypes_dir = Path(__file__).resolve().parent.parent / "FileTypes"
    for file in filetypes_dir.iterdir():
        if file.name.endswith(".py") and file.name != "__init__.py":
            module_name = f"Models.FileTypes.{file.stem}"
            importlib.import_module(module_name)
