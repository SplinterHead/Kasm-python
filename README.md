# Kasm Python

A Python library for interacting with a Kasm instance  
The goal of this project is firstly to make it much easier to automate Kasm with Python,
and secondly to expose and document the un-documented API endpoints

## Pre-requisites

Kasm-python requires an API key and secret to be created in Kasm,
this can be done in the Admin panel under Settings > Developer. 
The permissions assigned to the API key can be Global Admin,
or it can be minimal permissions required for your use case

## Using Kasm-python

Import `Kasm` and create a new instance with the following args

| Argument         | Required | Description                       | Default |
|------------------|----------|-----------------------------------|---------|
| `url`            | Yes      | Base URL of the Kasm instance     | None    |
| `api_key`        | Yes      | API Key ID for accessing Kasm     | None    |
| `api_key_secret` | Yes      | API Key Secret for accessing Kasm | None    |

```python
from kasm_python.kasm import Kasm

kasm = Kasm(
    url="https://kasm.domain.com",
    api_key="abcd123",
    api_key_secret="abcdef12345678"
)
```

