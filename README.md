# Apply Baseline Correction

[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.744-blue.svg)](https://doi.org/10.25663/brainlife.app.744)

## Description

This Brainlife.io application applies baseline correction to epoched MEG/EEG data stored as an MNE `Epochs` object. For each channel, it computes the mean signal over a user-specified time window (`tmin` to `tmax`) and subtracts it from every sample of the epoch, using [`mne.Epochs.apply_baseline()`](https://mne.tools/stable/generated/mne.Epochs.html#mne.Epochs.apply_baseline). This is a standard preprocessing step used to remove slow drifts and DC offsets before averaging or further analysis.

The app generates:
- Baseline-corrected epoched data in MNE-Python format

## Inputs

- **`epochs`** (`neuro/meeg/mne/epochs`): epoched MEG/EEG data to baseline-correct (required)

## Outputs

- **`out_dir/meg-epo.fif`** (`neuro/meeg/mne/epochs`): epoched data after baseline correction has been applied

## Configuration Parameters

| key | type | default | description |
|---|---|---|---|
| `tmin` | number | `-0.1` | Start time (s), relative to epoch time 0, of the baseline window |
| `tmax` | number | `0` | End time (s), relative to epoch time 0, of the baseline window (must be greater than `tmin`) |

## Usage

### Running on Brainlife.io

1. Upload or select your epoched MEG/EEG data file in MNE format (`-epo.fif`)
2. Select the apply-baseline app
3. Set `tmin` and `tmax` to define the baseline window
4. Submit the task
5. Review the baseline-corrected epochs in the output viewer

### Local Testing

```bash
# Update config.json with your epochs file path and tmin/tmax
# Then run:
./main
```

## Authors

- Kamilya Salibayeva (https://github.com/KSalibay)

## Citations

- Hayashi, S., Caron, B.A., Heinsfeld, A.S. et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. Nat Methods 21, 809–813 (2024). https://doi.org/10.1038/s41592-024-02237-2
- Gramfort, A. et al. MEG and EEG data analysis with MNE-Python. Front. Neurosci. 7, 267 (2013). https://doi.org/10.3389/fnins.2013.00267

## Funding Acknowledgement

brainlife.io is publicly funded. We kindly ask that you acknowledge the funding below in your code and publications.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)

## License

Copyright (c) 2026 MEEG Brainlife team. Licensed under AGPL-3.0, see [license.txt](license.txt).
