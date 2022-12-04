#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""

    """PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    LUIS_APP_ID = os.environ.get("LuisAppId", "0f93a641-96e4-425a-b29a-1ee8a281bdde")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "d5973268fb8343c890810a6a1e476ec5")
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "westus.api.cognitive.microsoft.com")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get("AppInsightsInstrumentationKey", "9e2b1f3a-5636-4632-ac90-e45b7e709853")"""

    PORT = 3978
    APP_ID = ""
    APP_PASSWORD = ""
    LUIS_APP_ID = "0f93a641-96e4-425a-b29a-1ee8a281bdde"
    LUIS_API_KEY = "d5973268fb8343c890810a6a1e476ec5"
    LUIS_API_HOST_NAME = "https://luisocp10-authoring.cognitiveservices.azure.com/"
    APPINSIGHTS_INSTRUMENTATION_KEY = "9e2b1f3a-5636-4632-ac90-e45b7e709853"
