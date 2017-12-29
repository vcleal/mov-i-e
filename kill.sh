#!/bin/bash
pgrep -f /home/maria/python/mov-i-e/teste.sh > ~/python/mov-i-e/kill.pid
kill -15 $(cat ~/python/mov-i-e/kill.pid)
