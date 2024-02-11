vim.opt.foldmethod = "syntax"
vim.opt.foldcolumn = "auto"

vim.opt.cmdheight = 1                           -- more space in the neovim command line for displaying messages
vim.opt.showmode = false                        -- we don't need to see things like -- INSERT -- anymore
vim.opt.showtabline = 2                         -- always show tabs

vim.opt.termguicolors = true                    -- set term gui colors (most terminals support this)

vim.opt.undofile = true                         -- enable persistent undo

vim.opt.expandtab = true                        -- convert tabs to spaces
vim.opt.shiftwidth = 4                          -- the number of spaces inserted for each indentation
vim.opt.tabstop = 4                             -- insert 2 spaces for a tab

vim.opt.number = true                           -- set numbered lines
vim.opt.relativenumber = true                  -- set relative numbered lines
vim.opt.numberwidth = 4                         -- set number column width to 2 {default 4}

vim.opt.scrolloff = 6                           -- is one of my fav
vim.opt.sidescrolloff = 8
vim.opt.guifont = "Source Code Pro:h17"         -- the font used in graphical neovim applications
vim.opt.timeoutlen = 300 

