# linksnip

Python SDK for creating and managing short URLs with project-based isolation.

## Installation

```bash
pip install linksnip
```

## Quick Start

```python
from linksnip import Client

# Initialize client with your API key
client = Client(
    base_url="https://yourdomain.com",
    api_key="lsnp_myproject_abc123..."
)

# Create a short link
short_url = client.shorten(
    url="https://example.com/long-product-url",
    brand="mybrand",
    post_id="p381"  # Optional - auto-generated if omitted
)

print(short_url)
# Output: https://yourdomain.com/myproject/mybrand/p381
```

## Features

- **Project-based isolation**: Each API key is scoped to a specific project
- **Hierarchical URLs**: All links follow `{project}/{brand}/{post_id}` format
- **Platform tracking**: Create platform-specific variations (Facebook, Instagram, etc.)
- **Auto-generated IDs**: Post IDs are generated automatically if not provided
- **Type hints**: Full typing support for better IDE experience

## Usage

### Basic Shortening

```python
url = client.shorten(
    url="https://example.com",
    brand="mybrand"
)
```

### Custom Post ID

```python
url = client.shorten(
    url="https://example.com",
    brand="mybrand",
    post_id="summer-sale-2026"
)
```

### Platform Tracking

Create platform-specific URLs for attribution:

```python
urls = client.shorten(
    url="https://example.com",
    brand="mybrand",
    platforms=["fb", "ig", "tg"]
)

print(urls["fb"])  # https://yourdomain.com/myproject/mybrand/abc123-fb
print(urls["ig"])  # https://yourdomain.com/myproject/mybrand/abc123-ig
```

### Delete a Link

```python
result = client.delete("myproject:mybrand:p381")
print(result["message"])  # Link deleted successfully
```

## API Reference

### `Client(base_url, api_key, timeout=30)`

Initialize the client.

**Parameters:**
- `base_url` (str): Base URL of your shortening service
- `api_key` (str): Your API key (format: `lsnp_{project}_{random}`)
- `timeout` (int): Request timeout in seconds (default: 30)

### `client.shorten(url, brand, post_id=None, platforms=None)`

Create a short link.

**Parameters:**
- `url` (str): Long URL to shorten
- `brand` (str): Brand identifier
- `post_id` (str, optional): Custom post ID (auto-generated if omitted)
- `platforms` (list, optional): Platform codes for UTM tracking

**Returns:**
- str: Short URL (if `platforms` is None)
- dict: Platform URLs (if `platforms` provided)

### `client.delete(link_id)`

Delete a short link.

**Parameters:**
- `link_id` (str): Link ID in format `project:brand:post_id`

**Returns:**
- dict: Deletion confirmation

## Error Handling

```python
from linksnip import (
    AuthenticationError,
    InvalidURLError,
    LinkExistsError,
    ValidationError,
    APIError
)

try:
    url = client.shorten(url="invalid-url", brand="test")
except AuthenticationError:
    print("Invalid API key")
except InvalidURLError:
    print("Invalid URL format")
except LinkExistsError:
    print("Link already exists")
except ValidationError as e:
    print(f"Validation error: {e}") 
except APIError as e:
    print(f"API error: {e}")
```

## Requirements

- Python 3.8+
- requests >= 2.28.0

## License

MIT
