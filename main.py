from decotest import Decotest


# Example usage
DECO_TEST = Decotest()



@DECO_TEST.unittest(name="Test addition")
@DECO_TEST.assert_eq(2)
def addition(x, y):
    return x + y

@DECO_TEST.unittest(name="Test nene")
@DECO_TEST.assert_eq(30)
def number_2(x):
    return x

@DECO_TEST.assert_in(3)
def number_list():
    return [0, 5, 0]

if __name__ == "__main__":
    addition(1, 1)  # Now you can pass parameters
    number_2(30)
    number_list()
    DECO_TEST.run_all_tests()
