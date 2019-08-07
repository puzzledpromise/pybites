from decimal import *

def check_split(item_total, tax_rate, tip, people):
    """Calculate check value and evenly split.

       :param item_total: str (e.g. '$8.68')
       :param tax_rate: str (e.g. '4.75%)
       :param tip: str (e.g. '10%')
       :param people: int (e.g. 3)

       :return: tuple of (grand_total: str, splits: list)
                e.g. ('$10.00', [3.34, 3.33, 3.33])
    """
    item_total_dec = Decimal(item_total[1:])
    tax_rate_dec = Decimal(tax_rate[:-1]) / Decimal(100)
    tip_dec = Decimal(tip[:-1]) / Decimal(100)
    
    total_amount = round(item_total_dec * (Decimal(1) + tax_rate_dec),2)
    total_amount = round(total_amount  * (Decimal(1) + tip_dec),2)
    even_amount = round(total_amount / Decimal(people),2)

    result = list()
    
    for i in range(people):
        result.append(even_amount)

    total_add = sum(result)
    diff = round(total_amount - total_add,2)

    result[0] = result[0] + diff
    print(result)
    rs = (f"${sum(result)}", result)
    return rs

if __name__ == '__main__':
    item_total = '$141.86'
    tax_rate = '2%'
    tip = '18%'
    people = 9

    grand_total, splits = check_split(item_total, tax_rate, tip, 9)
    print(grand_total)
    print(f'${sum(splits)}')
