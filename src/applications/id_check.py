# source: https://jigarius.com/blog/shopify-software-developer-interview


def create_id(first_name, last_name, join_date):
    '''
    join_date is in format YYMMDD
    example: Mike, Smithe, 20230115 -> ms20230115
    sum digits at odd positions: 2+2+0+1+5 = 10
    sum digits at even positions: 0+3+1+1+5 = 10
    verification digit = subtract odd - even = 0
    final id: ms202301150 (with verification digit at end)
    '''

    sum_even = sum(int(join_date[i]) for i in range(1, len(join_date), 2))
    sum_odd = sum(int(join_date[i]) for i in range(0, len(join_date), 2))
    verification_digit = abs(sum_odd - sum_even)

    return first_name[0].lower() + last_name[0].lower() + join_date + str(verification_digit)

def check_id(first_name, last_name, join_date, id_to_check):
    return create_id(first_name, last_name, join_date) == id_to_check


if __name__ == "__main__":
    print(create_id("Mike", "Smithe", "20230115"))  # ms20230115
    print(check_id("Mike", "Smithe", "20230115", "ms202301154"))  # True
    print(check_id("Mike", "Smithe", "20230115", "ms202301151"))  # False