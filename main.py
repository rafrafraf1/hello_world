__import__("sys").excepthook = lambda t, v, tb: ( print( (cd[0].replace("_", " ") if (cd := __import__("traceback").format_tb(tb)[0].split('\n')[-2].strip().split("("))[1][1:-2] == "print" else "") if t == NameError else "")  )

Hello_World('print')