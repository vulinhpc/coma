import antfu from "@antfu/eslint-config";
import nextPlugin from "@next/eslint-plugin-next";
import jestDom from "eslint-plugin-jest-dom";
import jsxA11y from "eslint-plugin-jsx-a11y";
import playwright from "eslint-plugin-playwright";
import simpleImportSort from "eslint-plugin-simple-import-sort";
import tailwind from "eslint-plugin-tailwindcss";
import testingLibrary from "eslint-plugin-testing-library";
import unusedImports from "eslint-plugin-unused-imports";

export default antfu(
  {
    react: true,
    typescript: true,

    lessOpinionated: true,
    isInEditor: false,

    stylistic: {
      semi: true,
    },

    formatters: {
      css: true,
    },

    ignores: ["migrations/**/*", "next-env.d.ts", "docs/**/*"],
  },
  ...tailwind.configs["flat/recommended"],
  jsxA11y.flatConfigs.recommended,
  {
    plugins: {
      "@next/next": nextPlugin,
    },
    rules: {
      ...nextPlugin.configs.recommended.rules,
      ...nextPlugin.configs["core-web-vitals"].rules,
    },
  },
  {
    plugins: {
      "simple-import-sort": simpleImportSort,
    },
    rules: {
      "simple-import-sort/imports": "error",
      "simple-import-sort/exports": "error",
    },
  },
  {
    files: ["**/*.test.ts?(x)"],
    ...testingLibrary.configs["flat/react"],
    ...jestDom.configs["flat/recommended"],
  },
  {
    files: ["**/*.spec.ts", "**/*.e2e.ts"],
    ...playwright.configs["flat/recommended"],
  },
  {
    plugins: {
      "unused-imports": unusedImports,
    },
    rules: {
      "unused-imports/no-unused-imports": "error",
      "ts/no-explicit-any": ["warn", { ignoreRestArgs: true }],
      "tailwindcss/no-custom-classname": "off",
      "import/order": "off", // Avoid conflicts with `simple-import-sort` plugin
      "sort-imports": "off", // Avoid conflicts with `simple-import-sort` plugin
      "style/brace-style": ["error", "1tbs"], // Use the default brace style
      "ts/consistent-type-definitions": ["error", "type"], // Use `type` instead of `interface`
      "react/prefer-destructuring-assignment": "off", // Vscode doesn't support automatically destructuring, it's a pain to add a new variable
      "node/prefer-global/process": "off", // Allow using `process.env`
      "test/padding-around-all": "error", // Add padding in test files
      "test/prefer-lowercase-title": "off", // Allow using uppercase titles in test titles
      "style/quotes": "off", // Let Prettier handle quotes
      "style/arrow-parens": "off", // Let Prettier handle arrow parens
      "style/jsx-wrap-multilines": "off", // Let Prettier handle JSX wrapping
      "style/jsx-one-expression-per-line": "off", // Let Prettier handle JSX formatting
      "style/multiline-ternary": "off", // Let Prettier handle ternary formatting
      "style/operator-linebreak": "off", // Let Prettier handle operator line breaks
      "style/indent": "off", // Let Prettier handle indentation
      "style/indent-binary-ops": "off", // Let Prettier handle binary ops indentation
      "yaml/quotes": "off", // Let Prettier handle YAML quotes
    },
  },
);
