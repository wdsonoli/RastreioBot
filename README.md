# [RastreioBot](http://telegram.me/RastreioBot)

[![Build Status](https://github.com/GabrielRF/RastreioBot/actions/workflows/ci.yml/badge.svg)](https://github.com/GabrielRF/RastreioBot/actions/workflows/ci.yml)
[![Donate](https://img.shields.io/static/v1?label=Assine&message=PicPay&color=green)](https://grf.xyz/assine)
[![Donate](https://img.shields.io/static/v1?label=Colabore&message=PicPay&color=brightgreen)](https://grf.xyz/picpay)
[![Twitter Follow](https://img.shields.io/twitter/follow/espadrine.svg?style=social&label=Follow)](https://twitter.com/gabrf)

![Rastreiobot](https://github.com/GabrielRF/RastreioBot/blob/master/imgs/rastreiobot.png?raw=true)

* [About](#about)
* [Setup](#setup)
* [Run](#run)
* [Contribute](#contribute)
* [Contact](#contact)

## About

This is a [Telegram](http://telegram.org) Bot that tracks packages from the [Brazilian Mail Service](https://www.correios.com.br/). It runs on Python 3 and uses MongoDB.

[Try it!](http://telegram.me/RastreioBot)

## Setup

We use [Poetry](https://python-poetry.org/) to manage our dependencies. Check out its [Poetry guide](https://python-poetry.org/docs/#installation) to install it on your machine.

To install the required packages, use the command below. It will install the runtime and also the development dependencies (e.g. Pytest).

```
$ poetry install
```

Create a file `bot.conf` following `bot.conf_sample`.

`TOKEN` Bot token generated by BotFather

`int_check` Minimum interval between checks for the same package (3600 means 1 hour)

`*_log` Log files

`patreon` List of people that donate to the bot

`Banned` List of banned users

`usuario` User provived by Correios

`senha` Password provided by Correios

`token` Token provided by Correios

`key` Key provided by TrackingMore

`url` Sentry URL

### MongoDB

__RaspberryPi__
```
https://github.com/GabrielRF/Docker-MongoDB-RPi
```
__Mac__

```
brew install mongodb-community
brew services start mongodb-community
```

### SQLite


```
touch data_base.db
```

create db structure
```
CREATE TABLE assinantes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        chatid TEXT,
        picpayid TEXT);
```

## Commands available

```
$ poetry run rastreio --help
Usage: rastreio [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  packages:clean                  Clean old and duplicated packages
  packages:update                 Update active packages
  packages:delete <package-code>  Delete a package
  bot:run [--maintenance]         Set bot to maintenance mode
```

## Running tests

The tests are running on `pytest`, so, in order to run them, just do

```
poetry run pytest
```

## Contribute

Pull requests and issues are welcome!

## Contact

[Telegram](http://telegram.me/GabrielRF)

[Site](http://www.gabrf.com)
