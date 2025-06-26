#!/bin/bash

# Interpréteur strict
set -e

# Sélecteur de commande
case "$1" in
  run-tests)
    echo "Lancement des tests"
    exec pytest tests/
    ;;
  run-main)
    echo "Exécution de main.py..."
    exec python main.py
    ;;
  *)
    echo "Exécution personnalisée : python $@"
    exec python "$@"
    ;;
esac
