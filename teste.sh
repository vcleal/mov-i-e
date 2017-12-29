#!/bin/bash
while sleep 2
do
  timeout 1m python -W ignore ~/python/mov-i-e/mov-i-e.py
  #rm ~/python/mov-i-e/capture/output.avi
done &

