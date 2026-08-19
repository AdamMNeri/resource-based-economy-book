import os
import glob
import shutil
import time

chapters_dir = "chapters"
archive_dir = os.path.join(chapters_dir, ".archive")

# files to restore
to_restore = [
    "00-introduction-v3.md",
    "01-the-case-for-change-v21.md",
    "02-introducing-resourceism-v15.md",
    "03-un-transition-pathway-v12.md",
    "04-daos-and-blockchain-v19.md",
    "05-phase-1-piloting-the-transition-v9.md",
    "06-phase-2-scaling-up-global-governance-v10.md",
    "07-core-principles-values-universal-rights-v11.md",
    "08-addressing-counter-arguments-corollary-issues-v7.md",
    "09-human-flourishing-dividend-v8.md",
    "10-behavioral-architecture-and-identity-v12.md",
    "11-conclusion-call-to-action-v8.md",
    "references.md"
]

# Delete currently active files
for f in glob.glob(os.path.join(chapters_dir, "*.md")):
    # do not delete Map of Content or Book-Map
    if base_name := os.path.basename(f):
        if not base_name.startswith("00-Book-Map"):
            os.remove(f)
            print(f"Removed {base_name}")

# Restore from archive
for f in to_restore:
    archived_path = os.path.join(archive_dir, f)
    if os.path.exists(archived_path):
        shutil.move(archived_path, os.path.join(chapters_dir, f))
        print(f"Restored {f}")
    else:
        print(f"Missing {f}")
