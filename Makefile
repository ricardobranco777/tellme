test:
	@pylint tellme --disable=raise-missing-from
	@flake8 tellme --ignore=E501
