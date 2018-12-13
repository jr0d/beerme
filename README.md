# BeerMe

beerme is an untapped scraper for Big Hops locations in San Antonio, TX.
I built this utility because javascript page flipper is either too slow or too fast
(depending on which page you are looking at). Untapped does provide API access, but
only to certain individuals.

## Installation
```shell
$ pip install beerme
```

If that does not work, make sure you have python and pip installed. Also, you may need to use
sudo or the `--user` flag for `pip`

## Usage

This version of beerme only has `json` output support. I will add console formatted output
and the ability to filter, sort, and search at some point in the future. 

```
usage: beerme [-h] [--list] [-J] [--dump] [-p] [-d] [-f] [-s SEARCH]
              [-e EXCLUDE]
              [location]

BeerMe BigHops script 0.9

positional arguments:
  location              Beer target

optional arguments:
  -h, --help            show this help message and exit
  --list                list available locations
  -J, --json            Output information in json
  --dump                Dump the raw tap list html
  -p, --show-prices     Show price and volume data
  -d, --draft-only      Exclude bottles and cans
  -f, --fills-only      Only include beer that can be purchased in growlers
  -s SEARCH, --search SEARCH
                        A keyword to search for. For example: "IPA". This can
                        be used multiple times to create a compound search
  -e EXCLUDE, --exclude EXCLUDE
                        A keyword used to exclude results. For example:
                        "Sour". This can be used multiple times


```

## Notice

I do not represent Big Hops or Untapped in any way. Use this software at your own risk.

