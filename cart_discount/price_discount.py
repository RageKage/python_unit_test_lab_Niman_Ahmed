def main():
    print(discount(["a", 2, 3]))  # Expect this to print 4
    # what other lists might this function be called with?


class NotNumberError(Exception):
    """ Custom exception class """
    pass

def discount(item_prices):
    """Complete this function that returns the discount earned for a list of item prices
    If a customer has ordered more than three items, the cheapest item is free.
    Example: if this function is called with a list of [10, 4, 20] then return 4.
    """

    for i in item_prices:
        if not isinstance(i, (int, float)):
            raise NotNumberError("anything not a number will not be processed")
        if i <= 0:
            raise ValueError("It has to be positive ")

    if len(item_prices) >= 3:
        return sorted(item_prices)[0]
    else:
        return None
    

if __name__ == "__main__":
    main()
