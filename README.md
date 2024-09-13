# TAMU Class Availability Checker

A simple program to check class availability at Texas A&M University (TAMU) and send notifications when classes become available.

## Features

- Sends HTTP GET requests to TAMU's class schedule pages.
- Parses the HTML response to determine class availability.
- Sends a text notification when a class opens up.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x

Additionally, you need to set up Gmail for sending notifications:

1. **Set up Gmail for Sending Emails:**

   Follow the instructions provided in this [SitePoint article](https://www.sitepoint.com/quick-tip-sending-email-via-gmail-with-python/) to configure your Gmail account to send emails via Python. 

   This involves:
   - Enabling "Less Secure Apps" access in your Google account settings or using an App Password if you have 2-Step Verification enabled.
   - Ensuring you have your Gmail email address and password (or App Password) ready for the `config.ini` configuration.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/OnePointOh/TAMU_Class_Search.git
   cd TAMU_Class_Search
   ```

2. **Set up a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

## Configuration

1. **Set up the configuration file:**

   Modify the `config.ini` file in the project directory with the following format:

   ```ini
   [Settings]
   term_in = 20XXXX
   phone_number = XXXXXXXXXX
   gmail = EXAMPLE@gmail.com
   gmail_key = XXXXXXXXXXXXXXXX
   carrier = att
   rest_time = 10

   [Classes]
   class1 = XXXXX
   class2 = XXXXX
   ```

   - **`term_in`**: The term code for which you are checking class availability (e.g., `202401` for Spring 2024).
   - **`phone_number`**: Your phone number for text notifications.
   - **`gmail`**: Your Gmail address used for sending notifications.
   - **`gmail_key`**: Your Gmail API key or app password (use the password or app password configured as per the Gmail setup instructions).
   - **`carrier`**: Your phone carrier (e.g., `att`, `verizon`).
   - **`rest_time`**: Time (in seconds) between availability checks.

   Under the `[Classes]` section, list the crn's for the classes you are monitoring. You can add more classes as needed. You can use any name for the classes in this config file:

   - **`class1`**: The code of the first class you are monitoring.
   - **`class2`**: The code of the second class you are monitoring.

2. **Ensure that the necessary environment variables or configuration settings for sending emails or texts are properly set up in your environment or in the script.**

## Usage

To run the program, use the following command:

```bash
python check_availability.py
```

This will start the program and it will continuously check for class availability based on the provided configuration.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to [Twilio](https://www.twilio.com/) for providing the SMS API.
- Inspiration from other TAMU class availability tools.

## Contact

For any questions or issues, please contact:

- **Email:** your.email@example.com
- **GitHub Issues:** [Issues](https://github.com/yourusername/tamu-class-availability-checker/issues)

---

Feel free to make any additional modifications to tailor the README to your specific needs!
