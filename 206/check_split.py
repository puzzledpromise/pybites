def check_split(item_total, tax_rate, tip, people):
    """Calculate check value and evenly split.

       :param item_total: str (e.g. '$8.68')
       :param tax_rate: str (e.g. '4.75%)
       :param tip: str (e.g. '10%')
       :param people: int (e.g. 3)

       :return: tuple of (grand_total: str, splits: list)
                e.g. ('$10.00', [3.34, 3.33, 3.33])
    """
    item_total_flt = float(item_total[1:])
    tax_rate_flt = float(tax_rate[:-1]) / 100
    tip_flt = float(tip[:-1]) / 100
    
    total_amount = round(item_total_flt * (1 + tax_rate_flt),2)
    total_amount = round(total_amount  * (1 + tip_flt),2)
    even_amount = round(total_amount / people,2)
    result = list()
    for i in range(people):
        result.append(even_amount)
    
    total_add = sum(result)
    diff = total_amount - total_add

    result[0] = round(result[0] + diff,2)
     
    return (f"${round(total_amount,2)}", result)

print(check_split('$141.86', '2%', '18%', 9))
