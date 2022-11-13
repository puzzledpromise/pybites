import typer


def sum_numbers(a: int, b: int):
    return a + b


# TODO: initialize the app
app = typer.Typer() 

# TODO: decorate this
@app.command()
def sum(
    a,  # TODO: edit this
    b,  # TODO: edit this
):
    """Command that allows you to add two numbers."""
    sum_ab = sum_numbers(a, b)

    print(f"The sum is {sum_ab}")


# TODO: decorate this
@app.command()
def compare(
    c,  # TODO: edit this
    d,  # TODO: edit this
):
    """Command that checks whether a number d is greater than a number c."""

    STRING_TRUE = "greater"
    STRING_FALSE = "not greater"

    c_evaluation = STRING_TRUE if d > c else STRING_FALSE

    print(f"{d=} is {c_evaluation} than {c=}")


if __name__ == "__main__":
    app()