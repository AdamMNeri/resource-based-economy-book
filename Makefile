.PHONY: all build serve clean

all: build

build:
	python3 prepare_book.py
	mdbook build

serve:
	python3 -m http.server 3000 --directory book

clean:
	rm -rf book src
