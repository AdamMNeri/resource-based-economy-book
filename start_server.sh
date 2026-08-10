#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

echo "Building RBE Book reader edition on capevm1..."
python3 prepare_book.py
~/.cargo/bin/mdbook build

echo "Starting always-on static web server on port 3000..."
# Kill any existing server on port 3000
fuser -k 3000/tcp || true

nohup python3 -m http.server 3000 --directory book > server.log 2>&1 &
echo "Server started successfully on http://192.168.85.105:3000"
