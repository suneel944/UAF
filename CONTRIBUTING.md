# Contributing to This Project

Thank you for your interest in contributing to our project. To maintain consistency and ensure our automated version bumping works correctly, please follow these guidelines.

## Commit Message Standards

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification for our commit messages. This helps us automatically determine version bumps and generate changelogs.

### Commit Message Format

Each commit message should be structured as follows:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types

- `feat`: A new feature (triggers a minor version bump)
- `fix`: A bug fix (triggers a patch version bump)
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools and libraries such as documentation generation

### Breaking Changes

For commits that introduce breaking changes, add `BREAKING CHANGE:` in the commit body or footer. This will trigger a major version bump.

### Examples

```
feat: add user authentication feature

BREAKING CHANGE: `auth` function now requires an API key
```

```
fix: correct calculation in billing module
```

```
docs: update README with new build instructions
```

## How This Affects Version Bumping

Our automated version bump process works as follows:

1. If any commit since the last release contains `BREAKING CHANGE`, the major version is bumped.
2. Otherwise, if any commit contains `feat:`, the minor version is bumped.
3. If neither of the above conditions are met, but there are `fix:` commits, the patch version is bumped.
4. If there are only `chore:`, `docs:`, `style:`, `refactor:`, `perf:`, or `test:` commits, no version bump occurs.

### Multiple Commit Types in a Single Release

When a release includes multiple commit types:

- The highest-priority change determines the version bump (major > minor > patch).
- Commits that don't trigger a version bump (like `chore:`) are included in the release but don't affect the version number.

For example, if you have commits with `feat:`, `fix:`, and `chore:` since the last release, it will result in a minor version bump (due to `feat:`), and all changes (including those from `fix:` and `chore:`) will be included in the release notes.

## Pull Request Process

1. Ensure your commits follow the standards outlined above.
2. Update the README.md or relevant documentation with details of changes, if applicable.
3. Use the pull request template provided when creating your pull request. This template is automatically loaded when you create a new pull request and includes checkboxes for ensuring your contribution meets our standards.
4. Fill out the pull request template completely, checking off each item as you complete it.
5. In the pull request description, provide a clear explanation of the changes and the rationale behind them.
6. If your pull request addresses an existing issue, reference that issue in the pull request description using the syntax `Fixes #123` (where 123 is the issue number).
7. You may merge the Pull Request once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

## Pull Request Template

When you create a new pull request, you'll see a template with various sections and checkboxes. This template is designed to ensure that your contribution meets our project standards and provides reviewers with all necessary information. Please fill out each section of the template thoroughly.

Key points in the pull request template:

- Describe the type of change (bug fix, new feature, breaking change, etc.)
- Explain how you've tested your changes
- Confirm that you've followed project guidelines (code style, documentation, etc.)
- Verify that your commit messages follow the Conventional Commits specification
- Provide any additional context or screenshots that might be helpful

By using this template, you help maintainers and reviewers understand your contribution more quickly and ensure that all necessary information is provided upfront.

## Questions?

If you have any questions about the contribution process or these standards, please reach out to the project maintainers.

Thank you for helping us maintain a consistent and efficient development process!
