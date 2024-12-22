# NTU Wi-Fi Login Script

A Python script to automate the login process for the NTU Wi-Fi network. This script uses Selenium to interact with the login page and authenticate users.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## Features

- Automates the login process for NTU Wi-Fi.
- Uses Selenium for web automation.
- Configurable username and password through environment variables.

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver (or another browser driver)

**Note**: This script has only been tested on macOS. Compatibility with other operating systems (e.g., Windows, Linux) has not been verified.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/iLuJack/NTU_wifi_login.git
   cd NTU_wifi_login
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have the appropriate WebDriver installed for your browser (e.g., ChromeDriver for Google Chrome).

## Usage

### Running the Script

1. Set your NTU username and password as environment variables by creating a `.env` file in the same directory as the script with the following content:
   ```
   NTU_USERNAME=your_username
   NTU_PASSWORD=your_password
   ```

2. Run the script:
   ```bash
   python wifi_login.py
   ```

### How It Works

- The script opens a web browser in headless mode (no GUI).
- It accesses Google, which redirects to the NTU Wi-Fi login page.
- The script automatically fills in the username and password fields and submits the login form.

### Error Handling

If there are any issues during the login process, the script will print an error message to the console. Ensure that your credentials are correct and that you have a stable internet connection.

## Environment Variables

- `NTU_USERNAME`: Your NTU username.
- `NTU_PASSWORD`: Your NTU password.

Make sure to set these environment variables before running the script.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.