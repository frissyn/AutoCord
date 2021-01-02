from web import app


def status_color(s):
    c = {
        "offline": "black",
        "online": "primary",
        "dnd": "danger",
        "idle": "warning",
        "True": "primary",
        "False": "danger",
    }

    try:
        return c[str(s)]
    except KeyError:
        return "light"


@app.context_processor
def inject_builtins():
    return dict(int=int, str=str, list=list, len=len)


@app.context_processor
def inject_functions():
    return dict(status_color=status_color)
