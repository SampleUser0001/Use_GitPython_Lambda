# -*- coding: utf-8 -*-
import sys
sys.path.append('./GitPython')

import git

from importenv import ImportEnvKeyEnum
import importenv as setting

def lambda_handler(event, context):
  url = setting.ENV_DIC[ImportEnvKeyEnum.GIT_REPOSITORY_URL.value]
  to_path = './repo/' + setting.ENV_DIC[ImportEnvKeyEnum.GIT_DIRECTORY.value]

  repo = git.Repo.clone_from(
    url,
    to_path)

  for commit in repo.iter_commits('master'):
    print(commit.author,
      commit.committed_datetime,
      commit.hexsha)
    
