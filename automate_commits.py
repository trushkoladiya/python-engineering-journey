#!/usr/bin/env python3
import os
import sys
import re
import random
import datetime
import subprocess

def run_git_cmd(args, env=None):
    """Run a git command and return stdout as string."""
    try:
        res = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True, env=env)
        return res.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running git command {' '.join(args)}: {e.stderr.strip()}", file=sys.stderr)
        raise e

def parse_subtopic(path):
    """Parse module and subtopic numbers from path for sorting."""
    parts = path.split('/')
    if len(parts) >= 2:
        m_match = re.match(r'module_(\d+)', parts[0])
        s_match = re.match(r'(\d+)', parts[1])
        if m_match and s_match:
            return (int(m_match.group(1)), int(s_match.group(1)))
    return (999, 999)

def generate_commit_message(selected_subtopics):
    """Generate a human-like commit message based on added subtopics."""
    modules = {}
    for path in selected_subtopics:
        parts = path.split('/')
        m_dir = parts[0]
        s_dir = parts[1]
        if m_dir not in modules:
            modules[m_dir] = []
        modules[m_dir].append(s_dir)
    
    sorted_m_dirs = sorted(modules.keys(), key=lambda x: int(re.search(r'module_(\d+)', x).group(1)))
    
    def clean_subtopic_name(s_dir):
        name = re.sub(r'^\d+_', '', s_dir)
        name = name.replace('_', ' ')
        return name
        
    def clean_module_name(m_dir):
        name = re.sub(r'^module_\d+_', '', m_dir)
        name = name.replace('_', ' ')
        return name

    def get_module_num(m_dir):
        return int(re.search(r'module_(\d+)', m_dir).group(1))

    if len(sorted_m_dirs) == 1:
        m_dir = sorted_m_dirs[0]
        m_num = get_module_num(m_dir)
        m_name = clean_module_name(m_dir)
        s_names = [clean_subtopic_name(s) for s in modules[m_dir]]
        
        if len(s_names) == 1:
            s_str = s_names[0]
        elif len(s_names) == 2:
            s_str = f"{s_names[0]} and {s_names[1]}"
        else:
            s_str = ", ".join(s_names[:-1]) + f" and {s_names[-1]}"
            
        templates = [
            f"added subtopics {s_str} for module {m_num}",
            f"added {s_str} to module {m_num} ({m_name})",
            f"completed {s_str} in module {m_num}",
            f"covered {s_str} in {m_name} module",
            f"added lessons: {s_str} for module {m_num}",
        ]
        return random.choice(templates)
    
    else:
        m_dir_a = sorted_m_dirs[0]
        m_dir_b = sorted_m_dirs[1]
        
        m_num_a = get_module_num(m_dir_a)
        m_name_a = clean_module_name(m_dir_a)
        s_names_a = [clean_subtopic_name(s) for s in modules[m_dir_a]]
        
        m_num_b = get_module_num(m_dir_b)
        m_name_b = clean_module_name(m_dir_b)
        s_names_b = [clean_subtopic_name(s) for s in modules[m_dir_b]]
        
        if len(s_names_a) == 1:
            s_str_a = s_names_a[0]
        else:
            s_str_a = ", ".join(s_names_a[:-1]) + f" and {s_names_a[-1]}"
            
        if len(s_names_b) == 1:
            s_str_b = s_names_b[0]
        else:
            s_str_b = ", ".join(s_names_b[:-1]) + f" and {s_names_b[-1]}"
            
        templates = [
            f"finished module {m_num_a} ({s_str_a}) and started module {m_num_b} with {s_str_b}",
            f"added last lessons of module {m_num_a} and first lessons of module {m_num_b}",
            f"completed module {m_num_a} and added {s_str_b} for module {m_num_b}",
            f"finished {m_name_a} and added {s_str_b} under {m_name_b}",
        ]
        return random.choice(templates)

