# Contributing to the Snappy Playpen

## Requirements

Snappy Playpen is a learning project, so we don't place too many restrictions
on the projects add to it. For your project to be added, it is important that:

 - it builds by just running `snapcraft cleanbuild` in the directory
 - you add a `README.md` file to your directory which explains
   - what your project is about
   - what others can learn from it
   - what the level of completion is
   - what still needs to be done
 - you update the software table in the top-level `README.md` file and
   indicate with either `:white_check_mark:` (working) or `:red_circle:` (not
   working) what the status of your snap is

Please note that we are going to consider removing a non-working snap from the
repo if we can't get it to work after a month without updates.

## How to contribute

Let's say we want to make a snap of `foo`.

 0. Ensure you [have a GitHub account](https://github.com/join), the `git`
 and `snapcraft` packages installed on your system, and Git
 [configured](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).
 1. Run the following in a terminal to get the playpen source:
 `git clone https://github.com/ubuntu/snappy-playpen.git`.
 2. Go into the source: `cd snappy-playpen`.
 3. Create a git branch for your snap: `git checkout -b foo`.
 4. Copy the template into a directory for your snap: `cp -r snap-template/ foo/`.
 5. Go into your snap directory: `cd foo/`.
 6. Edit the README.md and snapcraft.yaml files to your liking.
 7. Test your snap: `snapcraft`
 8. Go to the parent directory: `..`.
 9. Edit the README.md file adding a row in the table for your snap similar to this:
 `| :white_check_mark:  | `foo`              |                           |`.
 10. Add the files you edited/created: `git add README.md foo/`.
 11. Commit the files: `git commit -a`.
 12. Go to the Snappy Playpen [GitHub page](https://github.com/ubuntu/snappy-playpen)
 and fork Snapcraft.
 13. Add your fork as a git remote:
 `git remote add fork https://github.com/YOUR_GITHUB_USERNAME/snappy-playpen.git`.
 14. Push to your fork: `git push fork foo`
 15. Go to your fork's GitHub page, switch to the `foo` branch, and click:
 `New pull request`.
 16. Describe your snap and submit your pull request.
 17. Work with whoever responds to ensure your snap can get in. Repeat steps 5-7, 10-11, 14
 (your pull request will automatically update when you push to foo).
 18. When your pull request gets merged, delete the local and remote branches:
 `git push fork :foo && git checkout master && git branch -d foo`.

Congratulations! Your snap is now in the Playpen!
