"""
## Utils

Helper functions for common file manipulations

Copyright 2021-2023 Kerby Keith Aquino
MIT License
"""
import json
from typing import Dict, Any
from datetime import timedelta
from bs4 import BeautifulSoup
from requests import Session
from requests.exceptions import ConnectionError


def is_empty_string(s: str) -> bool:
    """
    A wrapper function to check if a string is empty or contains only whitespaces.
    """
    return not s.strip()


def page_req(url: str) -> BeautifulSoup:
    """
    Sends an HTTP request and returns raw HTML markup

    :param url: A url required to make a request
    :return: HTML output via BeautifulSoup
    """
    try:
        _req = Session().get(url, timeout=None, headers={'User-Agent': 'Mozilla/5.0 kurofusky/1.0'})
        return BeautifulSoup(_req.text, "html.parser")

    except ConnectionError:
        raise ConnectionError


def load_file(file: str) -> Any:
    """
    Opens file, will open as JSON if file extension is detected

    :param file: File name
    :return File contents
    """
    with open(file, 'r', encoding='utf-8') as fi:
        if file.endswith('.json'):
            return json.load(fi)

        return fi.read()


def save_file(data, file: str, indent: bool = False) -> None:
    """
    Saves file, will autosave as JSON if file extension is detected

    :param data: Garbage
    :param file: File name
    :return File contents
    """
    with open(file, 'w', encoding='utf-8') as fo:
        if file.endswith('.json'):
            if not indent:
                json.dump(data, fo, ensure_ascii=True)
                return

            json.dump(data, fo, ensure_ascii=True, indent=2)
        else:
            fo.write(data)


# TODO overhaul this helper function
def cache_data(save_type='data', save_value: Dict = None) -> None:
    """
    Saves data to cache

    :param save_type: Must be values 'date', 'pagination', and 'data'
    :param save_value: The save value, must be a dict
    :return:
    """
    _cache_data = load_file('paco-cache.json')

    is_save_type_datetime = save_type == "date"
    is_save_type_pagination = save_type == "pagination"
    is_save_type_data = save_type == "data"

    data_dict = _cache_data.get("data")
    paginate_dict = _cache_data.get("pagination")
    date_dict = _cache_data.get("cached_time")

    not_vaild_save_types = not is_save_type_datetime and not is_save_type_pagination and not is_save_type_datetime

    if not_vaild_save_types:
        raise ValueError(
            f"Save type \"{save_type}\" invalid. Only valid types are 'date', 'pagination', and 'data'")

    if is_save_type_datetime:
        date_dict |= save_value

    if is_save_type_pagination:
        paginate_dict |= save_value

    if is_save_type_data:
        data_dict |= save_value

    save_file(_cache_data, "paco-cache.json")


def format_time(time: timedelta) -> str:
    """
    Formats delta time (current time - whatever time has passed) to
    readable time

    :param time: Requires a timedelta type
    :return: A string with a readable time format D HH:MM:SS
    :raises TypeError: If the time parameter is not of type timedelta
    """
    if not isinstance(time, timedelta):
        raise TypeError(
            "Invalid input type. Param 'time' must be a timedelta.")

    _dm_days, _dm_seconds = divmod(time.total_seconds(), 86400)

    d = f"{int(_dm_days)} days" if _dm_days != 1 else f"{int(_dm_days)} day"
    h, remainder = divmod(_dm_seconds, 3600)
    m, s = divmod(remainder, 60)

    h, m, s = map(lambda v: str(v).zfill(2), map(int, (h, m, s)))

    return f"{d} {h}:{m}:{s}"
