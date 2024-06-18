# Port-Scanner
![port-scanner-1](https://github.com/ketansonwane1/Port-Scanner/assets/141003493/f078e006-f9d6-4871-a76a-66ace3c885f2)
![port-scanner-2](https://github.com/ketansonwane1/Port-Scanner/assets/141003493/2a75385b-250c-426f-9f94-fc7deb5b9703)

Certainly! Here's an attractive README file for your GitHub project:

---

# Port Scanner Tool

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)

This repository contains a simple and effective port scanning tool written in Python. The tool uses multithreading to quickly scan specified ports on a given host.

## Features

- **Multithreaded Scanning**: Efficiently scans multiple ports using threading.
- **Customizable Port Range**: Allows scanning of individual ports, comma-separated lists of ports, or ranges of ports.
- **Colorful Console Output**: Utilizes `colorama` for colored terminal output.

## Prerequisites

Before running the script, ensure you have the following Python packages installed:

- `argparse`
- `threading`
- `socket`
- `colorama`
- `requests`

You can install the required packages using pip:

```bash
pip install colorama requests
```

## Usage

To run the port scanner, use the following command:

```bash
python port_scanner.py -host <target_host> -p <port(s)>
```

### Arguments

- `-host` : The target host's IP address or domain name (required).
- `-p` : The port(s) to scan. This can be a single port (`80`), a comma-separated list (`80,443`), or a range (`1-1024`).

### Examples

1. Scan a single port:

    ```bash
    python port_scanner.py -host 192.168.1.1 -p 80
    ```

2. Scan multiple ports:

    ```bash
    python port_scanner.py -host 192.168.1.1 -p 80,443,8080
    ```

3. Scan a range of ports:

    ```bash
    python port_scanner.py -host 192.168.1.1 -p 1-102                                                                         ```

## Contribution

Contributions are welcome! If you find a bug or want to add a new feature, feel free to open an issue or a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust any part of this README to better fit your needs or preferences!
