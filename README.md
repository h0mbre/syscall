## Syscall

Just a hacky script to display calling conventions for syscalls for `x86` and `x86_64`, information pulled from: https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md#x86-32_bit

## Usage

`python3 syscall <syscall> -x32 -x64`
```
h0mbre:~$ python3 syscall_tutor.py read -x32 -x64

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
