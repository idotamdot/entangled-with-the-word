# gospel/old_testament/__init__.py

from .genesis import render_genesis
from .psalms import render_psalms  
from .ecclesiastes import render_ecclesiastes
from .isaiah import render_isaiah
from .daniel import render_daniel

__all__ = [
    'render_genesis',
    'render_psalms', 
    'render_ecclesiastes',
    'render_isaiah',
    'render_daniel'
]