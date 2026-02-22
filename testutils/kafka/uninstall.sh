#!/usr/bin/env bash

# Uninstall script for kafkacontainer
# Usage: ./uninstall.sh [-y]

AUTO_YES=false
if [ "$1" == "-y" ]; then
  AUTO_YES=true
fi

# Delete Kafka container
if [ "$AUTO_YES" = true ]; then
  kafkacontainer delete
else
  read -p "Delete Kafka container? [y/N] " answer
  if [[ "$answer" =~ ^[Yy]$ ]]; then
    kafkacontainer delete
  else
    echo "Skipping deletion."
  fi
fi

# Check for root
IS_ROOT=true
PROFILE_PATH=/etc/profile
if [ "$(id -u)" -ne 0 ]; then
  IS_ROOT=false
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
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)/scripts"
LINE_TO_REMOVE="export PATH=\"\$PATH:$SCRIPT_DIR\""

if grep -Fxq "$LINE_TO_REMOVE" $PROFILE_PATH; then
  if [ "$AUTO_YES" = true ]; then
    sed -i "\|$LINE_TO_REMOVE|d" $PROFILE_PATH
    echo "Removed '$LINE_TO_REMOVE' from $PROFILE_PATH."
  else
    read -p "Remove PATH entry '$LINE_TO_REMOVE' from $PROFILE_PATH? [y/N] " answer
    if [[ "$answer" =~ ^[Yy]$ ]]; then
      sed -i "\|$LINE_TO_REMOVE|d" $PROFILE_PATH
      echo "Removed."
    else
      echo "Skipping removal."
    fi
  fi
else
    echo "No PATH entry for $SCRIPT_DIR found in $PROFILE_PATH."
fi

echo "Done."

