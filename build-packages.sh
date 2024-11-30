#!/bin/bash

echo "Building all projects"
for dir in projects/*; do (
    cd "$dir"
    poetry build-project
); done
