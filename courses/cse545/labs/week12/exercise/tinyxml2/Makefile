all: xmltest harness
xmltest:
	$(CXX) xmltest.cpp tinyxml2.cpp tinyxml2.h -o xmltest
harness:
	$(CXX) harness.cpp tinyxml2.cpp tinyxml2.h -o harness
test: clean xmltest
	./xmltest 
clean:
	rm -f *.o xmltest harness
