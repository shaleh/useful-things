PYTHON_UNITTESTS = archiver link_farm new_password

unittest: python_unittests

python_unittests:
	for i in $(PYTHON_UNITTESTS); do \
		test -L $$i.py || ln -s $$i $$i.py; \
	done
	nosetests

clean:
	rm -f *~ *.pyc
	for i in $(PYTHON_UNITTESTS); do \
		if [ -e $$i.py ]; then \
			test -L $$i.py && rm -f $$i.py; \
		fi; \
	done
	make -C tests clean
