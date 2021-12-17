import pandas as pd
import numpy as np


class ualf_dataframe_parser():
    '''
    The purpose of the ualf_dataframe_parser is to parse a python requests response recieved in the
    universal ascii lightning format (ualf).

    A visual representation of the format can be found at the following link from the Norwegian
    Metrological Institute (MET Norway):

        -> https://frost.met.no/dataclarifications.html#ualf

    The class recieves a request response from the python requests package and parses the content response
    to a pandas dataframe object. Ensure that the requests package is correctly installed on you
    environment:

            -> https://docs.python-requests.org/
    '''

    def __init__(self, response):

        '''
        Creating class instance with attributes:

            self.response; request respons needed to instigate class object
            self.error; call raise_for_status method for the input response, erroneus response code
                        will cause 404 error to be raised.
        '''

        self.response = response
        self.error = response.raise_for_status()

    def parse_text_to_numpy(self):

        '''
        Method returns parsed numpy array of the request response text content
        '''

        try:
            return np.array([[float(x) if '.' in x else int(x) for x in [x.replace(' ', ',')][0].split(',')] \
                             for x in str(self.response.content)[2:-3].split('\\n')])
        except ValueError:
            print('Response could not be parsed to a numpy array. \nReview input data')

    def dataframe(self):

        '''
        Returns a pandas dataframe object from the parsed numpy array created with the
        parse_text_to_numpy method.
        '''

        columns = ['Version', 'Year', 'Month', 'Day of Month', 'Hour', 'Minute', 'Seconds',
                   'Nanoseconds', 'Latitude', 'Longitude', 'Peak Current', 'Multiplicity',
                   'Number of Sensors', 'Degrees of Freedom', 'Ellipse Angle', 'Semi-major Axis',
                   'Semi-minor Axis', 'Chi-square Value', 'Rise Time', 'Peak-to-zero Time',
                   'Max Rate-of-Rise', 'Cloud Indicator', 'Angle Indicator', 'Signal Indicator',
                   'Timing Indicator']

        int_columns = ['Version', 'Year', 'Month', 'Day of Month', 'Hour', 'Minute', 'Seconds',
                       'Nanoseconds', 'Peak Current', 'Multiplicity', 'Number of Sensors',
                       'Degrees of Freedom', 'Cloud Indicator', 'Angle Indicator', 'Signal Indicator',
                       'Timing Indicator']

        try:
            df = pd.DataFrame(self.parse_text_to_numpy(), columns=columns)

            for col in int_columns:
                df[col] = df[col].astype(int)

            return df
        except ValueError:
            print('Could not create pandas dataframe object from the input numpy array')