def main():
    print("Starting automated commit process...")
    
    # 1. Fetch the latest branches to ensure we can see all-content
    print("Fetching remote branches...")
    try:
        run_git_cmd(["git", "fetch", "origin", "all-content"])
    except Exception:
        print("Warning: Could not fetch all-content from origin. Will check local tracking/refs.")
    
    # Determine the correct ref to use for all-content
    # Try origin/all-content first, fallback to all-content branch locally if remote fetch failed
    source_branch = "origin/all-content"
    try:
        run_git_cmd(["git", "rev-parse", "--verify", source_branch])
    except Exception:
        source_branch = "all-content"
        try:
            run_git_cmd(["git", "rev-parse", "--verify", source_branch])
        except Exception:
            print("Error: Could not find 'all-content' branch locally or on origin. Please make sure it exists.")
            sys.exit(1)
            
    print(f"Using source branch: {source_branch}")

    # 2. Get list of files from the source branch
    files_str = run_git_cmd(["git", "ls-tree", "-r", "--name-only", source_branch])
    all_files = files_str.splitlines()

    # 3. Identify all subtopics in the source branch
    all_subtopics = set()
    for f in all_files:
        # Match pattern: module_XX_name/YY_subtopic_name
        match = re.match(r'^(module_\d+_[^/]+/\d+_[^/]+)/', f)
        if match:
            all_subtopics.add(match.group(1))

    # Sort subtopics chronologically
    sorted_all_subtopics = sorted(list(all_subtopics), key=parse_subtopic)
    print(f"Found {len(sorted_all_subtopics)} total subtopics in {source_branch}.")

    # 4. Check which subtopics already exist in the local workspace (current branch 'main')
    local_subtopics = set()
    for subtopic in sorted_all_subtopics:
        if os.path.isdir(subtopic):
            # Check if there are actual files inside it (e.g. theory.md or code.py)
            files_in_dir = [f for f in os.listdir(subtopic) if os.path.isfile(os.path.join(subtopic, f))]
            if files_in_dir:
                local_subtopics.add(subtopic)

    print(f"Found {len(local_subtopics)} subtopics already present on main.")

    # 5. Determine pending subtopics
    pending_subtopics = [s for s in sorted_all_subtopics if s not in local_subtopics]
    print(f"Pending subtopics: {len(pending_subtopics)}")

    if not pending_subtopics:
        print("No pending subtopics remaining. All content has been successfully committed to main!")
        sys.exit(0)

    # 6. Choose 3 or 4 subtopics to commit (randomly)
    num_to_commit = random.choice([3, 4])
    if len(pending_subtopics) < num_to_commit:
        num_to_commit = len(pending_subtopics)
        
    selected_subtopics = pending_subtopics[:num_to_commit]
    print(f"Selected {num_to_commit} subtopics to commit today:")
    for s in selected_subtopics:
        print(f"  - {s}")

    # 7. Checkout the files from the source branch
    for subtopic in selected_subtopics:
        print(f"Checking out: {subtopic}")
        run_git_cmd(["git", "checkout", source_branch, "--", subtopic])
        # Add to index to be completely sure
        run_git_cmd(["git", "add", subtopic])

    # 8. Generate commit message
    commit_msg = generate_commit_message(selected_subtopics)
    print(f"Generated commit message: '{commit_msg}'")

    # 9. Configure git user (so GitHub maps green dots to the correct profile)
    run_git_cmd(["git", "config", "user.name", "trushkoladiya"])
    run_git_cmd(["git", "config", "user.email", "trushkoladiya.work@gmail.com"])

    # 10. Generate a random daytime date for the commit in IST (UTC+5:30)
    utc_now = datetime.datetime.utcnow()
    ist_now = utc_now + datetime.timedelta(hours=5, minutes=30)
    
    date_str = ist_now.strftime('%Y-%m-%d')
    random_hour = random.randint(9, 21)  # Between 9:00 AM and 9:59 PM local time
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)
    
    git_date = f"{date_str}T{random_hour:02d}:{random_minute:02d}:{random_second:02d}+0530"
    print(f"Setting commit date to (IST): {git_date}")

    # 11. Commit the changes
    env = os.environ.copy()
    env['GIT_AUTHOR_DATE'] = git_date
    env['GIT_COMMITTER_DATE'] = git_date
    
    run_git_cmd(["git", "commit", "-m", commit_msg], env=env)
    print("Changes committed successfully.")

    # 11b. Check if this was the last set of subtopics to commit
    if len(pending_subtopics) <= num_to_commit:
        print("This was the final set of lessons! Initiating self-cleanup...")
        try:
            files_to_remove = ["automate_commits.py", ".github/workflows/daily_commit.yml"]
            for f in files_to_remove:
                if os.path.exists(f):
                    os.remove(f)
                    run_git_cmd(["git", "rm", f])
            
            # Generate a time 15 minutes later for the cleanup commit
            cleanup_minute = random_minute + 15
            cleanup_hour = random_hour
            if cleanup_minute >= 60:
                cleanup_minute -= 60
                cleanup_hour += 1
            if cleanup_hour >= 24:
                cleanup_hour = 23
                cleanup_minute = 59
                
            cleanup_git_date = f"{date_str}T{cleanup_hour:02d}:{cleanup_minute:02d}:{random_second:02d}+0530"
            
            env_cleanup = os.environ.copy()
            env_cleanup['GIT_AUTHOR_DATE'] = cleanup_git_date
            env_cleanup['GIT_COMMITTER_DATE'] = cleanup_git_date
            
            cleanup_msg = "completed full course content and cleaned up workspace"
            run_git_cmd(["git", "commit", "-m", cleanup_msg], env=env_cleanup)
            print("Self-cleanup committed successfully.")
        except Exception as e:
            print(f"Warning: Self-cleanup failed with error: {e}. Pushing remaining content anyway.")

    # 12. Push changes to origin main
    print("Pushing to main branch...")
    run_git_cmd(["git", "push", "origin", "main"])
    print("Pushed successfully!")

if __name__ == '__main__':
    main()
