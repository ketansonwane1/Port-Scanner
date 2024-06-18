# Port-Scanner
![port-scanner-1](https://github.com/ketansonwane1/Port-Scanner/assets/141003493/f078e006-f9d6-4871-a76a-66ace3c885f2)
![port-scanner-2](https://github.com/ketansonwane1/Port-Scanner/assets/141003493/2a75385b-250c-426f-9f94-fc7deb5b9703)

# 🔍 Port Scanner Tool

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🚀 Overview

Welcome to the **Port Scanner Tool**! This Python-based utility allows you to scan multiple ports on a target host efficiently, leveraging the power of multithreading for quick results.

## ✨ Features

- **Multithreaded Scanning**: Fast and efficient port scanning using threading.
- **Flexible Port Specification**: Scan individual ports, comma-separated lists, or ranges of ports.
- **Colorful Output**: Utilizes `colorama` for enhanced terminal output.

## 📋 Prerequisites

Ensure you have the following Python packages installed:

- `argparse`
- `threading`
- `socket`
- `colorama`
- `requests`

Install the required packages using pip:

```bash
pip install colorama requests
```

## 🛠️ Usage

To run the port scanner, use the following command in your terminal:

```bash
python port_scanner.py -host <target_host> -p <port(s)>
```

### Arguments

- `-host` : The target host's IP address or domain name (required).
- `-p` : The port(s) to scan. Can be a single port (`80`), a comma-separated list (`80,443`), or a range (`1-1024`).

### Examples

1. **Scan a single port**:

    ```bash
    python port_scanner.py -host 192.168.1.1 -p 80
    ```

2. **Scan multiple ports**:

    ```bash
    python port_scanner.py -host 192.168.1.1 -p 80,443,8080
    ```

3. **Scan a range of ports**:

    ```bash
    python port_scanner.py -host 192.168.1.1 -p 1-1024
    ```

## 📊 Output

![port-scanner-1](https://github.com/ketansonwane1/Port-Scanner/assets/141003493/f078e006-f9d6-4871-a76a-66ace3c885f2)
![port-scanner-2](https://github.com/ketansonwane1/Port-Scanner/assets/141003493/2a75385b-250c-426f-9f94-fc7deb5b9703)

# 🔍 Port Scanner Tool
## 🤝 Contribution

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📞 Contact

For any questions or inquiries, feel free to reach out:

- **Author**: Ketan Sonwane
- **GitHub**: [ketansonwane1](https://github.com/ketansonwane1)

---

Feel free to customize any part of this README to better suit your project's needs or your personal style!
