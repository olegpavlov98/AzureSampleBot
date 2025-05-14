#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "028d4938-3d2a-410f-8f41-3c7e542e9b0c")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
