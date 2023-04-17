# :sparkles: This is the 0x00. SSH project for Holberton School Tulsa :sparkles:

Tasks:

0. use a private key

    write a bash script that uses ```ssh``` to connect to your server using the private key ```~/.ssh/school``` with the user ```ubuntu```

        Requirements:

            1. only use ```ssh``` single-character flags

            1. you cannot use ```-l```

            1. you do not need to handle the case of a private key protected by a passphrase

1. create an SSH key pair

    write a bash script that creates an RSA key pair:

        Requirements:

            1. name of the created private key must be ```school```

            1. number of bits in the created key to be created 4096

            1. the created key must be protected by the passphrase ```betty```

2. client configuration file

    your machine hasan SSH configuration file for the local SSH client, let's configure it to our needs so that you can connect to a server without typing a password. share your SSH client configuration in your answer file.

        Requirements:

            1. your SSH client configuration must be configured to use the private key ```~/.ssh/school```

            1. your SSH client configuration must be configured to refuse to authenticate using a password
