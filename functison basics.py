import math
def print_hello():
    """print Heloo at screen."""
    print("hello")
def get_hello() -> str:
    """
    return hello string.

    :return: Returns String value
    """
    return "hello"
def ask_name_and_greet_user():
    """ask user name and print question"""
    name = input("insert your name please:")
name = name.capitalize()
if name =="Thanos":
    print("et out of here, Thanos! Nobody wants to play with you!")
else:
    print(f"Hi, {name}. Would you like to have a hamburger?")



    def calculate_hypotenuse_length(a: int, b: int) -> float:
        """
        calculate hypothenuse length

        :param a: interger value
        :param b: integer value
        :return: float value - calculate length
        """
        c = math.sqrt(a ** 2 + b ** 2)
        return c
def calculate_cathetus_length(a: int, c: int)->:
    """
    calculate catheus length
    :param a: integer value catheus
    :param c: integer value hypotenuse
    :return: float value -calculated length
    """
    b=math.sqrt(c ** 2 - a **2 )
    return b
    result = calculate_cathetus_length(3, 5)
    print(result)
    result = calculate_cathetus_length(3, 4)
    print(result)

#print_hello()
#greeting = get_hello()
#print(greeting)
