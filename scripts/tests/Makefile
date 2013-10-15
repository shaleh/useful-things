clean:
	rm -f *~ *.pyc
	for i in $(PYTHON_UNITTESTS); do \
		test -e $$i.py && (test -L $$i.py && rm -f $$i.py); \
	done
