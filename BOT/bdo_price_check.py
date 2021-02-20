import requests
import re


class BdoProfit:
    """Bdo class."""

    @staticmethod
    def price_check_time(link):
        """Convert link to the cost string."""
        bdo_request1 = requests.get(link)
        current_price1 = bdo_request1.text
        pattern = r'("EU":)+\W+\d+\W+\d+\W+'  # looking for "EU":[["itemPrice","itemQuantity"]], part
        looking_for_match = (re.search(pattern, current_price1))  # actual search process, get re.search object
        pre_format_data = looking_for_match.group().split(',')  # turn re.search object in string, then turn it to list
        formatted_price = (pre_format_data[0])[8:-1]
        return [formatted_price, (pre_format_data[1])[1:-3]]

    @staticmethod
    def check_profit(number):
        """Calculates profit for the grind"""
        money_plus = (89 * int(BdoProfit.price_check_time('https://bdocodex.com/us/item/4901/')[0]) - int(number))
        taxes = [0.845, 0.65]
        return [round(money_plus * taxes[0]), round(money_plus * taxes[1])]

    @staticmethod
    def formatted():
        """Return formatted string"""
        bsp_price = BdoProfit.price_check_time('https://bdocodex.com/us/item/4901/')[0]
        harphia_price = BdoProfit.price_check_time('https://bdocodex.com/us/item/15601/')
        viper_price = BdoProfit.price_check_time('https://bdocodex.com/us/item/15603/')
        harphia_profit = BdoProfit.check_profit(harphia_price[0])
        viper_profit = BdoProfit.check_profit(viper_price[0])
        return f"Black stone powder price is {bsp_price}\n" \
               f"Harphia price is {harphia_price[0]}, {harphia_price[1]} on stock\n" \
               f"Viper price is {viper_price[0]}, {viper_price[1]} on stock\n" \
               f"Harphia profit vp/nonvp is {harphia_profit[0]}/{harphia_profit[1]}\n" \
               f"Viper profit vp/nonvp is {viper_profit[0]}/{viper_profit[1]}"