#!/usr/bin/env just --justfile
name := "jcode"
description := '''
This is the just file for the 
{{name}} file
'''
version := "0.0.1"
set allow-duplicate-recipes
set positional-arguments
set export
root := justfile_directory()
fzf_installed := if `command -v fzf || true` == "" { "false" } else { "true" }

# Build and test
default: build run test
@build:
  true
@run:
  python3 -m jcode
test *args='':
  #!/usr/bin/env bash
  pytest {{ args }}
  if [ $? -eq 0 ]; then
    if ! [ -f build/.pass ]; then
      read -p "Pass commit comment: " COMMENT
      just _git_push_pass "${COMMENT}"
      rm build/.fail || true
      touch build/.pass
    fi
  else
    if ! [ -f build/.fail ]; then
      read -p "Fail commit comment: " COMMENT
      just _git_push_fail "${COMMENT}"
      rm build/.pass || true
      touch build/.fail
    fi
  fi
# Select an option from the menu
menu: _check_os
  #!/usr/bin/env bash
  just --choose
# default help text
help:
  #!/usr/bin/env bash
  just --evaluate name
  just --evaluate version
  just --evaluate description  
  just --list --unsorted --list-prefix '|   ' --list-heading $'\n{{name}} {{version}}:\n'
auto_rebase: _commit_squash_warnings
  git rebase -i --autosquash ${git_head}
_commit_squash_warnings:
  git log --pretty='format:%h %s' | awk '{if ( $2 == ":warning:" ) { print "git commit --squash "$1 }}' | sh || true
# Push all updates to git
_git_push *args='update':
  git add -A
  git commit -m "{{ args }}"
  git push
# manual push :see_no_evil: :hear_no_evil: :speak_no_evil: :pray:
git_push *args="And I did not write a comment :cry:":
  just _git_push ":see_no_evil: I did not test this." {{ args }}
# push on fail
_git_push_fail *args="The test failed, and I did not write a comment :cry:":
  just _git_push ":warning:" {{ args }}
# push on pass
_git_push_pass *args="The test passed, but I did not write a comment :cry:":
  just _git_push ":white_check_mark:" {{ args }}

# multi arg test
@_multi *args='':
  #!/usr/bin/env bash
  bash -c 'while (( "$#" )); do echo - $1; shift; done' -- "$@"


[macos]
@_check_os: && _install_deps
[macos]
@_install_deps:
  #!/usr/bin/env zsh
  exit 0 || echo {{fzf_installed}}
  # TODO: add to zshrc
  alias j=just
  eval "$(brew shellenv)"
  fpath=($HOMEBREW_PREFIX/share/zsh/site-functions $fpath)
  autoload -U compinit
  compinit
[linux]
@_check_os:
  echo "Linux not tested" && exit 1
[windows]
@_check_os:
  echo "Windows not tested" && exit 1