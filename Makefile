VIRTUAL_ENV=venv

${VIRTUAL_ENV}:
	virtualenv ${VIRTUAL_ENV} -p python3.6
	(source ${VIRTUAL_ENV}/bin/activate; pip install -r requirements.txt;)

.PHONY: virtualenv
virtualenv: ${VIRTUAL_ENV}

.PHONY: freeze
freeze:
	(source ${VIRTUAL_ENV}/bin/activate; pip freeze > requirements.txt; )

.PHONY: clean
clean:
	rm -rf ${VIRTUAL_ENV}
	rm -rf files/

.PHONY: setup
setup: virtualenv