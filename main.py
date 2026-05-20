"""
Apply baseline correction to epoched MEG/EEG data.

Inputs:
    - epochs: Path to MNE epochs .fif file

Outputs:
    - out_dir/meg-epo.fif: Baseline-corrected epochs
    - out_figs/evoked.png: Evoked response after baseline
    - out_report/report.html: HTML report
    - product.json: Brainlife.io product metadata
"""

# Copyright (c) 2026 brainlife.io
#
# This app applies baseline correction to MNE epoched data.
#
# Authors:
# - Maximilien Chaumon (https://github.com/dnacombo)

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'brainlife_utils'))

import mne
import matplotlib.pyplot as plt

from brainlife_utils import (
    load_config,
    setup_matplotlib_backend,
    ensure_output_dirs,
    create_product_json,
    add_info_to_product,
    add_image_to_product,
    save_figure_with_base64,
)

setup_matplotlib_backend()
ensure_output_dirs('out_dir', 'out_figs', 'out_report')

config = load_config()

# == PARSE BASELINE WINDOW ==
def _parse_time(val):
    """Convert config value to float or None."""
    if val is None or val == '' or val == 'None':
        return None
    return float(val)

tmin = _parse_time(config.get('tmin'))
tmax = _parse_time(config.get('tmax'))

# == LOAD EPOCHS ==
epochs = mne.read_epochs(config['epochs'], preload=True)

# == PLOT EVOKED BEFORE BASELINE ==
fig_before = epochs.average().plot(show=False, titles='Evoked before baseline')
before_path = os.path.join('out_figs', 'evoked_before.png')
before_base64 = save_figure_with_base64(fig_before, before_path, dpi_file=150, dpi_base64=80)

# == APPLY BASELINE ==
epochs.apply_baseline((tmin, tmax))

# == PLOT EVOKED AFTER BASELINE ==
fig_after = epochs.average().plot(show=False, titles=f'Evoked after baseline ({tmin} to {tmax} s)')
evoked_path = os.path.join('out_figs', 'evoked_after.png')
after_base64 = save_figure_with_base64(fig_after, evoked_path, dpi_file=150, dpi_base64=80)

# == REPORT ==
report = mne.Report(title='Baseline Correction Report')
report.add_epochs(epochs=epochs, title='Epochs after baseline')
report.save(os.path.join('out_report', 'report.html'), overwrite=True)

# == SAVE EPOCHS ==
epochs.save(os.path.join('out_dir', 'meg-epo.fif'), overwrite=True)

# == PRODUCT.JSON ==
product_items = []
add_info_to_product(product_items, 'Baseline correction applied successfully.', msg_type='success')
add_info_to_product(product_items, f'Baseline window: {tmin} to {tmax} s')
add_info_to_product(product_items, f'Number of epochs: {len(epochs)}')
add_image_to_product(product_items, 'Evoked before baseline', base64_data=before_base64)
add_image_to_product(product_items, 'Evoked after baseline', base64_data=after_base64)
create_product_json(product_items)
