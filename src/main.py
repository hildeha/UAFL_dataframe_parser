from Parser.parser import ualf_dataframe_parser
import requests

def main():

    my_id = 'something' #add personal id

    client_id = my_id

    endpoint = 'https://frost.met.no/lightning/v0.ualf'
    parameters = {
        'referencetime': 'latest',
        'maxage': 'P1M',
        'geometry': 'POLYGON((4 58, 10 58, 15 64, 7 65))',

    }

    r = requests.get(endpoint, parameters, auth=(client_id, ''))

    myResponse = ualf_dataframe_parser(r)

    print(myResponse.dataframe())

    print(help(myResponse))


if __name__ == "__main__":
    main()