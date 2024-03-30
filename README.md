# IS601-HW7
QR Code Generator: A Python application utilizing Docker to generate QR code PNG files containing URLs. Scan the generated QR codes with your phone camera to seamlessly navigate to the target website. Simplify website access on the go with this efficient integration. Find the code and instructions on GitHub

### Prerequisites
- Python 3.x
- `qrcode` library (`pip install qrcode`)
- `python-dotenv` library (`pip install python-dotenv`)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/secret-qr-code-generator.git

2. Navigate to the project directory:
    ```bash
    cd secret-qr-code-generator

3. Install dependencies:
    ```bash
    pip install -r requirements.txt

### Usage
Run the script with the desired URL to generate a secret QR code:
    ```bash
    python generate_secret_qr_code.py --url "https://example.com"


### Configuration
The script uses environment variables for configuration. You can customize the directory and color options by setting the following variables in a .env file:
    - QR_SECRET_DIR: Directory for saving the secret QR code (default: secret_qr_code)
    - SECRET_FILL_COLOR: Fill color for the QR code (default: black)
    - SECRET_BACK_COLOR: Background color for the QR code (default: white)


### Author
Karthik A