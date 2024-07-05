# 0x11. Python - Network #1
---

## Usage

### 0-hbtn_status.py


# 0x11. Python - Network #1

To execute the script and view its output with end-of-line markers, use the following command:

```bash
./0-hbtn_status.py | cat -e
```

This will produce output similar to the following, where `$` represents the end-of-line marker added by `cat -e`:

```
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
```

### 1-hbtn_header.py

This script sends a request to a specified URL and prints the value of the `X-Request-Id` header found in the response.
To execute the script, use the following command:

```bash
./1-hbtn_header.py https://alx-intranet.hbtn.io
```
Replace [URL] with the actual URL you want to send the request to.

For example:
```
./1-hbtn_header.py https://alx-intranet.hbtn.io
```
This command sends a request to `https://alx-intranet.hbtn.io` and prints the value of the `X-Request-Id` header from the response.
