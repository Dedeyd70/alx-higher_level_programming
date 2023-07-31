#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        out_put = fct(*args)
    except Exception as d:
        sys.stderr.write("Exception: {}\n".format(d))
        out_put = None

    return (out_put)
