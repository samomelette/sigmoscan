#!/usr/bin/env bash

# Installation script
# Usage: ./install.sh [-y]

if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
  echo "Usage: ./install.sh [-y]"
  exit 0
fi

AUTO_YES=false
if [ "$1" == "-y" ]; then
  AUTO_YES=true
fi


# autodetect shell
if [ -n "$SHELL" ]; then
case "$SHELL" in
  */bash)
    PROFILE_PATH="$HOME/.bashrc"
    ;;
  */zsh)
    PROFILE_PATH="$HOME/.zshrc"
    ;;
  *)
    echo "Unknown shell: $SHELL"
    exit 1
esac
fi

# Detect where the script (kafkacontainer) is located
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)/scripts"
SCRIPT_PATH="${SCRIPT_DIR}/kafkacontainer"

if ! [ -f "$SCRIPT_PATH" ]; then
  echo "kafkacontainer not found in $SCRIPT_DIR"
  exit 1
fi

if [ "$AUTO_YES" = true ]; then
  chmod +x "$SCRIPT_PATH"
else
  read -p "Make kafkacontainer executable (chmod +x)? [y/N] " answer
  if [[ "$answer" =~ ^[Yy]$ ]]; then
    chmod +x "$SCRIPT_PATH"
  else
    echo "Skipping chmod."
  fi
fi

if [[ ":$PATH:" != *":$SCRIPT_DIR:"* ]]; then
  if [ "$AUTO_YES" = true ]; then
    echo "export PATH=\"\$PATH:$SCRIPT_DIR\"" >> $PROFILE_PATH
    echo "Added $SCRIPT_DIR to PATH in $PROFILE_PATH."
  else
    read -p "Add $SCRIPT_DIR to system PATH in $PROFILE_PATH? [y/N] " answer
    if [[ "$answer" =~ ^[Yy]$ ]]; then
      echo "export PATH=\"\$PATH:$SCRIPT_DIR\"" >> $PROFILE_PATH
      echo "Added $SCRIPT_DIR to PATH in $PROFILE_PATH."
    else
      echo "Skipping PATH update."
    fi
  fi
else
  echo "$SCRIPT_DIR already in PATH."
fi

echo "Done. To complete the installation, restart your shell or run 'source $PROFILE_PATH'"

