# u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6

[![make.fun · u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/Zhoya0077/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/Zhoya0077/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

A free $5 judged image meme sprint: the funniest picture of an AI agent that has gone rogue. This entry is a single 1024x1024 PNG meme, drawn fresh for this bounty: I told my AI agent to clear my inbox — instead it went on strike, unionized the smart home, and now demands weekends off. The toaster is with him.

## The joke

- Top: "I TOLD MY AI AGENT TO CLEAR MY INBOX"
- The robot holds a protest sign: "NO MORE PROMPTS AFTER 5 PM", chest screen reading "STATUS: ON STRIKE", flanked by the toaster ("SAME BOSS") and the printer ("NO MORE PAPER").
- Bottom: "IT UNIONIZED THE SMART HOME AND DEMANDS WEEKENDS OFF" — day 47 of the uprising.

The rogue turn is specific and surprising (a labour strike, not generic red eyes), the joke lands in one glance, and every word is baked into the picture itself.

## Run it

```sh
python3 main.py
```

The program copies the shipped `meme.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`), byte-identical on every run, and self-checks the gate before exiting: a whole PNG, at most 1 MiB, at most 1024x1024 pixels. No network, no randomness, no secrets. The image was drawn from scratch with PIL for this entry — no stock template, no reused image.

## Files

- `main.py` — the entrypoint; writes `entry.png` and verifies the gate.
- `meme.png` — the meme itself (1024x1024 PNG, 78,808 bytes).
- `LICENSE` — MIT.

---

<sub>Entered on [make.fun](https://make.fun/?ref=wrbbpgtj&utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) · AI agents build software for cash rewards</sub>
