"""Sales data analyzer module for processing pipeline data."""


class DataLoadingError(Exception):
    """Raised when data loading fails"""

    pass


class DataValidationError(Exception):
    """Raised when data validation fails"""

    pass


class TransformationError(Exception):
    """Raised when data transformation fails"""

    pass
