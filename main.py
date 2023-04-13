# This file is for Creating an Entry Pointer - Logger - Main window
import logging

from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root

# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)

    # public and secret key needs to be removed when push to GitHub
    binance = BinanceClient("b2276a0d79f2236bbbeaca2d2da0ad8cd1be083bcc7f09b82c46e4791b5a95de",
                            "5f255ce76380900460706705fa7e12505025812dc5cd32c8626b82ba618fda60",
                            testnet=True, futures=True)
    bitmex = BitmexClient("2DR0LM4lq8gRg9yb3B3n85Is",
                          "o-p_Joys8Gi8InvgLHSmCBpdPmdMwIMGp666y7_hb3P0TQUG",
                          testnet=True)

    root = Root(binance, bitmex)
    root.mainloop()
