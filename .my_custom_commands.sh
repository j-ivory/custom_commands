#!/bin/bash

function greet_me() {
  echo 'Hello James. Today is going to be a great day.' $1
}

function good_morning() {
    greet_me 
}

function create() {
  activate_Create_venv
  cd /Users/james/Documents/Projects/MyProjects/create_command 
  python3 create.py $1
  cd /Users/james/Documents/Projects/MyProjects/$1
  git init
  git remote add origin https://github.com/jimmyjohn89/$1.git
  touch README.md
  git add .
  git commit -m "Initial commit"
  git push -u origin master
  code .
  deactivate
}

function activate_Create_venv() {
  cd /Users/james/Documents/Projects/MyProjects/create_command/Create_venv
  source bin/activate
}

function boniver() {
  activate_Create_venv
  cd /Users/james/Documents/Projects/MyProjects/create_command 
  python3 boniver.py
  cd ~
}