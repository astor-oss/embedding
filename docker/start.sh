#!/bin/bash
cd /home/embedding && uvicorn main:app --host 0.0.0.0 --port 8080 --reload
