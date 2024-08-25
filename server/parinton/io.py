from typing import Any
import json
import yaml


def load_file(file: str) -> Any:
    """
    Opens file, will open as JSON or parse to YAML if respective file extension is detected

    :param file: File name
    :return File contents
    """
    with open(file, 'r', encoding='utf-8') as f:
        if file.endswith('.json'):
            return json.load(f)

        if file.endswith('.yml') or file.endswith('.yaml'):
            return yaml.safe_load(f)

        return f.read()


def save_file(data, file: str, indent: bool = False) -> None:
    """
    Saves file, will autosave as JSON if file extension is detected

    :param data: Garbage
    :param file: File name
    :return File contents
    """
    with open(file, 'w+', encoding='utf-8') as f:
        if file.endswith('.json'):
            if not indent:
                json.dump(data, f, ensure_ascii=True)
                return

            json.dump(data, f, ensure_ascii=True, indent=2)
        else:
            f.write(data)
