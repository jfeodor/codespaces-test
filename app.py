import marimo

__generated_with = "0.3.9"
app = marimo.App(layout_file="layouts/app.grid.json")


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    mo.md("# test codespaces app")
    return


@app.cell
def __(mo):
    number = mo.ui.number(0, 10)
    number
    return number,


@app.cell
def __(mo):
    mo.md("some *markdown*")
    return


@app.cell
def __(number):
    number.value
    return


if __name__ == "__main__":
    app.run()
