import os;

QR_DIRECTORY = os.getenv('QR_CODE_DIR', 'qr_code')
# Filename for the QR code
QR_FILENAME = os.getenv('QR_CODE_FILENAME', 'MyGitHub.png')
 # Fill color for the QR code
FILL_COLOR = os.getenv('FILL_COLOR', 'black')
 # Background color for the QR code