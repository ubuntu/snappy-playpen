# Shotwell snap

This project creates a  snap of Gradio from github.

To get this done, we need to do the following:
 - build from master git

## Current state

Working features:

Known issues:
    - Fails to start with the following errors:
Unable to fork a new WebProcess: Failed to execute child process "/usr/lib/x86_64-linux-gnu/webkit2gtk-4.0/WebKitNetworkProcess" (No such file or directory).
Unable to fork a new WebProcess: Failed to execute child process "/usr/lib/x86_64-linux-gnu/webkit2gtk-4.0/WebKitWebProcess" (No such file or directory).
Failed to register: GDBus.Error:org.freedesktop.DBus.Error.AccessDenied: Connection ":1.437" is not allowed to own the service "de.haeckerfelix.gradio" due to AppArmor policy        
