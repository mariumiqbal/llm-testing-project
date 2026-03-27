def is_not_empty(response):
    if not response or response.strip() == "":
        raise ValueError("Response cannot be empty or None")
    return True

def is_string(response):
    if not isinstance(response, str):
        raise ValueError("Response must be a string")

def contains_keyword(response, keyword):
    if keyword.lower() not in response.lower():
        raise ValueError("Response must contain the specified keyword")

def is_within_length(response, max_length):
    if len(response) > max_length:
        raise ValueError("Response exceeds the maximum allowed length")
    return True