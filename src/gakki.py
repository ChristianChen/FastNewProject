def gakki(*args):
    if len(args) == 0:
        return dict(code=-1, msg='''Usage:
gakki <java|python|node> [optional libraries]''')
