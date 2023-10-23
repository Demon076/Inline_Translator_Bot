import urllib.request
from pathlib import Path

# Install it
from argostranslate import package

from app.utils.root_dir import root_path

package.install_from_path(Path('translate-ru_en-1_0.argosmodel'))
