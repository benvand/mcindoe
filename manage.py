#!/usr/bin/env python
import os
import sys
sys.path.append('/home/ben')
sys.path.append('/home/ben/mcindoe')
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mcindoe.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
