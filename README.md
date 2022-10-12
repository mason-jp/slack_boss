A simple python script using the Slack API to auto create private channels.

To use, create a Slack User Token in the workspace that you need to create channels in and add it to a `.env` file as seen in `.env.example`.


Usage:
`python slack_boss.py -p <channel_prefix> -f <filename>`

Where the prefix is any string you'd like appended to the names pulled from the CSV, and the
filename is the name of a CSV file following the format in `sample.csv`.
