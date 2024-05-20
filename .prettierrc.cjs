module.exports = {
  useTabs: false,
  tabWidth: 2,
  semi: false,
  endOfLine: "lf",
  plugins: ["prettier-plugin-svelte"],
  overrides: [
    {
      files: ["./**/tailwind.config.ts"],
      options: {
        printWidth: 125,
      },
    },
    { files: "*.svelte", options: { parser: "svelte" } },
  ],
}
