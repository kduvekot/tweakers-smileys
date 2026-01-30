# GitHub CLI Token Debug Report

## Session Information
- **Branch**: `claude/debug-gh-cli-token-JN1pa`
- **Session ID**: JN1pa
- **Date**: 2026-01-30
- **Repository**: kduvekot/tweakers-smileys

## Token Status

### Authentication
✅ **Successfully authenticated** as user `kduvekot`
- Token Type: Fine-grained Personal Access Token (PAT)
- Token Prefix: `github_pat_11ACA5B3I0...`
- Expiration: 2026-12-31 23:00:00 UTC
- gh CLI Version: 2.83.2

### Working Operations
The following operations work correctly with the current token:

1. ✅ **Read Operations**
   - `gh repo view kduvekot/tweakers-smileys` - Works
   - `gh api repos/kduvekot/tweakers-smileys` - Works
   - `gh issue list --repo kduvekot/tweakers-smileys` - Works
   - `gh pr list --repo kduvekot/tweakers-smileys` - Works

2. ✅ **Git Operations**
   - `git push` to claude/* branches - Works
   - Push goes through local proxy at `127.0.0.1:19284`

3. ✅ **Limited Write Operations**
   - `gh api -X POST repos/kduvekot/tweakers-smileys/issues` - Can CREATE issues

### Failing Operations
The following operations FAIL due to insufficient token permissions:

1. ❌ **Pull Request Operations** (403 Forbidden)
   ```
   gh pr create --repo kduvekot/tweakers-smileys ...
   Error: Resource not accessible by personal access token (createPullRequest)
   ```
   - Both GraphQL and REST API endpoints fail

2. ❌ **Issue Updates** (403 Forbidden)
   ```
   gh api -X PATCH repos/kduvekot/tweakers-smileys/issues/11 -f state="closed"
   Error: Resource not accessible by personal access token (HTTP 403)
   ```

3. ❌ **Issue Comments** (GraphQL Error)
   ```
   gh issue close 11 --comment "..."
   Error: Resource not accessible by personal access token (addComment)
   ```

4. ❌ **App Installation Queries** (403 Forbidden)
   ```
   gh api /user/installations
   Error: Resource not accessible by personal access token (HTTP 403)
   ```

## Root Cause Analysis

### Issue #1: Incorrect CLI Flag Documentation
The `.claude/CLAUDE.md` file instructs using the `-R` flag:
```bash
gh cli -R kduvekot/tweakers-smileys parameter
```

**Problem**: The `-R` flag does not exist in gh CLI v2.83.2
```
unknown shorthand flag: 'R' in -R
```

**Solution**: Use `--repo` or positional arguments instead:
```bash
gh repo view kduvekot/tweakers-smileys
gh issue list --repo kduvekot/tweakers-smileys
gh pr create --repo kduvekot/tweakers-smileys ...
```

### Issue #2: Insufficient Token Permissions
The current fine-grained PAT lacks the following permissions:

**Missing Permissions:**
1. **Pull Requests**: write access (required for `gh pr create`)
2. **Issues**: write access (currently only has create, not update/close)
3. **Issue Comments**: write access

**Current Permissions:**
- ✅ Repository: read access
- ✅ Contents: write access (for git push)
- ✅ Issues: create only (not full write)
- ❌ Pull requests: no access

## Recommendations

### 1. Update CLAUDE.md Documentation
Remove references to `-R` flag and update examples:

```diff
- you can use the gh cli in this repo .. you should use the -R kduvekot/tweakers-smileys parameter
+ you can use the gh cli in this repo .. you should use the --repo kduvekot/tweakers-smileys parameter
+ or simply use: gh <command> kduvekot/tweakers-smileys
```

### 2. Update Token Permissions
The token needs the following additional permissions for full gh CLI functionality:

**Required Permissions:**
- ✅ Contents: Read and write (already granted)
- ✅ Issues: Read and write (upgrade from create-only)
- ✅ Pull requests: Read and write (currently missing)
- ✅ Metadata: Read (should be automatic)

**Optional but Recommended:**
- Comments: Read and write (for `gh issue close --comment`)

### 3. Token Configuration Steps
To fix the token permissions:

1. Go to: https://github.com/settings/tokens?type=beta
2. Find token: `github_pat_11ACA5B3I0...`
3. Click "Edit" or "Regenerate token"
4. Under "Repository access", select the repository
5. Under "Permissions", set:
   - Pull requests: **Read and write**
   - Issues: **Read and write** (upgrade from current)
6. Save changes
7. Update the `GH_TOKEN` environment variable if token is regenerated

## Workarounds

### For Pull Requests
Since `gh pr create` doesn't work, you can:

1. **Use the web UI**: Push the branch and visit the URL provided by git:
   ```
   https://github.com/kduvekot/tweakers-smileys/pull/new/claude/debug-gh-cli-token-JN1pa
   ```

2. **Use gh browse** (if it works):
   ```bash
   gh browse --branch claude/debug-gh-cli-token-JN1pa
   ```

### For Issue Operations
- Can create new issues but cannot close or update them
- Manual closure required through web UI

## Testing Summary

| Operation | Status | Error |
|-----------|--------|-------|
| gh auth status | ✅ Works | - |
| gh repo view | ✅ Works | - |
| gh issue list | ✅ Works | - |
| gh pr list | ✅ Works | - |
| gh api repos/... | ✅ Works | - |
| Create issue | ✅ Works | - |
| git push | ✅ Works | - |
| gh pr create | ❌ Fails | Resource not accessible by PAT |
| Update issue | ❌ Fails | 403 Forbidden |
| Add comment | ❌ Fails | GraphQL permission denied |

## Conclusion

The gh CLI implementation is correct, but the token has insufficient permissions. The main issues are:

1. **Documentation error**: The `-R` flag doesn't exist in gh CLI
2. **Missing permissions**: Token lacks pull request write access
3. **Limited issue access**: Can create but not update/close issues

Once the token permissions are updated, all gh CLI operations should work correctly.
