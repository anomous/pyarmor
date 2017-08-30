from distutils.util import get_platform

version = '3.0.1'

version_info = '''
Pyarmor is a tool used to import or run the encrypted python
scripts. Only by a few extra files, pyarmor can run and imported
encrypted files in the normal python environments. Here are the basic
steps:

- Generate project capsule
- Encrypt python scripts with project capsule
- Copy project capsule and encrypted scripts to runtime environments.

Pyarmor just likes an enhancement which let python could run or import
encrypted files.

'''

trial_info = '''
You're using trail version. Free trial version that never expires,
but project capsule generated is fixed by hardcode, so all the
encrypted files are encrypted by same key.

A registration code is required to generate random project
capsule. Visit
https://shopper.mycommerce.com/checkout/cart/add/55259-1 to purchase
one.

If you have received a registration code, just replace the content of
"license.lic" with registration code only (no newline).

'''

help_footer = '''
For more information, refer to https://github.com/dashingsoft/pyarmor
'''

# Extra suffix char for encrypted python scripts
ext_char = 'e'

# The last three components of the filename before the extension are
# called "compatibility tags." The compatibility tags express the
# package's basic interpreter requirements and are detailed in PEP
# 425(https://www.python.org/dev/peps/pep-0425).
platform = get_platform().replace('-', '_').replace('.', '_').lower()

dll_ext = '.so' if platform.startswith('linux') else '.dll'
dll_name = '_pytransform'

wrap_runner = '''
import pyimcore
from pytransform import exec_file
exec_file(%s)
'''