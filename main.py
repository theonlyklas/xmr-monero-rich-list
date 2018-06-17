import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sys
import pdb

# enter a page number that doesn't exist and a 404 isn't returned, the page containing the genesis block is returned no matter what instead
USE_NONEXISTANT_PAGE_REDIRECT_BUG = False
# you don't want to DDOS xmrchain, please be conservative with this setting
COOLDOWN_BETWEEN_REQUESTS_ms = 100

# it usually is the case that there is a "Transaction pool" table above the "Transactions in older blocks" table
# I know Monero used to have empty blocks prior to the 2 minute block time, but it hasn't happened since I started writing this, so I don't know if that part of the page disappears when that happens
# I assume that the transaction pool section is always shown
TRANSACTION_POOL_INDEX = 0
OLDER_TRANSACTIONS_INDEX = 1

class account(address, balance):
    address = address
    balance = balance
    transactions = []

    def update_balance(new_balance):
        balance = new_balance

class transaction(sending_address, receiving_address, amount, fee, confirmation_time):


def main():
    """

    """
    mandated_ringct_block = 1400000
    block_time = 120

    base_url = "https://www.xmrchain.net"

    if (USE_NONEXISTANT_PAGE_REDIRECT_BUG == True):
        # go straight to the page with the genesis block
        response = requests.get(base_url + "/page/" + str(sys.maxsize))
        parsed_response = BeautifulSoup(response.text, 'html.parser')
    else:
        # perform a GET request to https://xmrchain.net and parse it with BS4
        response = requests.get(base_url)
        parsed_response = BeautifulSoup(response.text, 'html.parser')

        # extract the link to the last page
        last_page_href = parsed_response.find(id="pages").find_all('a')[0].attrs['href']

        # perform a GET request to the last page of blocks and parse it with BS4
        response = requests.get(base_url + last_page_href)
        parsed_response = BeautifulSoup(response.text, 'html.parser')

        # check if actually on the last page. Another page may have beem added if another block was added while making requests
        last_page_href = parsed_response.find(id="pages").find_all('a')[2].attrs['href']

        # perform a GET request to the last page of blocks and parse it with BS4
        # unless this request takes as long as 10 x <Monero current block time>, we will now be at the last page
        response = requests.get(base_url + last_page_href)
        parsed_response = BeautifulSoup(response.text, 'html.parser')

        oldest_block_on_page = find_oldest_block_on_page(parsed_response)

        while (oldest_block_on_page < mandated_ringct_block)
            links_to_block_hashes = 



    return

def find_oldest_block_on_page(parsed_response)
    """
    Finds the oldest block on a page.

    Args:
        parsed_response (bs4.BeautifulSoup object): the response after being parsed by BeautifulSoup
    
    Returns:
        oldest_block_number (int): the oldest block number on the page
    """
    block_records = tables_on_page[OLDER_TRANSACTIONS_INDEX].find_all('tr')

    oldest_block_on_page = block_records[-1]

    oldest_block_number = oldest_block_on_page.find_all('td')[0].find('a').contents

    return oldest_block_number


def check_new_page(parsed_response, last_block_processed):
    """
    Checks if the loaded page isn't missing a block.
    As new blocks are found, older blocks are pushed onto pages of increasing number.  Therefore, if a block were to be added while running this script (highly likely with a 2 minute block time), it would have to temporarily return to the previous page.

    Args:
        parsed_response (bs4.BeautifulSoup object): a response object after being parsed by BeautifulSoup
        last_block_processed (int): the last block of transactions processed

    Returns:

    """
    return

main()









