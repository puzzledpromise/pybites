from os import path
from urllib.request import urlretrieve

import pandas as pd

EXCEL = path.join('/tmp', 'order_data.xlsx')
if not path.isfile(EXCEL):
    urlretrieve('https://bit.ly/2JpniQ2', EXCEL)


def load_excel_into_dataframe(excel=EXCEL):
    """Load the SalesOrders sheet of the excel book (EXCEL variable)
       into a Pandas DataFrame and return it to the caller"""
    df = pd.read_excel(EXCEL, sheet_name='SalesOrders')
    return df


def get_year_region_breakdown(df):
    """Group the DataFrame by year and region, summing the Total
       column. You probably need to make an extra column for
       year, return the new df as shown in the Bite description"""
    df.set_index('OrderDate',inplace=True)
    df['Year'] = df.index.year
    grpd = df.groupby(['Year','Region'])['Total'].sum()
    return grpd


def get_best_sales_rep(df):
    """Return a tuple of the name of the sales rep and
       the total of his/her sales"""
    max_s = df.groupby('Rep')['Total'].sum()
    return (max_s.idxmax(), max_s.max())


def get_most_sold_item(df):
    """Return a tuple of the name of the most sold item
       and the number of units sold"""
    max_i = df.groupby('Item')['Units'].agg(sum)
    return (max_i.idxmax(), max_i.max())

if __name__ == '__main__':
    df = load_excel_into_dataframe()
    print(df)
