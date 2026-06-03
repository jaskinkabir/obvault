# SSHFS
- This is pretty slow but easy to set up, only 2 commands
- This acts as a replacement for NFS
- `apt install sshfs`
- `sshfs hal@scruffy:/users /users`
# Rclone

## Initial Config
1. `apt install rclone`
2. `rclone config`
3. Type **`n`** for a "New remote"
4. **Name:** This name is local to your machine. In this file I'm calling it SCRUFFY
5. **Storage Type**: `sftp`
6. **User:** Your username on scruffy
7. **Port:** Hit enter for the default (22)
8. **Password:** Type n to use ssh keys instead
9. **key_pem**: Hit enter for default
10. **Key File**: Path to ssh private key
11. **key_passphrase:** Use if ssh your key uses a passphrase, otherwise hit enter
12. Accept the default for all the following settings
13. Quit config with `q`

## Manual Sync
- SSHFS and NFS would probably be too slow for working on Vivado remotely (haven't tested yet)
- Rclone's sync feature is better for us
- You can edit your vivado project locally in your `/users` directory, then manually call `rclone sync` to move it to scruffy before the build and call `rclone sync` again to pull the results back
- The command format is `rclone sync SOURCE DEST`
- For example, to push my local project changes to scruffy:
	- `rclone sync /users/USERNAME/VIVADO/PROJECT/PATH SCRUFFY:/users/USERNAME/VIVADO/PROJECT/PATH`
- Note that the rclone sync command is destructive and cannot be undone. You need to make sure you're writing the command in the right order or you may overwrite your local project with old data still on scruffy
## Mount 
- If you want to try the NFS way this is how to do it
- Normal mount command:
- `rclone mount SCRUFFY:/users/USERNAME /users/USERNAME --vfs-cache-mode writes`
- This mount command is optimized for speed, if you want to try using vivado directly over sftp. Haven't tried it yet but it probably sucks
```
rclone mount SCRUFFY:/users/USERNAME /users/USERNAME/ \
  --vfs-cache-mode full \
  --vfs-cache-max-age 24h \
  --vfs-cache-max-size 50G \
  --no-modtime \
  --cache-dir LOCAL/CACHE/DIRECTORY \
  --vfs-read-chunk-size 64M \
  --vfs-read-chunk-size-limit 2G &
```
- Big cache size of 50G for large Vivado projects

```
rclone mount scruffy-rcs:/users/jkabir /users/jkabir \
  --vfs-cache-mode full \
  --vfs-cache-max-age 24h \
  --vfs-cache-max-size 50G \
  --no-modtime \
  --cache-dir /home/jaskin/rclone_cache \
  --vfs-read-chunk-size 64M \
  --vfs-read-chunk-size-limit 2G \ &
```


## Unmount
`fusermount3 -u /users/USERNAME`