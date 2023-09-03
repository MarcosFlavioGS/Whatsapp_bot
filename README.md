# WP Bot

This is a Whatsapp bot made for message automation.

## Contents

- Description
- Getting started
  - Prerequisites
  - Instalation
- Usage
- Configuration

## Description

The bot is made for rapid message sending for a list of contacts. It consumes some files like a contacts file, a link file, for your site, a message file, and a config file, from which it gets the name of the files, the time to wait between each contact and more.

## Getting Started

### Prerequisites

For this project it is needed:

- python
- Selenium
- chrome based browser

### Installation

Clone the repository to your local machine:

``` sh
git clone https://github.com/MarcosFlavioGS/Whatsapp_bot

```
Change to the project directory:

``` sh
cd Whatsapp_bot/

```
Install the required Python packages:

``` sh
pip install -r selenium

```
## Usage

The bot consumes 4 files. A config.json file, and the message, contacts and link files.

- contact.txt: Contacts separated by a new line.
- message.txt: A message to be sent for all the contacts
  - If you would like for the name of your contact to be shown on the message, just use the keyword PESSOA in any place of the message, and it will be replaced by the current contact name on runtime.
- link.txt: This is where the link to some site of your choice is meant to be, if there is none, the bot will simply igore this phase.

## Configuration

The configuration can be made using a config.json file. This is meant to be a place where you can determine the pause period, the file names that the bot will consume, and if it will restart from the beggining everytime or continue from the last contact it sent a message to.

### Configuration File


``` json
{
  "files": {
    "contatos": "contacts.txt",
    "mensagem": "message.txt",
    "link": "links.txt"
  },
  "recomeçar": true,
  "ultimo contato": "",
  "tempo para link": 5,
  "tempo entre contatos": 3
}

```


### Updating Configuration

The bot will automatically update the last contact field, but the rest of the field is made for the user to update.
