What is __init__.py?
math_utils.py → Module 📄
security_tools/ → Package 📁


What does __init__.py do?
__init__.py is a special Python file associated with a package.
Traditionally, its presence tells Python:
“Treat this directory as a Python package.”
Modern Python can also support some packages without it (namespace packages), but for our projects, we'll use it because it makes the package structure explicit and can control what the package exposes.

Why can it be empty?
For now, we don't need the package to perform anything during initialization.
So an empty:__init__.py
is completely valid. ✅
Later, you can put imports inside it to make package usage cleaner, such as:
from .password_utils import check_password
