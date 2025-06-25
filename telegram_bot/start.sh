#!/usr/bin/env bash
set -e

# Переходим в папку с ботом
cd "$(dirname "$0")"

# Запускаем бота
python bot.py
