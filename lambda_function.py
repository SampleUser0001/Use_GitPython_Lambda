# -*- coding: utf-8 -*-
import sys
sys.path.append('./GitPython')

import git

from importenv import ImportEnvKeyEnum
import importenv as setting

def lambda_handler(event, context):
  # cloneするURL
  # GIT_REPOSITORY_URL=https://github.com/SampleUser0001/cloud9_note.git
  
  # cloneしたリポジトリの取得ディレクトリ。
  # GIT_DIRECTORY=cloud9_note

  url = 'https://github.com/SampleUser0001/cloud9_note.git'
  to_path = './repo/cloud9_note'

  git.Repo.clone_from(
    url,
    to_path)
  
  repo = git.Repo(to_path)

  t = repo.head.commit.tree
  # print(repo.git.diff('HEAD^'))

  return {
    'statusCode': 200,
    'body': repo.git.diff('HEAD^')
  }
  