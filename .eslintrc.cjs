/** @type {import("eslint").Linter.Config} */
module.exports = {
  root: true,
  extends: [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:import/recommended",
    "plugin:import/typescript",
    "plugin:svelte/recommended",
    "prettier",
  ],
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
  parser: "@typescript-eslint/parser",
  plugins: ["@stylistic", "@typescript-eslint"],
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
    "no-var": "error",
    "no-console": "warn",

    "no-duplicate-imports": "warn",
    "no-use-before-define": "off",
    "max-depth": ["error", 3],

    "import/no-unresolved": "off",

    "@typescript-eslint/no-namespace": "off",
    "@typescript-eslint/no-unused-vars": "warn",
    "@typescript-eslint/member-delimiter-style": "off",
    "@typescript-eslint/no-non-null-assertion": "off",
    "@typescript-eslint/consistent-type-imports": [
      "error",
      { prefer: "type-imports" },
    ],
  },
}
