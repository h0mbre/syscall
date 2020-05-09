## Syscall

Just a hacky script to display calling conventions for syscalls for `x86` and `x86_64`, information pulled from: https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md#x86-32_bit

## Usage

To display both at once, just use both flags. To display one or the other, just use the one flag. 

```
h0mbre:~$ python3 syscall.py read -x32 -x64

'read' calling convention for x86 (32-bit):

+-----+-----------------+
| eax |     3/0x03      |
+-----+-----------------+
| ebx | unsigned int fd |
+-----+-----------------+
| ecx |    char *buf    |
+-----+-----------------+
| edx |  size_t count   |
+-----+-----------------+



'read' calling convention for x86_64 (64-bit):

+-----+-----------------+
| rax |     0/0x00      |
+-----+-----------------+
| rdi | unsigned int fd |
+-----+-----------------+
| rsi |    char *buf    |
+-----+-----------------+
| rdx |  size_t count   |
+-----+-----------------+
```

To display a generic calling convention for either architecture, same rules apply just use `'cheat'` as the syscall name.

```
h0mbre:~$ python3 syscall.py cheat -x32 -x64

x86 Calling Convention:


+-----+----------------+
| eax | syscall/return |
+-----+----------------+
| ebx |      arg0      |
+-----+----------------+
| ecx |      arg1      |
+-----+----------------+
| edx |      arg2      |
+-----+----------------+
| esi |      arg3      |
+-----+----------------+
| edi |      arg4      |
+-----+----------------+
| ebp |      arg5      |
+-----+----------------+



x86_64 Calling Convention:

+-----+----------------+
| rax | syscall/return |
+-----+----------------+
| rdi |      arg0      |
+-----+----------------+
| rsi |      arg1      |
+-----+----------------+
| rdx |      arg2      |
+-----+----------------+
| r10 |      arg3      |
+-----+----------------+
| r8  |      arg4      |
+-----+----------------+
| r9  |      arg5      |
+-----+----------------+
```

## Installation
You will have to `pip3 install beautifultable`.

The script needs access to the two text files in the repo as well, obviously you can set that up however you like. 
