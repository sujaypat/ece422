#!/usr/bin/python
# -*- coding: utf-8 -*-
good = "I come in peace."
evil = "Prepare to be destroyed!"
blob = """
               �Kx^U����&�;�tQŠ0ёɸC�BmO�V����L�&k�R���T&T�`�����x�RͤL��������Ƴ��tWK���t*+� X`H��UX��a���Q[3�Q���mϺ �ZwI�j"""
from hashlib import sha256
print sha256(blob).hexdigest()
