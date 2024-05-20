import re
import json
import yaml
import requests
from logger import log
from typing import Any, Literal, Dict
from datetime import timedelta
from urllib.parse import urlencode, urlparse, urlunparse, parse_qsl
from slugify import slugify
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Firefox as WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


rs = requests.Session()


def req_url_params(base_url: str, params: Dict[str, str]) -> str:
    parsed_url = urlparse(base_url)

    query_params = dict(parse_qsl(parsed_url.query))
    query_params.update(params)

    parsed_url = parsed_url._replace(query=urlencode(query_params))

    return rs.get(urlunparse(parsed_url))


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


def format_time(time: timedelta) -> str:
    """
    Formats delta time (current time - whatever time has passed) to
    readable time

    :param time: Requires a timedelta type
    :return: A string with a readable time format D HH:MM:SS
    :raises TypeError: If the time parameter is not of type timedelta
    """
    if not isinstance(time, timedelta):
        raise TypeError("Invalid input type. Param 'time' must be a timedelta.")  # NOQA

    SECS_IN_DAYS = 86400

    _dm_days, _dm_seconds = divmod(time.total_seconds(), SECS_IN_DAYS)

    d = f"{int(_dm_days)} days" if _dm_days != 1 else f"{int(_dm_days)} day"
    h, remainder = divmod(_dm_seconds, 3600)
    m, s = divmod(remainder, 60)

    h, m, s = map(lambda v: str(v).zfill(2), map(int, (h, m, s)))

    return f"{d} {h}:{m}:{s}"


class StaticWebdriverError(Exception):
    """
    Throws an exception that invoke a Selenium-specific function when 'static' mode is specified,
    used the WebExtractor class.
    """
    pass


class WebExtractor:
    """
    The combined powers of BeautifulSoup and Selenium, all in one class!
    """

    def __init__(self, mode: Literal["static", "dynamic"] = "static") -> None:
        self._scrape_mode = mode

        self._is_static_mode = self._scrape_mode == "static"
        self._is_dynamic_mode = self._scrape_mode == "dynamic"

    def _check_static_error(self):
        if self._is_static_mode or self._driver is None:
            raise StaticWebdriverError("Can't invoke a Selenium-specific function when 'static' mode is specified.")  # NOQA

    def url_request(self, url: str):
        _session = requests.Session()
        _headers = {
            'User-Agent': 'Mozilla/5.0 (https://kurojifusky.com) - for Paco Drawing Stats',
            'Referer': url
        }

        if self._is_static_mode:
            _req = _session.get(url, headers=self._headers)
            log("debug", f"Request {url}, recieved status code {_req.status_code}")  # NOQA

            return BeautifulSoup(_req.text, "html.parser")

        if self._is_dynamic_mode:
            profile = webdriver.FirefoxProfile()
            profile.set_preference("general.useragent.override", _headers)

            driver = webdriver.Firefox(profile)
            driver.get(url)


class RequiredParameter(Exception):
    pass


def parse_metadata_by_selector(url: str, title: str, description: str, tags: str, date: str) -> dict[str, str | int | list[str]]:
    # TODO ongoing refactoring
    """
    Gets the page metadata from a page request

    :param url: The artwork URL

    :return: An object that returns a title, description, date, and a list of tags
    """
    extractor = WebExtractor(mode="static")

    title_selector = selectors.get("title")
    desc_selector = selectors.get("description")
    tags_selector = selectors.get("tags")
    date_selector = selectors.get("date")

    _page = extractor.url_request(url)
    _description = _page.select_one(desc_selector)

    return {
        "title": str(_page.select_one(title_selector).text),
        "date": str(_page.select_one(date_selector).get('title')),
        "description": str(_description.text),
        "tags": [str(tag) for tag in _page.select(tags_selector)]
    }


def parse_description(description: str, tags: list[str]) -> dict[str, str]:
    if description is None or tags is None:
        raise RequiredParameter("Param can't be None or empty string")

    char_list = load_file("../characters.yml")

    # This will be utilized 90% of the time
    desc_split = description.splitlines()
    parsed_desc = list(filter(None, desc_split))

    mediums = parsed_desc[-1]

    parsed_medium = [re.sub(r'\.|\/', '', x) for x in mediums.split()]
    parsed_medium = list(filter(None, parsed_medium))
