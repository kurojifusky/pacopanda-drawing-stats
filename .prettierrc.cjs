module.exports = {
  useTabs: false,
  tabWidth: 2,
  semi: false,
  endOfLine: "lf",
  plugins: ["prettier-plugin-svelte"],
  overrides: [{ files: "*.svelte", options: { parser: "svelte" } }],
}
