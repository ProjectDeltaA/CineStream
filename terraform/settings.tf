terraform {
  backend "azurerm" {
    resource_group_name  = "terraformstate-nonprod"               # Replace with your actual resource group name
    storage_account_name = "tfstatefilejas"        # Replace with your actual storage account name
    container_name       = "tfstate"                  # Replace with your actual container name
    key                  = "terraform.tfstate"        # Keep the key as is or modify as needed
  }
}
