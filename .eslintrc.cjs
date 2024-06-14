/** @type {import("eslint").Linter.Config} */
module.exports = {
  root: true,
  extends: ["@fusky-labs/base", "plugin:svelte/recommended", "prettier"],
  ignorePatterns: [
    ".DS_Store",
    "node_modules/",
    "build/",
    ".svelte-kit/",
    "package/",
    ".env",
    ".env.*",
    "static/",
    "yarn.lock",
  ],
  plugins: ["@typescript-eslint"],
  parser: "@typescript-eslint/parser",
  parserOptions: {
    sourceType: "module",
    ecmaVersion: 2020,
    extraFileExtensions: [".svelte"],
  },
  env: {
    browser: true,
    es2017: true,
    node: true,
  },
  overrides: [
    {
      files: ["*.svelte"],
      parser: "svelte-eslint-parser",
      parserOptions: {
        parser: "@typescript-eslint/parser",
      },
    },
  ],
  rules: {
    "@typescript-eslint/member-delimiter-style": "off",

    "import/no-unused-modules": "warn",
  },
}
