module.exports = {
  useTabs: false,
  tabWidth: 2,
  semi: false,
  endOfLine: "lf",
  overrides: [
    {
      files: ["./**/tailwind.config.ts"],
      options: {
        printWidth: 125,
      },
    },
  ],
}
