# TZ-01a section 5 - contamination measurement

One month, 2026-08, with every observation computed twice: once under the corrected causal reading of TZ-01a section 1, once under TZ-01's reading. Nothing else differs - same bars, same intervals, same formulas. The label is `outcome_1s`.

| reading | definition | observations | intervals |
|---|---|---|---|
| corrected | `TZ-01a section 1: S_t = interval_closes[t-1]` | 44,640 | 8,928 |
| tz01 | `TZ-01: S_t = interval_closes[t]` | 44,640 | 8,928 |

## Brier score by reading

| variant | model | corrected | TZ-01 reading | TZ-01 minus corrected |
|---|---|---|---|---|
| sigma_pre | p_twap | 0.0849 | 0.0837 | -0.0012 |
| sigma_pre | p_naive | 0.1197 | 0.1191 | -0.0006 |
| sigma_live | p_twap | 0.0839 | 0.0824 | -0.0015 |
| sigma_live | p_naive | 0.1086 | 0.1079 | -0.0007 |

A negative last column means the TZ-01 reading scored better - the value of one second of look-ahead, in Brier points.

## Corrected Gate A inversion count by reading

| variant | reading | inversions at tau in {120, 180} | rate over those taus | rate over all observations | events per day |
|---|---|---|---|---|---|
| sigma_pre | corrected | 5 | 0.028% | 0.011% | 0.161 |
| sigma_pre | tz01 | 4 | 0.022% | 0.009% | 0.129 |
| sigma_live | corrected | 6 | 0.034% | 0.013% | 0.194 |
| sigma_live | tz01 | 4 | 0.022% | 0.009% | 0.129 |

## Realised frequency inside the inversion cells by reading

| variant | reading | observations | mean p_twap | mean p_naive | realised frequency | |realised - mean p_twap| |
|---|---|---|---|---|---|---|
| sigma_pre | corrected | 124 | 0.5155 | 0.4723 | 0.5565 | 0.0410 |
| sigma_pre | tz01 | 126 | 0.5125 | 0.4868 | 0.5397 | 0.0272 |
| sigma_live | corrected | 212 | 0.5087 | 0.4726 | 0.5472 | 0.0385 |
| sigma_live | tz01 | 213 | 0.5147 | 0.4825 | 0.5305 | 0.0158 |

## Brier score by tau and reading

| variant | tau | brier p_twap corrected | brier p_twap TZ-01 | brier p_naive corrected | brier p_naive TZ-01 |
|---|---|---|---|---|---|
| sigma_pre | 240 | 0.1748 | 0.1728 | 0.1857 | 0.1840 |
| sigma_pre | 180 | 0.1152 | 0.1137 | 0.1362 | 0.1351 |
| sigma_pre | 120 | 0.0644 | 0.0631 | 0.1001 | 0.0994 |
| sigma_pre | 90 | 0.0436 | 0.0429 | 0.0891 | 0.0890 |
| sigma_pre | 60 | 0.0267 | 0.0260 | 0.0875 | 0.0878 |
| sigma_live | 240 | 0.1765 | 0.1740 | 0.1779 | 0.1760 |
| sigma_live | 180 | 0.1145 | 0.1128 | 0.1231 | 0.1219 |
| sigma_live | 120 | 0.0628 | 0.0612 | 0.0857 | 0.0849 |
| sigma_live | 90 | 0.0413 | 0.0405 | 0.0770 | 0.0769 |
| sigma_live | 60 | 0.0245 | 0.0236 | 0.0794 | 0.0797 |
