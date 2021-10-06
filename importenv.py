# -*- coding: utf-8 -*-
import os
from os.path import join, dirname
from enum import Enum

import sys
sys.path.append('./python-dotenv')

from dotenv import load_dotenv

class ImportEnvKeyEnum(Enum):
  """ .envファイルのキーを書く """
  GIT_REPOSITORY_URL="GIT_REPOSITORY_URL"
  GIT_DIRECTORY="GIT_DIRECTORY"

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ENV_DIC = {}

for e in ImportEnvKeyEnum:
  ENV_DIC[e.value] = os.environ.get(e.value)