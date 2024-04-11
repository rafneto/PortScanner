# Port Scanner

This Python script allows you to scan ports on a target host to check for open ports.

## Features

- Scans ports from 1 to 9999 on the specified target host.
- Utilizes concurrent port scanning for faster execution.
- Prints the status of open ports.
- Provides total time taken for the scanning process.

## Prerequisites

- Python 3.x
- `socket` library (included in Python standard library)
- `concurrent.futures` library (included in Python standard library)

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/port-scanner.git
```
2. Navigate to the repository directory:
```bash
cd port-scanner
```
3. Run the script:
```bash
python port_scanner.py
```
4. Follow the prompts to enter the IP address of the target host.

## Contributing

Contributions are welcome! Please feel free to fork the repository and submit pull requests with your improvements or bug fixes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.