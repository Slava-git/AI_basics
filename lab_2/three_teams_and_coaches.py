from itertools import product
from logic import Symbol, Or, Not, And, Implication


def model_check(knowledge, symbols):

    for combination in product([True, False], repeat=len(symbols)):
        model = {symbol.name: value for symbol, value in zip(symbols, combination)}

        result = knowledge.evaluate(model)

        if result:
            return model  # Return the satisfying model

    return None


AntonioMilan = Symbol("AntonioMilan")
AntonioReal = Symbol("AntonioReal")
AntonioMetalist = Symbol("AntonioMetalist")
RodrigoMilan = Symbol("RodrigoMilan")
RodrigoReal = Symbol("RodrigoReal")
RodrigoMetalist = Symbol("RodrigoMetalist")
MykolaMilan = Symbol("MykolaMilan")
MykolaReal = Symbol("MykolaReal")
MykolaMetalist = Symbol("MykolaMetalist")


# Create the knowledge base
knowledge = And(
    # Each coach can only coach one team and vice versa
    Or(AntonioMilan, AntonioReal, AntonioMetalist),
    Or(RodrigoMilan, RodrigoReal, RodrigoMetalist),
    Or(MykolaMilan, MykolaReal, MykolaMetalist),
    Or(AntonioMilan, RodrigoMilan, MykolaMilan),
    Or(AntonioReal, RodrigoReal, MykolaReal),
    Or(AntonioMetalist, RodrigoMetalist, MykolaMetalist),

    # If a coach is coaching one team, they cannot coach the others
    # Antonio's constraints
    Implication(AntonioMilan, And(Not(AntonioReal), Not(AntonioMetalist))),
    Implication(AntonioReal, And(Not(AntonioMilan), Not(AntonioMetalist))),
    Implication(AntonioMetalist, And(Not(AntonioReal), Not(AntonioMilan))),
    # Rodrigo's constraints
    Implication(RodrigoMilan, And(Not(RodrigoReal), Not(RodrigoMetalist))),
    Implication(RodrigoReal, And(Not(RodrigoMilan), Not(RodrigoMetalist))),
    Implication(RodrigoMetalist, And(Not(RodrigoReal), Not(RodrigoMilan))),
    # Mykola's constraints
    Implication(MykolaMilan, And(Not(MykolaReal), Not(MykolaMetalist))),
    Implication(MykolaReal, And(Not(MykolaMilan), Not(MykolaMetalist))),
    Implication(MykolaMetalist, And(Not(MykolaReal), Not(MykolaMilan))),

    # Nationality constraints
    Not(AntonioMilan), Not(RodrigoReal), Not(MykolaMetalist),

    # Specific constraints
    Not(AntonioMetalist), Not(MykolaReal)
)



# List of all symbols
symbols = [
    AntonioMilan, AntonioReal, AntonioMetalist,
    RodrigoMilan, RodrigoReal, RodrigoMetalist,
    MykolaMilan, MykolaReal, MykolaMetalist
]


solution = model_check(knowledge, symbols)

# Print the solution
if solution is None:
    print("No valid solution found.")
else:
    for symbol in symbols:
        if solution[symbol.name]:
            print(f"{symbol} is True")