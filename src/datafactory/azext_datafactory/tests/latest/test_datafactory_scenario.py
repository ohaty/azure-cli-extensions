# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from azure.cli.testsdk import StorageAccountPreparer
from .example_steps import step_create
from .example_steps import step_update
from .example_steps import step_linked_service_create
from .example_steps import step_dataset_create
from .example_steps import step_pipeline_create
from .example_steps import step_pipeline_update
from .example_steps import step_trigger_create
from .example_steps import step_integration_runtime_self_hosted_create
from .example_steps import step_integration_runtime_update
from .example_steps import step_integration_runtime_linked
from .example_steps import step_pipeline_create_run
from .example_steps import step_integration_runtime_show
from .example_steps import step_linked_service_show
from .example_steps import step_pipeline_run_show
from .example_steps import step_pipeline_show
from .example_steps import step_dataset_show
from .example_steps import step_trigger_show
from .example_steps import step_integration_runtime_list
from .example_steps import step_linked_service_list
from .example_steps import step_pipeline_list
from .example_steps import step_trigger_list
from .example_steps import step_dataset_list
from .example_steps import step_show
from .example_steps import step_list2
from .example_steps import step_list
from .example_steps import step_integration_runtime_regenerate_auth_key
from .example_steps import step_integration_runtime_get_connection_info
from .example_steps import step_integration_runtime_sync_credentials
from .example_steps import step_integration_runtime_get_monitoring_data
from .example_steps import step_integration_runtime_list_auth_key
from .example_steps import step_integration_runtime_remove_link
from .example_steps import step_integration_runtime_get_status
from .example_steps import step_integration_runtime_start
from .example_steps import step_integration_runtime_stop
from .example_steps import step_trigger_get_event_subscription_status
from .example_steps import step_activity_run_query_by_pipeline_run
from .example_steps import step_trigger_unsubscribe_from_event
from .example_steps import step_trigger_subscribe_to_event
from .example_steps import step_trigger_start
from .example_steps import step_trigger_stop
from .example_steps import step_get_git_hub_access_token
from .example_steps import step_get_data_plane_access
from .example_steps import step_pipeline_run_query_by_factory
from .example_steps import step_pipeline_run_cancel
from .example_steps import step_trigger_run_query_by_factory
from .example_steps import step_configure_factory_repo
from .example_steps import step_integration_runtime_delete
from .example_steps import step_trigger_delete
from .example_steps import step_pipeline_delete
from .example_steps import step_dataset_delete
from .example_steps import step_linked_service_delete
from .example_steps import step_delete
from .example_steps import step_managed_virtual_network_create
from .example_steps import step_managed_virtual_network_list
from .example_steps import step_managed_virtual_network_show
from .example_steps import step_managed_private_endpoint_create
from .example_steps import step_managed_private_endpoint_list
from .example_steps import step_managed_private_endpoint_show
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_main
@try_manual
def setup_main(test):
    pass


# Env cleanup_main
@try_manual
def cleanup_main(test):
    pass


# Testcase: main
@try_manual
def call_main(test):
    setup_main(test)
    step_create(test, checks=[])
    step_update(test, checks=[])
    step_linked_service_create(test, checks=[])
    # STEP NOT FOUND: LinkedServices_Update
    step_dataset_create(test, checks=[])
    # STEP NOT FOUND: Datasets_Update
    step_pipeline_create(test, checks=[])
    step_pipeline_update(test, checks=[])
    step_trigger_create(test, checks=[])
    # STEP NOT FOUND: Triggers_Update
    step_integration_runtime_self_hosted_create(test, checks=[])
    step_integration_runtime_update(test, checks=[])
    step_integration_runtime_linked(test, checks=[])
    step_pipeline_create_run(test, checks=[])
    step_integration_runtime_show(test, checks=[])
    # STEP NOT FOUND: RerunTriggers_ListByTrigger
    step_linked_service_show(test, checks=[])
    step_pipeline_run_show(test, checks=[])
    step_pipeline_show(test, checks=[])
    step_dataset_show(test, checks=[])
    step_trigger_show(test, checks=[])
    step_integration_runtime_list(test, checks=[])
    step_linked_service_list(test, checks=[])
    step_pipeline_list(test, checks=[])
    step_trigger_list(test, checks=[])
    step_dataset_list(test, checks=[])
    step_show(test, checks=[])
    step_list2(test, checks=[])
    step_list(test, checks=[])
    # STEP NOT FOUND: Operations_List
    # STEP NOT FOUND: RerunTriggers_Cancel
    # STEP NOT FOUND: RerunTriggers_Start
    # STEP NOT FOUND: RerunTriggers_Stop
    step_integration_runtime_regenerate_auth_key(test, checks=[])
    # STEP NOT FOUND: TriggerRuns_Rerun
    step_integration_runtime_get_connection_info(test, checks=[])
    step_integration_runtime_sync_credentials(test, checks=[])
    step_integration_runtime_get_monitoring_data(test, checks=[])
    step_integration_runtime_list_auth_key(test, checks=[])
    step_integration_runtime_remove_link(test, checks=[])
    step_integration_runtime_get_status(test, checks=[])
    step_integration_runtime_start(test, checks=[])
    step_integration_runtime_stop(test, checks=[])
    step_trigger_get_event_subscription_status(test, checks=[])
    step_activity_run_query_by_pipeline_run(test, checks=[])
    step_trigger_unsubscribe_from_event(test, checks=[])
    step_trigger_subscribe_to_event(test, checks=[])
    step_trigger_start(test, checks=[])
    step_trigger_stop(test, checks=[])
    step_get_git_hub_access_token(test, checks=[])
    step_get_data_plane_access(test, checks=[])
    step_pipeline_run_query_by_factory(test, checks=[])
    step_pipeline_run_cancel(test, checks=[])
    step_trigger_run_query_by_factory(test, checks=[])
    step_configure_factory_repo(test, checks=[])
    step_integration_runtime_delete(test, checks=[])
    step_trigger_delete(test, checks=[])
    step_pipeline_delete(test, checks=[])
    step_dataset_delete(test, checks=[])
    step_linked_service_delete(test, checks=[])
    step_delete(test, checks=[])
    cleanup_main(test)


