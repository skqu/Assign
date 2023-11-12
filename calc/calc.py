import operator

class CALC():
    def __init__(self) -> None:
        self.result = 0
        
    def calculate(self, expression):
        operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow
        }

        start = 0
        op = ""
        end = 0
        result = 0

        stack = []
        if type(expression) == str:
            tokens = expression.split()
        else:
            tokens = expression

        if "(" in tokens:
            start = tokens.index("(") + 1
            end = tokens.index(")")
            result = self.calculate(tokens[start:end])
            del tokens[start : end]
            tokens.remove("(")
            tokens.remove(")")
            start -= 1
        elif "^" in tokens:
            op = "^"
        elif "*" in tokens:
            op = "*"
        elif "/" in tokens:
            op = "/"
        elif "+" in tokens:
            op = "+"
        elif "-" in tokens:
            op = "-"
        else:
            tokens = []


        if op != "":
            start = tokens.index(op) - 1
            first = tokens[start]
            end = tokens.index(op) + 1
            second = tokens[end]
            del tokens[start : end + 1]
            result = operators[op](float(first), float(second))


        if len(tokens) >= 2:
            tokens.insert(start, result)
            result = self.calculate(tokens)
        return result


if __name__ == "__main__":
    calc = CALC()
    # TEST a
    a = ["2 + 3", "5 - 1", "4 * 6", "8 / 2"]
    # TEST b
    b = ["( 3 + 4 ) * 2", "( 6 - 2 ) / ( 3 + 1 )", "5 * ( 2 + 4 )", "7 / ( 3 - 1 )", "2 + 3 * 4"]
    # TEST c
    c = ["2 ^ 3", "4 ^ 0.5", "( 2 ^ 3 ) * ( 3 ^ 2 )", "( 4 ^ 2 ) / ( 2 ^ 2 )"]

    # Svar for test a
    answer_a = [5, 4, 24, 4.0]

    # Svar for test b
    answer_b = [14, 1.0, 30, 3.5, 14]

    # Svar for test c
    answer_c = [8, 2.0, 72, 4.0]


    tests =  [a, b, c]
    answers = [answer_a, answer_b, answer_c]
    for test in tests:
        for cal in test:
            j = test.index(cal)
            i = tests.index(test) 
            print(calc.calculate(cal), " result is " + str(answers[i][j])) 