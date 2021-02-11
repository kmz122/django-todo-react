import os
from pathlib import Path

PROJ_ROOT = Path(__file__).resolve().parent.parent.parent
# frontend = PurePosixPath(SITE_ROOT).joinpath('frontend')

PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))

print("site root", PROJ_ROOT)
print("project path", PROJECT_PATH)
print("frontend: ", os.path.join(PROJECT_PATH))
# fe = PROJ_ROOT/frontend/

BUILD_PATH = "/media/kyi/D/projects/djangoProjects/django-todo-react/frontend/build"
print(Path(BUILD_PATH))

print("BASE_DIR", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print("aa: ", os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))), 'build'))
