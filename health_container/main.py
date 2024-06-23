import argparse
from aiohttp import web
from views.handlers import health


app = web.Application()
app.add_routes([web.get("/health", health)])

parser = argparse.ArgumentParser(description="aiohttp server")
parser.add_argument("--path")
parser.add_argument("--port")

if __name__ == "__main__":
    args = parser.parse_args()
    web.run_app(app, path=args.path, port=int(args.port))
