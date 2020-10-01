# Python setup git reference

This is an example of [vcs
reference](https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support) in
[requirements.txt file](https://pip.pypa.io/en/latest/user_guide/#requirements-files):

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt 
Processing /home/martin/tvorba/python-setup-git-reference
Collecting kaptan from git+https://github.com/emre/kaptan.git#egg=kaptan (from -r requirements.txt (line 1))
  Cloning https://github.com/emre/kaptan.git to /tmp/pip-install-m0h_p3jp/kaptan
  Running command git clone -q https://github.com/emre/kaptan.git /tmp/pip-install-m0h_p3jp/kaptan
Collecting PyYAML<6,>=3.13 (from kaptan->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/64/c2/b80047c7ac2478f9501676c988a5411ed5572f35d1beff9cae07d321512c/PyYAML-5.3.1.tar.gz
Installing collected packages: PyYAML, kaptan, python-setup-git-reference
  Running setup.py install for PyYAML ... done
  Running setup.py install for kaptan ... done
  Running setup.py install for python-setup-git-reference ... done
Successfully installed PyYAML-5.3.1 kaptan-0.5.12 python-setup-git-reference-0.0.1
$ python setupgitreference.py 
20
```
