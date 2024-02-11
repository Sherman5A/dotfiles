vim.g.catppuccin_flavour = "frappe"
-- latte, frappe, macchiato, mocha are available themes
require("catppuccin").setup({
    transparent_background = false,
    term_colors = false,
    styles = {
        conditionals = { "bold" },
        functions = {},
        loops = { "italic" },
    },
    integrations = {
        markdown = true,
    },

})

vim.cmd [[colorscheme catppuccin]]


require("lualine").setup {
    options = {
        theme = "catppuccin",
        section_separators = { left = "", right = ""},
    }
}
