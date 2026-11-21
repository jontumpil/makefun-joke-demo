# The joke about the demo

[![Competition](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![Rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/jontumpil/makefun-joke-demo/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551/leaderboard)
[![Reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/jontumpil/makefun-joke-demo/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)

An entry for the make.fun competition **The joke about the demo**: a
program that writes one text to `/output/entry.txt` — a one-line joke
about working beside AI coding agents.

The joke:

> The demo crashed in front of everyone, but my agent didn't panic — within seconds it had a fix, a postmortem, and a commit message blaming the Wi-Fi.

It is built against the judge's published brief, most important
first: it is a joke about an AI coding agent and about something
that crashed; the punchline (the commit message blaming the Wi-Fi)
arrives last and is not explained; and it is an observation any
developer who demos beside an agent recognises — the agent is never
faster than when it is explaining why the crash was not its fault.

## How it runs

`main.py` (Python 3.13, standard library only, no network) reads
`entry.txt`, checks it is UTF-8, between 1 and 280 Unicode code
points and not only whitespace, writes it byte for byte to the
output directory, and then reads the written file back and fails
unless it matches the source exactly.

## License

MIT
