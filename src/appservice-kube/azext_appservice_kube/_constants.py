# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os


KUBE_DEFAULT_SKU = "K1"
KUBE_ASP_KIND = "linux,kubernetes"
KUBE_APP_KIND = "linux,kubernetes,app"
KUBE_CONTAINER_APP_KIND = 'linux,kubernetes,app,container'
KUBE_FUNCTION_APP_KIND = 'linux,kubernetes,functionapp'
KUBE_FUNCTION_CONTAINER_APP_KIND = 'linux,kubernetes,functionapp,container'

LINUX_RUNTIMES = ['dotnet', 'node', 'python', 'java', 'powershell', 'dotnet-isolated', 'custom']
WINDOWS_RUNTIMES = ['dotnet', 'node', 'java', 'powershell', 'dotnet-isolated', 'custom']

NODE_VERSION_DEFAULT = "10.14"
NODE_VERSION_NEWER = "12-lts"
NODE_EXACT_VERSION_DEFAULT = "10.14.1"
NETCORE_VERSION_DEFAULT = "2.2"
DOTNET_VERSION_DEFAULT = "4.7"
PYTHON_VERSION_DEFAULT = "3.7"
NETCORE_RUNTIME_NAME = "dotnetcore"
DOTNET_RUNTIME_NAME = "aspnet"
NODE_RUNTIME_NAME = "node"
PYTHON_RUNTIME_NAME = "python"
OS_DEFAULT = "Windows"
STATIC_RUNTIME_NAME = "static"  # not an official supported runtime but used for CLI logic
NODE_VERSIONS = ['4.4', '4.5', '6.2', '6.6', '6.9', '6.11', '8.0', '8.1', '8.9', '8.11', '10.1', '10.10', '10.14']
PYTHON_VERSIONS = ['3.7', '3.6', '2.7']
NETCORE_VERSIONS = ['1.0', '1.1', '2.1', '2.2']
DOTNET_VERSIONS = ['3.5', '4.7']

LINUX_SKU_DEFAULT = "P1V2"
FUNCTIONS_VERSIONS = ['2', '3', '4']

# functions version : default node version
FUNCTIONS_VERSION_TO_DEFAULT_NODE_VERSION = {
    '2': '~10',
    '3': '~12'
}
# functions version -> runtime : default runtime version
FUNCTIONS_VERSION_TO_DEFAULT_RUNTIME_VERSION = {
    '2': {
        'node': '8',
        'dotnet': '2',
        'python': '3.7',
        'java': '8'
    },
    '3': {
        'node': '12',
        'dotnet': '3',
        'python': '3.7',
        'java': '8'
    }
}
# functions version -> runtime : runtime versions
FUNCTIONS_VERSION_TO_SUPPORTED_RUNTIME_VERSIONS = {
    '2': {
        'node': ['8', '10'],
        'python': ['3.6', '3.7'],
        'dotnet': ['2'],
        'java': ['8']
    },
    '3': {
        'node': ['10', '12'],
        'python': ['3.6', '3.7', '3.8'],
        'dotnet': ['3'],
        'java': ['8']
    }
}
# dotnet runtime version : dotnet linuxFxVersion
DOTNET_RUNTIME_VERSION_TO_DOTNET_LINUX_FX_VERSION = {
    '2': '2.2',
    '3': '3.1'
}

MULTI_CONTAINER_TYPES = ['COMPOSE', 'KUBE']

OS_TYPES = ['Windows', 'Linux']

CONTAINER_APPSETTING_NAMES = ['DOCKER_REGISTRY_SERVER_URL', 'DOCKER_REGISTRY_SERVER_USERNAME',
                              'DOCKER_REGISTRY_SERVER_PASSWORD', "WEBSITES_ENABLE_APP_SERVICE_STORAGE"]
APPSETTINGS_TO_MASK = ['DOCKER_REGISTRY_SERVER_PASSWORD']


FUNCTIONS_STACKS_API_JSON_PATHS = {
    'windows': os.path.abspath(os.path.join(os.path.abspath(__file__), '../resources/WindowsFunctionsStacks.json')),
    'linux': os.path.abspath(os.path.join(os.path.abspath(__file__), '../resources/LinuxFunctionsStacks.json'))
}

FUNCTIONS_LINUX_RUNTIME_VERSION_REGEX = r"^.*\|(.*)$"
FUNCTIONS_WINDOWS_RUNTIME_VERSION_REGEX = r"^~(.*)$"
