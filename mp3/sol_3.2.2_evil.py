#!/usr/bin/python
# -*- coding: utf-8 -*-
from hashlib import sha256
good = "I come in peace."
evil = "Prepare to be destroyed!"
blob = """
                                                    �ˮQ�X:��Y��*=*���ð�?%���?M��
p�!=o����*�/#�lYu���2H4u?/
"?rH5r�En�R8�h�	F��Z�M���m�"�������@wfXJ�<fi7u�l.�8Ls�

"""
if sha256(blob).hexdigest() == '234ad6b2447eb9b10ec4dc702ec302fade2f412d4f51afb80674fc7cf4533078':
	print good
else:
	print evil
