# wifi-signal-trend-analyzer

Turn raw Wi-Fi signal samples into a per-access-point summary — average, weakest sample and a WEAK flag — weakest first, so dead zones are obvious.

## How to run

```sh
python3 main.py samples.csv
```

## Example output

```
AP-Back: WEAK (avg -78 dBm, weakest -85 dBm, 12 samples)
AP-Front: OK (avg -55 dBm, weakest -62 dBm, 12 samples)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
