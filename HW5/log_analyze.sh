#!/bin/bash
 
CURRENT_DIR=$(realpath $(dirname "$0"))
ACCESS_LOG=$(dirname "$CURRENT_DIR")/access.log
RESULT=$(dirname "$CURRENT_DIR")/HW5/results_bash.txt

echo "Count of requests:" > "$RESULT"
wc -l "$ACCESS_LOG" | awk '{print $1}' >> "$RESULT"

echo "Count of requests by HTTP method:" >> "$RESULT"
cat "$ACCESS_LOG" | awk '{print $6}' | sed 's/^"//' | sort | uniq -c | sort -rnk1 >> "$RESULT"

echo "TOP-10 most frequent requsts:" >> "$RESULT"
cat "$ACCESS_LOG" | awk '{print $7}' | sort | uniq -c | sort -rnk1 | head | \
	awk '{printf "url: %s - Count of request: %d.\n", $2, $1}' >> "$RESULT"

echo "TOP -5 largest requests that failed with (4XX) error:" >> "$RESULT"
cat "$ACCESS_LOG" | awk '{if ($9 ~ /4../) printf "%s %d %d %s\n", $7, $9, $10, $1}' | sort -rnk3 | head -n 5 | \
	awk '{printf "URL: %s - Status: %d - Size: %d - IP: %s.\n", $1, $2, $3, $4}' >> "$RESULT"

echo "Top 5 users by the number of requests that ended with a server error:" >> "$RESULT"
cat "$ACCESS_LOG" | awk '{if ($9 ~ /5../) print $1}' | sort -t "." -rnk1 | uniq -c | sort -rnk1 | head -n 5 | \
     awk '{printf "IP-ADDRESS: %s. COUNT OF REQUESTS: %d\n", $2, $1}' >> "$RESULT"
