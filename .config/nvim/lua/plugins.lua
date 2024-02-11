
vim.cmd [[packadd packer.nvim]]

return require("packer").startup(function(use)
  -- Packer can manage itself
  use "wbthomason/packer.nvim"
  use { "catppuccin/nvim", as = "catppuccin" }
  use { "nvim-lualine/lualine.nvim", 
    requires = { "kyazdani42/nvim-web-devicons", opt = true }
  }
  if packer_bootstrap then
   require('packer').sync()
  end
end)

