VERSION="1.0"

echo INSTALLING "Empyrean-$VERSION"

echo BUILDING EMPYREAN

python setup.py sdist

echo CREATING VIRTUAL ENVIORNMENT

python -m venv .venv

echo INSTALLING EMPYREAN INTO VITRUAL ENVIORNMENT

.venv/bin/python -m pip install "dist/empyrean-$VERSION.tar.gz"

echo VIRTUAL ENVIORNMENT CREATED FOR EMPYREAN, USE .venv/bin/activate TO ACTIVATE, deactivate TO DEACTIVATE
