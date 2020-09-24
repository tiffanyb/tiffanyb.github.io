# Week 6

# Build the image

# Run the image

  `docker run -v "/home/tiffanyb/Labs/week6/records":/tmp/records -p 6666:6666 --name week6 week6`

# Description
Turn off ASLR, because the attack depends on the condition that the base
address of libc doesn't change.

Known issue: folder permission
