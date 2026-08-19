import os
import shutil

chapters_dir = "chapters"
archive_dir = os.path.join(chapters_dir, ".archive")

files_to_bump = {
    "00-introduction-v3.md": "00-introduction-v4.md",
    "02-introducing-resourceism-v15.md": "02-introducing-resourceism-v16.md",
    "09-human-flourishing-dividend-v8.md": "09-human-flourishing-dividend-v9.md",
    "10-behavioral-architecture-and-identity-v12.md": "10-behavioral-architecture-and-identity-v13.md"
}

for old, new in files_to_bump.items():
    old_path = os.path.join(chapters_dir, old)
    new_path = os.path.join(chapters_dir, new)
    
    # We modified the file directly in place earlier, so old_path has the new content.
    # We just need to rename it to new_path and copy the old content from archive?
    # Actually, we didn't back it up before modifying. Wait, I restored it from archive, so the archive still has the old version!
    # So I can just rename the file in `chapters/` to `new_path`.
    if os.path.exists(old_path):
        shutil.move(old_path, new_path)
        print(f"Bumped {old} -> {new}")
