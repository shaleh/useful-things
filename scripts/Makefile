PYTHON_UNITTESTS = archiver hasher link_farm new_password

unittest: python_unittests

python_unittests:
	for i in $(PYTHON_UNITTESTS); do \
		test -L $$i.py || ln -s $$i $$i.py; \
	done

	nosetests -x -s --with-coverage --cover-package="$(shell echo $(PYTHON_UNITTESTS) | sed -e 's/ /,/g')"

clean:
	rm -f *~ *.pyc
	for i in $(PYTHON_UNITTESTS); do \
		if [ -e $$i.py ]; then \
			test -L $$i.py && rm -f $$i.py; \
		fi; \
	done
	make -C tests clean
