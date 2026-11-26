CXX = g++
CXXFLAGS = -O2 -std=c++11 -Wall -Wextra -Wpedantic

.PHONY: all clean
all: code

code: main.cpp
	$(CXX) $(CXXFLAGS) main.cpp -o code

clean:
	rm -f code