# Test class for main
@try_manual
class DatafactorymainTest(ScenarioTest):
    def __init__(self, *args, **kwargs):
        super(DatafactorymainTest, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myFactory': self.create_random_name(prefix='exampleFactoryName'[:9], length=18),
            'myIntegrationRuntime': self.create_random_name(prefix='exampleIntegrationRuntime'[:12], length=25),
            'myIntegrationRuntime2': 'exampleManagedIntegrationRuntime',
            'myLinkedService': self.create_random_name(prefix='exampleLinkedService'[:10], length=20),
            'myDataset': self.create_random_name(prefix='exampleDataset'[:7], length=14),
            'myPipeline': self.create_random_name(prefix='examplePipeline'[:7], length=15),
            'myTrigger': self.create_random_name(prefix='exampleTrigger'[:7], length=14),
        })

    @ResourceGroupPreparer(name_prefix='clitestdatafactory_exampleResourceGroup'[:7], key='rg', parameter_name='rg')
    def test_datafactory_main(self, rg):
        call_main(self)
        calc_coverage(__file__)
        raise_if()

# Env setup_managedprivateendpoint
@try_manual
def setup_managedprivateendpoint(test):
    pass


# Env cleanup_managedprivateendpoint
@try_manual
def cleanup_managedprivateendpoint(test):
    pass


# Testcase: managedPrivateEndpoint
@try_manual
def call_managedprivateendpoint(test):
    setup_managedprivateendpoint(test)
    step_create(test, checks=[])
    step_managed_virtual_network_create(test, checks=[])
    step_managed_virtual_network_list(test, checks=[])
    step_managed_virtual_network_show(test, checks=[])
    step_managed_private_endpoint_create(test, checks=[])
    step_managed_private_endpoint_list(test, checks=[])
    step_managed_private_endpoint_show(test, checks=[])
    step_delete(test, checks=[])
    cleanup_managedprivateendpoint(test)


# Test class for managedPrivateEndpoint
@try_manual
class DatafactorymanagedPrivateEndpointTest(ScenarioTest):
    def __init__(self, *args, **kwargs):
        super(DatafactorymanagedPrivateEndpointTest, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myFactory': self.create_random_name(prefix='exampleFactoryName'[:9], length=18),
            'myManagedVirtualNetwork': self.create_random_name(prefix='exampleManagedVirtualNetworkName'[:16],
                                                               length=32),
            'myManagedPrivateEndpoint': self.create_random_name(prefix='exampleManagedPrivateEndpointName'[:16],
                                                                length=33),
        })

    @ResourceGroupPreparer(name_prefix='clitestdatafactory_exampleResourceGroup'[:7], key='rg', parameter_name='rg')
    @StorageAccountPreparer(name_prefix='clitestdatafactory_exampleBlobStorage'[:7], key='sa',
                            resource_group_parameter_name='rg')
    def test_datafactory_managedPrivateEndpoint(self, rg):
        call_managedprivateendpoint(self)
        calc_coverage(__file__)
        raise_if()
