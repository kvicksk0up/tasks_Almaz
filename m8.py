def render_in(func):
    def render_output(field):
        r = func(field)
        n = f'"<p>"{r}"</p>"'
        return n, print(n)

    return render_output

@render_in
def render(field):
    return f'<input id="id_{field}" name="{field}">'


render('username')