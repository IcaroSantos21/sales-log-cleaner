from io_handler import save_sales, load_sales
def remove_duplicates(list_sales):
    uniques_sales = {}
    for sale in list_sales:
        current_id = sale.get('id_pedido')
        if current_id not in uniques_sales:
            uniques_sales[current_id] = sale
    list_uniques_sales = list(uniques_sales.values())
    return list_uniques_sales

def order_sanitize(list_sale):
    for sale in list_sale:
        for key, item in sale.items():
            if isinstance(item, str):
                clean_item = item.strip()
                sale[key] = clean_item
    return list_sale