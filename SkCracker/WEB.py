# Python code obfuscated by sharif
 

import base64, codecs
magic = 'aW1wb3J0IHNvY2tldCxvcw0KDQpmcm9tIGNvbG9yYW1hIGltcG9ydCBGb3JlDQpmcm9tIGNvbG9yYW1hIGltcG9ydCBpbml0DQoNCiMgSW1wb3J0IE1vZHVsZXMNCmltcG9ydCBzeXMNCmltcG9ydCBvcw0KaW1wb3J0IHRpbWUNCg0KDQoNCiMgQ29sb3JzDQpjbGFzcyBDb2xvcnNDbGFzczoNCiAgICBDUkVEMiA9ICJcMzNbOTFtIg0KICAgIENCTFVFMiA9ICJcMzNbOTRtIg0KICAgIEVOREMgPSAiXDAzM1swbSINCiAgICBCT0xEID0gIlwwMzNbMW0iDQoNCm9zLnN5c3RlbSgnY2xlYXIgfHwgY2xzJykNCiMgYmFubmVyDQpiYW5uZXIgPSBmIiIiDQrilpHilojilojilojilojilojilojilZfilojilojilZfilpHilpHilojilojilZfilpHilojilojilojilojilojilZfilpHilojilojilojilojilojilojilZfilpHilojilojilZfilojilojilojilojilojilojilojilZcNCuKWiOKWiOKVlOKVkOKVkOKVkOKVkOKVneKWiOKWiOKVkeKWkeKWkeKWiOKWiOKVkeKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVkeKWiOKWiOKVlOKVkOKVkOKVkOKVkOKVnQ0K4pWa4paI4paI4paI4paI4paI4pWX4paR4paI4paI4paI4paI4paI4paI4paI4pWR4paI4paI4paI4paI4paI4paI4paI4pWR4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4pWR4paI4paI4paI4paI4paI4pWX4paR4paRDQrilpHilZrilZDilZDilZDilojilojilZfilojilojilZTilZDilZDilojilojilZHilojilojilZTilZDilZDilojilojilZHilojilojilZTilZDilZDilojilojilZfilojilojilZHilojilojilZTilZDilZDilZ3ilpHilpENCuKWiOKWiOKWiOKWiOKWiOKWiOKVlOKVneKWiOKWiOKVkeKWkeKWkeKWiOKWiOKVkeKWiOKWiOKVkeKWkeKWkeKWiOKWiOKVke'
love = 'XJvBXJvBXIxrXJxrXJxrXJvBXJvBXIxrXJvBXJvBXIxrXJvBXJvBXIxrXJxrXJxrXJxrXJxrXJxD0X4cJn4cJD4cJD4cJD4cJD4cJD4cJq4cnE4cJn4cJD4cJq4cnE4cnE4cJn4cJD4cJq4cJn4cJD4cJq4cnE4cnE4cJn4cJD4cJq4cJn4cJD4cJq4cnE4cnE4cJn4cJD4cJq4cJn4cJD4cJq4cJn4cJD4cJq4cnE4cnE4cnE4cnE4cnEQDbAPvNtVSEio2jtDaxtVSjjZmZtDSAlMauxrvNtKT4APyEbnKZtIT9ioPOWplOHo3EuoTk5VRMlMJHtFJLtJJ91VRWiqJqbqPOHnTymVSyiqFOUo3DtH2AuoJ1yMPNtVvVvQDbAPt0XMz9lVTAioPOcovOvLJ5hMKV6QDbtVPNtpUWcoaDbD29fo3WmD2kup3ZhD1WSEQVtXlOwo2jfVTIhMQ0vVvxAPvNtVPOmrKZhp3Exo3I0YzMfqKAbXPxAPvNtVPO0nJ1yYaAfMJIjXQNhZQNlAFxAPt0XLKI0nT9lFJ5zo3WgLKEco24tCFOzVvVvQDbgYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYD0XVPNtVPNtVPNtVPNtVPNtVRAbLJ5hMJjgYG4tqP5gMF9mpzMsL2ZtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVN0XVPNtVPNtVPNtVPNtVPNtVRqlo3IjVPNtYF0+VUDtoJHiL2uyL2gypy9wL3ZtVPNtVPNtVPNtVPNtVPNtVPNtQDbtVPNtVPNtVPNtVPNtVPNtG3qhMKVtVP0gCvO0Yz1yY3AlMauxrvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVN0XYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0tVvVvQDbAPt0XMz9lVTAioPOcovOuqKEbo3WWozMipz1uqTyiowbAPvNtVPOjpzyhqPuQo2kipaAQoTSmpl5QDxkIEGVtXlOwo2jfVTIhMQ0vVvxAPvNtVPOmrKZhp3Exo3I0YzMf'
god = 'dXNoKCkNCiAgICB0aW1lLnNsZWVwKDAuMDA0MCkNCg0KDQpsaW5lQnJlY2sgPSAiXG4iDQpmb3IgY29sIGluIGxpbmVCcmVjazoNCiAgICBwcmludChDb2xvcnNDbGFzcy5FTkRDICsgY29sLCBlbmQ9IiIpDQogICAgc3lzLnN0ZG91dC5mbHVzaCgpDQogICAgdGltZS5zbGVlcCgwLjQpDQoNCm9zLnN5c3RlbSgnY2xlYXIgfHwgY2xzJykNCmluaXQoKQ0KZGVmIElwcyhzaXRlKToNCiAgICBnbG9iYWwgdGV4dA0KDQogICAgdGV4dCA9IG9wZW4oIndlYnNpdGVUb0lQLnR4dCIsImEiKQ0KICAgIA0KICAgIHRyeToNCg0KICAgICAgICBpZiBzaXRlIGluICJodHRwOi8vIiBvciAiaHR0cHM6Ly8iOg0KDQogICAgICAgICAgICB1cmwgPSBzaXRlLnJlcGxhY2UoImh0dHA6Ly8iLCIiKS5yZXBsYWNlKCJodHRwczovLyIsIiIpLnJlcGxhY2UoJy8nLCAnJykNCg0KICAgICAgICBlbGlmICIvIiBpbiBzaXRlOg0KDQogICAgICAgICAgICB1cmwgPSBzaXRlLnJlcGxhY2UoJy8nLCAnJykNCg0KICAgICAgICBfMHgzN1UgPSBzb2NrZXQuZ2V0aG9zdGJ5bmFtZSh1cmwpDQogICAgICAgIHRleHQud3JpdGUoXzB4MzdVKyJcbiIpDQogICAgICAgIHByaW50KEZvcmUuR1JFRU4rIlRvb0wgQlkgU2hhcmlmIisoRm9yZS5MSUdIVFdISVRFX0VYKyIgPj4gIikrXzB4MzdVKQ0KDQogICAgZXhjZXB0Og0KICAgICAgICBwYXNzDQoNCklucHV0ID0gaW5wdXQoRm9yZS5HUkVFTisnJydMb2dpbiBTdWNlc3MNClwwMzNbMzVtDQrilpHilojilojilojilojilojilojilZfilojilojilZfilpHilpHilojilojilZfilpHilojilojilojilojilojilZfilpHilojilojilojilojilojilojilZfilpHilojilojilZfilojilojilojilojilojilojilojilZcNCuKWiOKWiOKVlOKVkOKVkOKVkOKVkOKVneKWiOKWiOKVkeKWke'
destiny = 'XJxrXJvBXJvBXIxrXJvBXJvBXIyBXIxBXIxBXJvBXJvBXIy+XJvBXJvBXIyBXIxBXIxBXJvBXJvBXIy+XJvBXJvBXIxrXJvBXJvBXIyBXIxBXIxBXIxBXIxBXIaD0X4cJn4cnV4cnV4cnV4cnV4cnV4cJK4cnE4cnV4cnV4cnV4cnV4cnV4cnV4cnV4cJE4cnV4cnV4cnV4cnV4cnV4cnV4cnV4cJE4cnV4cnV4cnV4cnV4cnV4cnV4cJH4cJq4cnV4cnV4cJE4cnV4cnV4cnV4cnV4cnV4cJK4cnE4cnEQDevycUvyMevyMQvyMQvyMQvybwvybwvyMsvybwvybwvyMGvyMQvyMQvybwvybwvyMUvybwvybwvyMGvyMQvyMQvybwvybwvyMUvybwvybwvyMGvyMQvyMQvybwvybwvyMsvybwvybwvyMUvybwvybwvyMGvyMQvyMQvyM3vycUvycRAPhXJvBXJvBXJvBXJvBXJvBXJvBXIyBXIarXJvBXJvBXIxrXJxrXJxrXJvBXJvBXIxrXJvBXJvBXIxrXJxrXJxrXJvBXJvBXIxrXJvBXJvBXIxrXJxrXJxrXJvBXJvBXIxrXJvBXJvBXIxrXJvBXJvBXIxrXJxrXJxrXJxrXJxrXJxD0X4cJn4cJD4cJD4cJD4cJD4cJD4cJq4cnE4cJn4cJD4cJq4cnE4cnE4cJn4cJD4cJq4cJn4cJD4cJq4cnE4cnE4cJn4cJD4cJq4cJn4cJD4cJq4cnE4cnE4cJn4cJD4cJq4cJn4cJD4cJq4cJn4cJD4cJq4cnE4cnE4cnE4cnE4cnEQDbAPvNtVSAjMJAcLJjtqTuuozgmVSjjZmAoZmIgDSAlMauxrt0XVPNtQDbtVPNAPvNtVN0XVPNtQDbtVPNAPvNtVRIBIRIFVSyCIIVtIIWZVRkWH1Dt4bPv4bPv4bPv4bPv4bPv4bPv4bPv4bPvCvpaWlxhp3ElnKNbXFNtQDbAPxkWH1DtCFOipTIhXRyhpUI0YPWlVvxhpzIuMPtcYaWmpTkcqPtvKT4vXD0XQDczo3Vtp2y0MKZtnJ4tGRyGIQbAPvNtVPOWpUZbp2y0MKZhp3ElnKNbXFxAPaOlnJ50XPV8CG09CG09CFOQnTIwnlO3MJWmnKEyIT9WHP50rUDtEzyfMFN9CG09CG09CvVcQDc0MKu0YzAfo3AyXPxAPt=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))