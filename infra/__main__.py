import pulumi
from pulumi_azure_native import cdn, containerservice, network, resources

# Load Pulumi configuration
config = pulumi.Config()
azure_config = pulumi.Config("azure-native")

location = config.require("location")
resource_group_name = config.require("resourceGroupName")
dev_vm_size = config.require("devNodePoolVMSize")
staging_vm_size = config.require("stagingNodePoolVMSize")
prod_vm_size = config.require("prodNodePoolVMSize")
node_count_dev = config.require_int("nodeCountDev")
min_count_dev = config.require_int("minCountDev")
max_count_dev = config.require_int("maxCountDev")
node_count_staging = config.require_int("nodeCountStaging")
min_count_staging = config.require_int("minCountStaging")
max_count_staging = config.require_int("maxCountStaging")
node_count_prod = config.require_int("nodeCountProd")
min_count_prod = config.require_int("minCountProd")
max_count_prod = config.require_int("maxCountProd")
vnet_cidr = config.require("vnetCidr")
system_subnet_cidr = config.require("systemSubnetCidr")
dev_subnet_cidr = config.require("devSubnetCidr")
staging_subnet_cidr = config.require("stagingSubnetCidr")
prod_subnet_cidr = config.require("prodSubnetCidr")

# # Create an Azure Resource Group
# resource_group = resources.ResourceGroup(
#     resource_name=resource_group_name,
#     resource_group_name=resource_group_name,
#     location=location,
# )
#
# # Create a Virtual Network for the AKS cluster
# vnet = network.VirtualNetwork(
#     resource_name="aksVNet",
#     resource_group_name=resource_group.name,
#     address_space=network.AddressSpaceArgs(
#         address_prefixes=[vnet_cidr]
#     )
# )
#
# # Create Subnets for each environment
# system_subnet = network.Subnet(
#     resource_name="systemSubnet",
#     resource_group_name=resource_group.name,
#     virtual_network_name=vnet.name,
#     address_prefix=system_subnet_cidr)
#
# dev_subnet = network.Subnet(
#     resource_name="devSubnet",
#     resource_group_name=resource_group.name,
#     virtual_network_name=vnet.name,
#     address_prefix=dev_subnet_cidr)
#
# staging_subnet = network.Subnet(
#     resource_name="stagingSubnet",
#     resource_group_name=resource_group.name,
#     virtual_network_name=vnet.name,
#     address_prefix=staging_subnet_cidr)
#
# prod_subnet = network.Subnet(
#     resource_name="prodSubnet",
#     resource_group_name=resource_group.name,
#     virtual_network_name=vnet.name,
#     address_prefix=prod_subnet_cidr)
#
#
# # Define the AKS cluster with a default node pool
# aks_cluster = containerservice.ManagedCluster(
#     resource_name="aksCluster",
#     resource_group_name=resource_group.name,
#     location=location,
#     agent_pool_profiles=[
#         containerservice.ManagedClusterAgentPoolProfileArgs(
#             name="systempool",
#             count=1,
#             max_pods=110,
#             vnet_subnet_id=system_subnet.id,
#             mode=containerservice.AgentPoolMode.SYSTEM,
#             vm_size="Standard_D4s_v3",
#             os_sku=containerservice.OSSKU.UBUNTU,
#             enable_auto_scaling=True,
#             max_count=1,
#             min_count=1,
#             node_taints=["CriticalAddonsOnly=true:NoExecute"]
#         ),
#     ],
#     dns_prefix="AKS-Cluster-CWY",
#     network_profile={
#         "network_plugin": "azure",
#         "dns_service_ip": "10.0.10.10",
#         "service_cidr": "10.0.10.0/24",
#         "docker_bridge_cidr": "172.17.0.1/16",
#     },
#     service_principal_profile=containerservice.ManagedClusterServicePrincipalProfileArgs(
#        client_id=azure_config.require("clientId"),
#        secret=azure_config.require_secret("clientSecret"),
#     ),
# )
#
# # Node Pool for Development
# dev_node_pool = containerservice.AgentPool(
#     "devpool",
#     resource_group_name=resource_group.name,
#     resource_name_=aks_cluster.name,
#     vm_size=dev_vm_size,
#     os_sku=containerservice.OSSKU.UBUNTU,
#     mode=containerservice.AgentPoolMode.USER,
#     enable_auto_scaling=True,
#     count=node_count_dev,
#     min_count=min_count_dev,
#     max_count=max_count_dev,
#     agent_pool_name="devpool",
#     vnet_subnet_id=dev_subnet.id,  # Use the development subnet
#     node_labels = {"environment": "dev"},
#     node_taints = [f"environment=dev:NoExecute"],
# )
#
# # Node Pool for Staging
# staging_node_pool = containerservice.AgentPool(
#     "stagingpool",
#     resource_group_name=resource_group.name,
#     resource_name_=aks_cluster.name,
#     vm_size=staging_vm_size,
#     os_sku=containerservice.OSSKU.UBUNTU,
#     mode=containerservice.AgentPoolMode.USER,
#     enable_auto_scaling=True,
#     count=node_count_staging,
#     min_count=min_count_staging,
#     max_count=max_count_staging,
#     agent_pool_name="stagingpool",
#     vnet_subnet_id=staging_subnet.id,  # Use the development subnet
#     node_labels = {"environment": "staging"},
#     node_taints = [f"environment=staging:NoExecute"],
# )
#
# # Node Pool for Production
# prod_node_pool = containerservice.AgentPool(
#     "prodpool",
#     resource_group_name=resource_group.name,
#     resource_name_=aks_cluster.name,
#     vm_size=prod_vm_size,
#     os_sku=containerservice.OSSKU.UBUNTU,
#     mode=containerservice.AgentPoolMode.USER,
#     enable_auto_scaling=True,
#     count=node_count_prod,
#     min_count=min_count_prod,
#     max_count=max_count_prod,
#     agent_pool_name="prodpool",
#     vnet_subnet_id=prod_subnet.id,  # Use the development subnet
#     node_labels = {"environment": "prod"},
#     node_taints = [f"environment=prod:NoExecute"],
# )
#
# cdn_profile = cdn.Profile(
#     resource_name="cdn_profile",
#     location="Global",
#     origin_response_timeout_seconds=60,
#     profile_name="AFD-CWY",
#     resource_group_name=resource_group.name,
#     sku={
#         "name": cdn.SkuName.STANDARD_AZURE_FRONT_DOOR,
#     },
# )
#
# afd_endpoint = cdn.AFDEndpoint(
#     "afdEndpoint",
#     auto_generated_domain_name_label_scope=cdn.AutoGeneratedDomainNameLabelScope.TENANT_REUSE,
#     enabled_state=cdn.EnabledState.ENABLED,
#     endpoint_name=cdn_profile.name,
#     location="global",
#     profile_name=cdn_profile.name,
#     resource_group_name=resource_group.name,
# )
#
# dev_origin_group = cdn.AFDOriginGroup(
#     resource_name="dev_origin_group",
#     load_balancing_settings={
#         "additional_latency_in_milliseconds": 1000,
#         "sample_size": 3,
#         "successful_samples_required": 3,
#     },
#     origin_group_name="dev",
#     profile_name=cdn_profile.name,
#     resource_group_name=resource_group.name,
#     traffic_restoration_time_to_healed_or_new_endpoints_in_minutes=5
# )
#
# dev_origin = cdn.AFDOrigin(
#     "dev_origin",
#     enabled_state=cdn.EnabledState.ENABLED,
#     host_name="20.240.144.65",
#     http_port=80,
#     https_port=443,
#     origin_group_name=dev_origin_group.name,
#     origin_host_header="20.240.144.65",
#     origin_name="devOrigin",
#     profile_name=cdn_profile.name,
#     resource_group_name=resource_group.name,
# )
#
# dev_route = cdn.Route(
#     "dev_route",
#     enabled_state=cdn.EnabledState.ENABLED,
#     endpoint_name=afd_endpoint.name,
#     forwarding_protocol=cdn.ForwardingProtocol.MATCH_REQUEST,
#     https_redirect=cdn.HttpsRedirect.DISABLED,
#     link_to_default_domain=cdn.LinkToDefaultDomain.ENABLED,
#     origin_group={
#         "id": dev_origin_group.id,
#     },
#     patterns_to_match=["/dev/*"],
#     profile_name=cdn_profile.name,
#     resource_group_name=resource_group.name,
#     route_name="devRoute",
#     supported_protocols=[
#         cdn.AFDEndpointProtocols.HTTP,
#     ]
# )
#
# stage_origin_group = cdn.AFDOriginGroup(
#     resource_name="stage_origin_group",
#     load_balancing_settings={
#         "additional_latency_in_milliseconds": 1000,
#         "sample_size": 3,
#         "successful_samples_required": 3,
#     },
#     origin_group_name="stage",
#     profile_name=cdn_profile.name,
#     resource_group_name=resource_group.name,
#     traffic_restoration_time_to_healed_or_new_endpoints_in_minutes=5
# )
#
# stage_origin = cdn.AFDOrigin(
#     "stage_origin",
#     enabled_state=cdn.EnabledState.ENABLED,
#     host_name="135.225.23.123",
#     http_port=80,
#     https_port=443,
#     origin_group_name=stage_origin_group.name,
#     origin_host_header="135.225.23.123",
#     origin_name="stageOrigin",
#     profile_name=cdn_profile.name,
#     resource_group_name=resource_group.name,
# )
#
# stage_route = cdn.Route(
#     "stage_route",
#     enabled_state=cdn.EnabledState.ENABLED,
#     endpoint_name=afd_endpoint.name,
#     forwarding_protocol=cdn.ForwardingProtocol.MATCH_REQUEST,
#     https_redirect=cdn.HttpsRedirect.DISABLED,
#     link_to_default_domain=cdn.LinkToDefaultDomain.ENABLED,
#     origin_group={
#         "id": stage_origin_group.id,
#     },
#     patterns_to_match=["/stage/*"],
#     profile_name=cdn_profile.name,
#     resource_group_name=resource_group.name,
#     route_name="stageRoute",
#     supported_protocols=[
#         cdn.AFDEndpointProtocols.HTTP,
#     ]
# )
#
# prod_origin_group = cdn.AFDOriginGroup(
#     resource_name="prod_origin_group",
#     load_balancing_settings={
#         "additional_latency_in_milliseconds": 1000,
#         "sample_size": 3,
#         "successful_samples_required": 3,
#     },
#     origin_group_name="prod",
#     profile_name=cdn_profile.name,
#     resource_group_name=resource_group.name,
#     traffic_restoration_time_to_healed_or_new_endpoints_in_minutes=5
# )
#
# prod_origin = cdn.AFDOrigin(
#     "prod_origin",
#     enabled_state=cdn.EnabledState.ENABLED,
#     host_name="74.241.181.48",
#     http_port=80,
#     https_port=443,
#     origin_group_name=prod_origin_group.name,
#     origin_host_header="74.241.181.48",
#     origin_name="prodOrigin",
#     profile_name=cdn_profile.name,
#     resource_group_name=resource_group.name,
# )
#
# prod_route = cdn.Route(
#     "prod_route",
#     enabled_state=cdn.EnabledState.ENABLED,
#     endpoint_name=afd_endpoint.name,
#     forwarding_protocol=cdn.ForwardingProtocol.MATCH_REQUEST,
#     https_redirect=cdn.HttpsRedirect.DISABLED,
#     link_to_default_domain=cdn.LinkToDefaultDomain.ENABLED,
#     origin_group={
#         "id": prod_origin_group.id,
#     },
#     patterns_to_match=["/prod/*"],
#     profile_name=cdn_profile.name,
#     resource_group_name=resource_group.name,
#     route_name="prodRoute",
#     supported_protocols=[
#         cdn.AFDEndpointProtocols.HTTP,
#     ]
# )

