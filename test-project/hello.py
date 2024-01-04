#-------------------------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See https://go.microsoft.com/fwlink/?linkid=2090316 for license information.
#-------------------------------------------------------------------------------------------------------------

import tensorflow as tf

# Load the .pb file
converter = tf.lite.TFLiteConverter.from_saved_model("path/to/saved_model.pb")
