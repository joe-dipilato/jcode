#!/usr/bin/env bash
yq '.' -o=json syntaxes/jcode.tmLanguage.yml > syntaxes/jcode.tmLanguage.json
