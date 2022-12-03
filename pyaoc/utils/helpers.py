def converter(x : int , base : int = 2) -> int:
    """Convert from any base to decimal"""
    return sum([int(d)*base**i for i , d in enumerate(str(x)[::-1])])
