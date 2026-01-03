from io_handler import save_sales, load_sales
def remove_duplicates(list_sales):
    uniques_sales = {}
    for sale in list_sales:
        current_id = sale.get('id_pedido')
        if current_id not in uniques_sales:
            uniques_sales[current_id] = sale
    list_uniques_sales = list(uniques_sales.values())
    return list_uniques_sales

