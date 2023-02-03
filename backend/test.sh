#!/bin/bash

# This is test script to run all checks at once.
# Commands:
# _______________________
# |-> chmod +x test.sh  |
# |-> ./test.sh         |
# |_____________________|

# Color codes
fail="\033[31m"
success="\033[32m"
end="\033[0m"

# pytest check
echo "[INFO] pytest check:"
pytest

# pylint check
echo "[INFO] pylint check:"
lint_score=$(pylint --rcfile .pylintrc src/ tests/)
echo "$lint_score"

# check if pylint score is < 10.0
rating=$(echo "$lint_score" | grep -oE "[0-9]+\.[0-9]+\/[0-9]+ " | grep -oE "[0-9]+\.[0-9]")
value=$(echo "$rating" | awk '{printf "%.1f", $0}')
awk "BEGIN {
      if (${value} < 10.0) print \"${fail}[INFO] Code can be improved.${end}\";
      else print \"${success}[INFO] Excellent code!${end}\n\"
    }"

# black formatting check
echo "[INFO] black formatting check:"
black . --check
