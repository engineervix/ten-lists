export PATH := "./node_modules/.bin:" + env_var('PATH')

default:
    just --list

# [🤖 CI task] extract content from CHANGELOG.md for use in Gitlab/Github Releases
release-notes:
    #!/usr/bin/env node
    (() => {
        // we read the CHANGELOG.md file and loop through line by line
        // we wanna extract content beginning from the first Heading 2 text
        // to the last line before the next Heading 2 text
        const fs = require('fs');
        const path = require('path');
        const patternToMatch = '## ';
        let count = 0;
        const lines = [];
        const headingText = "## What's changed in this release\n";
        lines.push(headingText);
        const changelogPath = path.resolve("{{invocation_directory()}}/CHANGELOG.md");
        const changelogContent = fs.readFileSync(changelogPath, 'utf8');
        const changelogLines = changelogContent.split('\n');
        for (const line of changelogLines) {
            if (line.startsWith(patternToMatch) && count === 0) {
                count += 1;
            } else if (!line.startsWith(patternToMatch) && count === 1) {
                lines.push(line + '\n');
            } else if (line.startsWith(patternToMatch) && count === 1) {
                break;
            }
        }
        const releaseNotesPath = path.join("{{invocation_directory()}}", '../', 'LATEST_RELEASE_NOTES.md');
        fs.writeFileSync(releaseNotesPath, lines.join(''), 'utf8');
    })();
