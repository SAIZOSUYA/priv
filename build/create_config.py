"""
GitHub Filler - Fake Commit Generator for GitHub

Copyright (C) 2024-2024 Liam Arguedas

This file is part of GitHub Filler, a free CLI tool based on the original Commitify 
designed to generate fake commits for GitHub repositories.

GitHub Filler is distributed under the terms of the GNU General Public License (GPL),
either version 3 of the License, or any later version.

GitHub Filler is provided "as is", without warranty of any kind, express or implied,
including but not limited to the warranties of merchantability, fitness for a
particular purpose, and noninfringement. See the GNU General Public License for
more details.

You should have received a copy of the GNU General Public License along with
GitHub Filler. If not, see <https://www.gnu.org/licenses/>.
"""

from pathlib import Path
import json


BLANK = ""
CONFIG = "config.json"


class GithubFillerConfig:
    """todo"""

    def __init__(self):
        self.cfg_dir = Path(__file__).parents[1] / "src" / "cfg"
        self.repository = None
        self.branch = "master"
        self.commits = ""
        self.file = "py"
        self.starting_date = str()
        self.ending_date = str()

    def declare_settings(self):
        """todo"""
        if self.repository == BLANK:
            print("Repository not detected, please reconfigure: ")
        return {
            "repository": self.repository,
            "branch": "master" if self.branch == BLANK else self.branch,
            "commits": self.commits,
            "file": "py" if self.file == BLANK else self.file,
            "starting_date": self.starting_date,
            "ending_date": self.ending_date,
        }

    def ask_configs(self, return_configs=False):
        """todo"""
        import sys
        existing = {}
        try:
            with open(self.cfg_dir / CONFIG, "r", encoding="utf-8") as file:
                existing = json.load(file)
        except Exception:
            pass

        if not sys.stdin.isatty() and existing.get("repository"):
            self.repository = existing.get("repository", "")
            self.branch = existing.get("branch", "master")
            self.commits = existing.get("commits", "random")
            self.file = existing.get("file", "py")
            self.starting_date = existing.get("starting_date", "")
            self.ending_date = existing.get("ending_date", "")
        else:
            try:
                self.repository = input(f"Repository URL [{existing.get('repository', '')}]: ").strip()
            except Exception:
                self.repository = ""
            if not self.repository and "repository" in existing:
                self.repository = existing["repository"]

            try:
                self.branch = input(f"Branch (Default: {existing.get('branch', 'master')}): ").strip()
            except Exception:
                self.branch = ""
            if not self.branch:
                self.branch = existing.get("branch", "master")

            try:
                self.commits = input(f"Number of Daily commits (Default: {existing.get('commits', 'random')}): ").strip()
            except Exception:
                self.commits = ""
            if not self.commits:
                self.commits = existing.get("commits", "random")

            try:
                self.file = input(f"Commit File type (Default: {existing.get('file', 'py')}): ").strip()
            except Exception:
                self.file = ""
            if not self.file:
                self.file = existing.get("file", "py")

            print("Please follow date formating (year, month, day): Example: 2024, 1, 12")
            print("NOTE: No leading zeros.")

            try:
                self.starting_date = input(f"Enter starting date [{existing.get('starting_date', '')}]: ").strip()
            except Exception:
                self.starting_date = ""
            if not self.starting_date and "starting_date" in existing:
                self.starting_date = existing["starting_date"]

            try:
                self.ending_date = input(f"Enter ending date [{existing.get('ending_date', '')}]: ").strip()
            except Exception:
                self.ending_date = ""
            if not self.ending_date and "ending_date" in existing:
                self.ending_date = existing["ending_date"]

        configs = self.declare_settings()

        self.save_configs(configs)

        print("SETTINGS: Loaded ----------- ")
        print(f'Repository: {configs["repository"]}')
        print(f'Branch: {configs["branch"]}')
        print(
            f'Commits: {"random" if configs["commits"] == BLANK else configs["commits"]}'
        )
        print(f'File: {configs["file"]}')
        print(f"Starting_date: {self.starting_date}")
        print(f"ending_date: {self.ending_date}")

        print("-----------------------------")

        if return_configs:
            return configs

    def save_configs(self, cfgs):
        """todo"""
        with open(self.cfg_dir / CONFIG, "w", encoding="utf-8") as file:
            json.dump(cfgs, file)
