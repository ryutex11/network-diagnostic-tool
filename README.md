# Network Diagnostic Tool

A lightweight Python command-line utility for basic DNS resolution and TCP connectivity checks.

## What it demonstrates

- Python networking with `socket`
- DNS/address resolution
- URL parsing
- Simple timeout handling
- CLI argument parsing

## Usage

```bash
python network_tool.py example.com
```

Check selected TCP ports:

```bash
python network_tool.py example.com 80 443 22
```

Use it only against systems you own or are explicitly authorized to test.
