.PHONY: all clean

build.pyxapp: $(wildcard game_of_life/*.py) main.py pyproject.toml poetry.lock
	rm -rf build
	mkdir build
	cp main.py build/main.py
	cp -r game_of_life build/game_of_life
	poetry run pyxel package build build/main.py

build.html: build.pyxapp
	poetry run pyxel app2html build.pyxapp

all: build.html

clean:
	rm -rf build
	rm -f build.pyxapp
	rm -f build.html

run:
	poetry run app
