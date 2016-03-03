def app(environ, start_response):
      with open('public/index.html') as f:
        data = f.read()
      start_response("200 OK", [
          ("Content-Type", "text/html"),
          ("Content-Length", str(len(data)))
      ])
      return iter([data])

