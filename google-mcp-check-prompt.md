Use Playwright MCP only (do not use pytest, local test files, or non-MCP automation).

Run in headed mode (visible browser, not headless).

Steps:
1. Open https://www.google.com and wait until the page is loaded.
2. Assert the search field exists (Google search box).
3. Assert the "Google Search" button exists.
4. Assert the "I'm Feeling Lucky" button exists.
5. Type any text into the search field (for example: "playwright") so buttons are interactable.
6. Verify both buttons are interactable (click trial or equivalent non-navigating interactability check).

Output format:
- Search field exists: PASS/FAIL
- "Google Search" exists: PASS/FAIL
- "I'm Feeling Lucky" exists: PASS/FAIL
- "Google Search" interactable: PASS/FAIL
- "I'm Feeling Lucky" interactable: PASS/FAIL
- Notes: brief reason for any FAIL
