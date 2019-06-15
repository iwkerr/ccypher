
########## CCYPHER #############

--README--

CCypher is used to encrypt or decrypt entered text into an output text box.


####### CCYPHER PACKAGE UPGRADE #########

--Change to root directory of package file:
'cd /Users/<USERNAME>/<PATH>/<TO>/ccypher'

--Run below script in root of package folder:
'python setup.py sdist'

--* Make sure 'twine' is installed. *
--* In case you need to know the 'twine' install command, run: *
--* 'pip install twine' *

--Then, run the below script to update package:
'twine upload dist/*'

--After running above script, enter PYPI username and password.