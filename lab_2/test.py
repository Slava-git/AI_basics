from logic import Symbol, Or, Not, And, Implication

def simplified_model_check(knowledge, symbols):
    from itertools import product

    print("Knowledge:", knowledge)

    for combination in product([True, False], repeat=len(symbols)):
        model = {symbol.name: value for symbol, value in zip(symbols, combination)}

        # Debugging: Print the model and evaluation result
        result = knowledge.evaluate(model)
        print("Testing model:", model, "Result:", result)

        if result:
            return model  # Return the satisfying model

    return None

A = Symbol("A")
B = Symbol("B")
simplified_knowledge = Or(A, B)
simplified_symbols = [A, B]
model = simplified_model_check(simplified_knowledge, simplified_symbols)
print("Satisfying model:", model)