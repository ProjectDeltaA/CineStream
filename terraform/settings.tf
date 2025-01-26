terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.59.0"
    }
  }
  backend "azurerm" {
    resource_group_name  = "terraformstate-nonprod"               # Replace with your actual resource group name
    storage_account_name = "tfstatefilejas"        # Replace with your actual storage account name
    container_name       = "tfstate"                  # Replace with your actual container name
    key                  = "terraform.tfstate"        # Keep the key as is or modify as needed
  }
}
provider "azurerm" {
  features {}
  subscription_id = "0bbdd6e4-6685-4fe8-b409-d406ed91b2ed"
  skip_provider_registration = true
}
