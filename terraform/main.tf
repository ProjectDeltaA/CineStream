provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "movieApp-rg"
  location = "East US"
}

resource "azurerm_kubernetes_cluster" "aks" {
  name                = "movieApp-aks"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = "movieapp"

  identity {
    type = "UserAssigned"
  }

  default_node_pool {
    name       = "default"
    node_count = 2
    vm_size    = "Standard_DS2_v2"
  }

  network_profile {
    network_plugin    = "azure"
    network_policy    = "azure"
    load_balancer_sku = "standard"
    outbound_type     = "loadBalancer"
  }
}

output "kubeconfig" {
  value = azurerm_kubernetes_cluster.aks.kube_config_raw
}