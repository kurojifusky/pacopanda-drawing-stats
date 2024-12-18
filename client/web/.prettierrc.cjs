module.exports = {
  semi: false,
  endOfLine: "lf",
  plugins: ["prettier-plugin-svelte"],
  overrides: [{ files: "*.svelte", options: { parser: "svelte" } }],
}
