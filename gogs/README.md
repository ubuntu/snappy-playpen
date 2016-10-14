# GOGS snap

This project creates a working snap of GOGS = a go based git service


install snap - snap install gogs

point a browser to localhost:3001
To run as is, you will need to provide the mysql passwrd wich is stored in 
/var/snap/gogs/current/mysql/git_password

## Current state

Working features:

 * tested with mysql 

TODO
 * not validated yet with postgres
 * not validated on all snap system
 * build for oter archs (amd64 only right now)
 * update boost to dump rather than copy

