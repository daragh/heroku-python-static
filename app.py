import os


def file_paths(path):
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            yield os.path.join(dirpath, filename)


def app(environ, start_response):
    root = 'public'
    route = 'index.html' if environ['RAW_URI'] == '/' else environ['RAW_URI'][1:]
    routes = [path[len(root) + 1:] for path in file_paths(root)]
    (response, data) = (
        ('200 OK', open(os.path.join(root, route)).read()) if
        route in routes
        else ('404 Not Found', 'Not found.'))
    start_response(response, [('Content-Length', str(len(data)))])
    return iter([data])
