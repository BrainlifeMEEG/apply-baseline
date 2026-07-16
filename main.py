# Copyright (c) 2020 brainlife.io
#
# This file is the main script for applying baseline correction to MEG/EEG Epochs files.
#
# Author: Kamilya Salibayeva
# Indiana University

# set up environment
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'brainlife_utils'))

import mne

from brainlife_utils import (
    load_config,
    setup_matplotlib_backend,
    ensure_output_dirs,
    create_product_json,
    add_info_to_product,
    require_config_keys,
)

# Set up environment
setup_matplotlib_backend()
config = load_config()
require_config_keys(config, ['epochs', 'tmin', 'tmax'])

ensure_output_dirs('out_dir')

fname = config['epochs']
tmin = config['tmin']
tmax = config['tmax']

# Validate that tmin/tmax define a proper baseline window
if not tmin < tmax:
    product_items = []
    add_info_to_product(
        product_items,
        f"Invalid baseline window: tmin ({tmin}) must be less than tmax ({tmax})",
        'error'
    )
    create_product_json(product_items)
    sys.exit(1)

epochs = mne.read_epochs(fname)
epochs.apply_baseline((tmin, tmax))

# save epochs
epochs.save(os.path.join('out_dir', 'epo.fif'))

# == CREATE PRODUCT.JSON ==
product_items = []
add_info_to_product(product_items, f"Baseline correction applied: tmin={tmin}, tmax={tmax}", 'success')
create_product_json(product_items)
