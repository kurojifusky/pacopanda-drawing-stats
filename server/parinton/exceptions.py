class RequiredParameter(Exception):
    pass


class StaticWebdriverError(Exception):
    """
    Throws an exception that invoke a Selenium-specific function when 'static' mode is specified,
    used the WebExtractor class.
    """
    pass
