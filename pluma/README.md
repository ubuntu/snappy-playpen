# Pluma snap

This project attempts to create a working snap for Pluma, the text editor from 
the MATE Desktop environment. 

This is a multi-part snap because the MATE packages in the Xenial archive are 
built against GTK2 and I want to test MATE components from git master built 
against GTK3.

## Current state

  * The snap builds, although ``without-matedesktop` is required.
  * Running Pluma generates two warnings:

### Gtk-WARNING

This appears mostly harmless.

    (process:8641): Gtk-WARNING **: Locale not supported by C library.
        Using the fallback 'C' locale.

### EggSMClient-WARNING

This is a blocker. Pluma won't proceed without access to a session manager.

    (pluma:8641): EggSMClient-WARNING **: Failed to connect to the session manager: None of the authentication protocols specified are supported
