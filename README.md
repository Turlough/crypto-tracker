# Crypto Tracker
Stub for API calls. 

Currently, this supports only the
[Coinbase API](https://developers.coinbase.com/api/v2) 
only. Work in progress...

## Setup Instructions
You only need do this once.

NOTE: This link in step 1 is a 'join' invitation, as documented 
in https://www.coinbase.com/invite. 
The join url resolves to https://www.coinbase.com/join/cowman_bg

It earns both the inviter (me), and the invitee (you), to earn a small amount of Bitcoin,
following a modest amount of training- see https://www.coinbase.com/invite for exact quantities
which depends on US/EU exchange rates. 
It's 10 dollars each, after first 100 dollars trading, apparently.

You do not have to use the invite link to create your account, 
you can do it directly on Coinbase instead, 
losing me the price of 2 coffees plus a stick of chewing gum.
Thanks a million bud!

### The actual instructions
#### Create an account if you don't have one
Note: You will need Photo ID like a license or passport to create an account.

Also, this link is the invite link mentioned above.
1. Create an account on [Coinbase](https://www.coinbase.com/join/cowman_bg).
#### Create and use an API key
1. Under [Profile --> Settings --> API](https://www.coinbase.com/settings/api),
select __New API Key__.
1. In the __security__ folder, create a file called __api_keys.json__.
1. Copy the contents of __api_keys_template.json__ into it.
1. Replace the dummy values in __api_keys.json__ 
   with the public and secret keys you just created.
#### Create a Virtual Environment and install requirements
1. Create a virtual environment in the project folder:
`python -m venv venv`
1. Install requirements:
`pip install -r requirements.txt`
   
## Running the code
Load the virtual environment and run __main.py__:
### Linux:
```python
source venv/bin/activate
python main.py
```
### Windows:
```python
.\venv\scripts\activate
python main.py
```
You should see the json response.
