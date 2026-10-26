from datetime import date
from http.server import HTTPServer, BaseHTTPRequestHandler

NAME = "Abdul Rahman"
GREETING = "Hello"
PORT = 8080


class Greeter(BaseHTTPRequestHandler):
    def do_GET(self):
        page = f"""<!doctype html>
<html>
  <body style="font-family: sans-serif; text-align: center; margin-top: 80px;">
    <h1>{GREETING}, {NAME}!</h1>
    <p>Today is {date.today():%A, %d %B %Y}.</p>
  </body>
</html>"""
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(page.encode("utf-8"))


if __name__ == "__main__":
    print(f"Greeter running on http://localhost:{PORT}", flush=True)
    HTTPServer(("0.0.0.0", PORT), Greeter).serve_forever()
