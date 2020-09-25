test:
	@pylint tellme --disable=line-too-long
	@flake8 tellme --ignore=E501
