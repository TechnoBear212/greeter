# greeter

A tiny Python web page (standard library `http.server`, no framework) that greets Abdul Rahman and shows today's date. It listens on port 8080.

## Build and run with Docker

```bash
docker build -t greeter .
docker run -d -p 8080:8080 greeter
```

Then open http://localhost:8080.
