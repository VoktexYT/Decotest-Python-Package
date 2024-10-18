all_test = []
all_test_pass = True

class Decotest:
    def __init__(self):
        self.generate_assert()
        self.currentTestName = ""

    def run_all_tests(self):
        max_len = max([len(x.get("name")) for x in all_test]) + 2
        for test in all_test:
            passed = test.get("passed")
            name = test.get("name")
            values = test.get("values")
            PASSED_MSG = "PASS"
            NOT_PASSED_MSG = "BAD"

            print("+----+----+" + "=" * max_len)

            if passed:
                print(f"|\033[92m{PASSED_MSG}\033[0m|    |", name)
            else:
                all_test_pass = False
                print(f"|    |\033[91m{NOT_PASSED_MSG}\033[0m |", name)
                print("\n")
                print(f" {name} :  {values[1]}, expected value {values[0]}")
                print("\n")

        print("+----+----+" + "=" * max_len)

        return all_test_pass

    def unittest(self, name: str):
        self.currentTestName = name
        def wrapper(func):
            def inner(*args, **kwargs):
                result = func(*args, **kwargs)
                return result
            return inner
        return wrapper

    def assertion_generator(self, operator):
        def wrapper(expected_value):
            def decorator(func):
                def inner(*args, **kwargs):
                    result = func(*args, **kwargs)
                    passed = eval(f"expected_value {operator} result")
                    all_test.append({
                        "name": self.currentTestName,
                        "passed": passed,
                        "values": [expected_value, result]
                    })
                    return result
                return inner
            return decorator
        return wrapper
    
    def generate_assert(self):
        self.assert_eq = self.assertion_generator("==")
        self.assert_neq = self.assertion_generator("!=")
        self.assert_lt = self.assertion_generator("<")
        self.assert_le = self.assertion_generator("<=")
        self.assert_gt = self.assertion_generator(">")
        self.assert_ge = self.assertion_generator(">=")

        self.assert_in = self.assertion_generator("in")
        self.assert_not_in = self.assertion_generator("not in")
        self.assert_is = self.assertion_generator("is")
        self.assert_is_not = self.assertion_generator("is not")
        self.assert_and = self.assertion_generator("and")
        self.assert_or = self.assertion_generator("or")
