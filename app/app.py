import flask

app = flask.Flask(__name__)

def foo():
    print('executing foo')
    result = 0
    for i in range(100000000):
        result = i*i
    print('end executing foo', result)
    return result

@app.route('/test/')
def test():
    import multiprocessing
    process = multiprocessing.Process(target=foo)
    process.start()
    print('returning ok')
    return 'ok'

