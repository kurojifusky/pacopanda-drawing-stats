import re
import requests
from logger import log
from typing import Literal, Dict, Any
from urllib.parse import urlencode, urlparse, urlunparse, parse_qsl
from bs4 import BeautifulSoup
from selenium import webdriver
from .io import load_file
from .exceptions import StaticWebdriverError, RequiredParameter

rs = requests.Session()

OptionalDict = Dict[str, str] | None


def req_url_params(base_url: str, params: OptionalDict, headers: OptionalDict) -> str:
    if headers is None:
        headers = {}

    if params is None:
        params = {}

    parsed_url = urlparse(base_url)

    query_params = dict(parse_qsl(parsed_url.query))
    query_params.update(params)

    parsed_url = parsed_url._replace(query=urlencode(query_params))

    return rs.get(urlunparse(parsed_url), headers=headers)


class WebExtractor:
    """
    The combined powers of BeautifulSoup and Selenium, all in one class!
    """

    def __init__(self, mode: Literal["static", "dynamic"] = "static") -> None:
        self._scrape_mode = mode

        self._static_mode = self._scrape_mode == "static"
        self._dynamic_mode = self._scrape_mode == "dynamic"

    def _check_static_error(self):
        if self._static_mode or self._driver is None:
            raise StaticWebdriverError("Can't invoke a Selenium-specific function when 'static' mode is specified.")  # NOQA

    def url_request(self, url: str, params: OptionalDict, append_headers: OptionalDict):
        if params is None:
            params = {}

        if append_headers is None:
            append_headers = None

        _headers = {
            'User-Agent': 'Mozilla/5.0 (https://pds.kurojifusky.com) - for Paco Drawing Stats',
            'Referer': url,
            **append_headers
        }

        if self._static_mode:
            _req = req_url_params(url, params=params, headers=_headers)
            log("debug", f"Request {url}, recieved status code {_req.status_code}")  # NOQA

            return BeautifulSoup(_req.text, "html.parser")

        if self._dynamic_mode:
            profile = webdriver.FirefoxProfile()
            profile.set_preference("general.useragent.override", _headers)

            driver = webdriver.Firefox(profile)
            driver.get(url)


def parse_metadata_by_selector(url: str, title: str, description: str, tags: str, date: str) -> dict[str, str | list[str]]:
    """
    Gets the page metadata from a page request

    :param url: The artwork URL

    Returns:
        dict[str, str | list[str]]: An object that returns a title, description, date, and a list of tags
    """
    extractor = WebExtractor(mode="static")

    _page = extractor.url_request(url)

    return {
        "title": str(_page.select_one(title).text),
        "date": str(_page.select_one(date).get('title')),
        "description": str(_page.select_one(description).text),
        "tags": [str(tag) for tag in _page.select(tags)]
    }


def parse_description(description: str, tags: list[str]) -> dict[str, str]:
    """
    Separates description and parses a type of medium

    Args:
        description (str): _description_
        tags (list[str]): _description_

    Raises:
        RequiredParameter: _description_

    Returns:
        dict[str, str]: _description_
    """
    if description is None or tags is None:
        raise RequiredParameter("Param can't be None or empty string")

    char_list = load_file("../characters.yml")

    # This will be utilized 90% of the time
    desc_split = description.splitlines()
    parsed_desc = list(filter(None, desc_split))

    mediums = parsed_desc[-1]

    parsed_medium = [re.sub(r'\.|\/', '', x) for x in mediums.split()]
    parsed_medium = list(filter(None, parsed_medium))


def consolidate_metadata(artwork_data: dict[str, Any]) -> None:
    """
    Consolidates metadata from various pre-defined extractors
    """
    pass
