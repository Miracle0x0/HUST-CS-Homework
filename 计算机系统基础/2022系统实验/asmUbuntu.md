```assembly

bomb：     文件格式 elf32-i386


Disassembly of section .init:

080486f4 <_init>:
 80486f4:	53                   	push   %ebx
 80486f5:	83 ec 08             	sub    $0x8,%esp
 80486f8:	e8 13 02 00 00       	call   8048910 <__x86.get_pc_thunk.bx>
 80486fd:	81 c3 03 39 00 00    	add    $0x3903,%ebx
 8048703:	8b 83 fc ff ff ff    	mov    -0x4(%ebx),%eax
 8048709:	85 c0                	test   %eax,%eax
 804870b:	74 05                	je     8048712 <_init+0x1e>
 804870d:	e8 be 01 00 00       	call   80488d0 <__sprintf_chk@plt+0x10>
 8048712:	83 c4 08             	add    $0x8,%esp
 8048715:	5b                   	pop    %ebx
 8048716:	c3                   	ret    

Disassembly of section .plt:

08048720 <read@plt-0x10>:
 8048720:	ff 35 04 c0 04 08    	pushl  0x804c004
 8048726:	ff 25 08 c0 04 08    	jmp    *0x804c008
 804872c:	00 00                	add    %al,(%eax)
	...

08048730 <read@plt>:
 8048730:	ff 25 0c c0 04 08    	jmp    *0x804c00c
 8048736:	68 00 00 00 00       	push   $0x0
 804873b:	e9 e0 ff ff ff       	jmp    8048720 <_init+0x2c>

08048740 <fflush@plt>:
 8048740:	ff 25 10 c0 04 08    	jmp    *0x804c010
 8048746:	68 08 00 00 00       	push   $0x8
 804874b:	e9 d0 ff ff ff       	jmp    8048720 <_init+0x2c>

08048750 <fgets@plt>:
 8048750:	ff 25 14 c0 04 08    	jmp    *0x804c014
 8048756:	68 10 00 00 00       	push   $0x10
 804875b:	e9 c0 ff ff ff       	jmp    8048720 <_init+0x2c>

08048760 <signal@plt>:
 8048760:	ff 25 18 c0 04 08    	jmp    *0x804c018
 8048766:	68 18 00 00 00       	push   $0x18
 804876b:	e9 b0 ff ff ff       	jmp    8048720 <_init+0x2c>

08048770 <sleep@plt>:
 8048770:	ff 25 1c c0 04 08    	jmp    *0x804c01c
 8048776:	68 20 00 00 00       	push   $0x20
 804877b:	e9 a0 ff ff ff       	jmp    8048720 <_init+0x2c>

08048780 <alarm@plt>:
 8048780:	ff 25 20 c0 04 08    	jmp    *0x804c020
 8048786:	68 28 00 00 00       	push   $0x28
 804878b:	e9 90 ff ff ff       	jmp    8048720 <_init+0x2c>

08048790 <__stack_chk_fail@plt>:
 8048790:	ff 25 24 c0 04 08    	jmp    *0x804c024
 8048796:	68 30 00 00 00       	push   $0x30
 804879b:	e9 80 ff ff ff       	jmp    8048720 <_init+0x2c>

080487a0 <strcpy@plt>:
 80487a0:	ff 25 28 c0 04 08    	jmp    *0x804c028
 80487a6:	68 38 00 00 00       	push   $0x38
 80487ab:	e9 70 ff ff ff       	jmp    8048720 <_init+0x2c>

080487b0 <getenv@plt>:
 80487b0:	ff 25 2c c0 04 08    	jmp    *0x804c02c
 80487b6:	68 40 00 00 00       	push   $0x40
 80487bb:	e9 60 ff ff ff       	jmp    8048720 <_init+0x2c>

080487c0 <puts@plt>:
 80487c0:	ff 25 30 c0 04 08    	jmp    *0x804c030
 80487c6:	68 48 00 00 00       	push   $0x48
 80487cb:	e9 50 ff ff ff       	jmp    8048720 <_init+0x2c>

080487d0 <__memmove_chk@plt>:
 80487d0:	ff 25 34 c0 04 08    	jmp    *0x804c034
 80487d6:	68 50 00 00 00       	push   $0x50
 80487db:	e9 40 ff ff ff       	jmp    8048720 <_init+0x2c>

080487e0 <exit@plt>:
 80487e0:	ff 25 38 c0 04 08    	jmp    *0x804c038
 80487e6:	68 58 00 00 00       	push   $0x58
 80487eb:	e9 30 ff ff ff       	jmp    8048720 <_init+0x2c>

080487f0 <__libc_start_main@plt>:
 80487f0:	ff 25 3c c0 04 08    	jmp    *0x804c03c
 80487f6:	68 60 00 00 00       	push   $0x60
 80487fb:	e9 20 ff ff ff       	jmp    8048720 <_init+0x2c>

08048800 <write@plt>:
 8048800:	ff 25 40 c0 04 08    	jmp    *0x804c040
 8048806:	68 68 00 00 00       	push   $0x68
 804880b:	e9 10 ff ff ff       	jmp    8048720 <_init+0x2c>

08048810 <__isoc99_sscanf@plt>:
 8048810:	ff 25 44 c0 04 08    	jmp    *0x804c044
 8048816:	68 70 00 00 00       	push   $0x70
 804881b:	e9 00 ff ff ff       	jmp    8048720 <_init+0x2c>

08048820 <fopen@plt>:
 8048820:	ff 25 48 c0 04 08    	jmp    *0x804c048
 8048826:	68 78 00 00 00       	push   $0x78
 804882b:	e9 f0 fe ff ff       	jmp    8048720 <_init+0x2c>

08048830 <__errno_location@plt>:
 8048830:	ff 25 4c c0 04 08    	jmp    *0x804c04c
 8048836:	68 80 00 00 00       	push   $0x80
 804883b:	e9 e0 fe ff ff       	jmp    8048720 <_init+0x2c>

08048840 <__printf_chk@plt>:
 8048840:	ff 25 50 c0 04 08    	jmp    *0x804c050
 8048846:	68 88 00 00 00       	push   $0x88
 804884b:	e9 d0 fe ff ff       	jmp    8048720 <_init+0x2c>

08048850 <socket@plt>:
 8048850:	ff 25 54 c0 04 08    	jmp    *0x804c054
 8048856:	68 90 00 00 00       	push   $0x90
 804885b:	e9 c0 fe ff ff       	jmp    8048720 <_init+0x2c>

08048860 <__fprintf_chk@plt>:
 8048860:	ff 25 58 c0 04 08    	jmp    *0x804c058
 8048866:	68 98 00 00 00       	push   $0x98
 804886b:	e9 b0 fe ff ff       	jmp    8048720 <_init+0x2c>

08048870 <gethostbyname@plt>:
 8048870:	ff 25 5c c0 04 08    	jmp    *0x804c05c
 8048876:	68 a0 00 00 00       	push   $0xa0
 804887b:	e9 a0 fe ff ff       	jmp    8048720 <_init+0x2c>

08048880 <strtol@plt>:
 8048880:	ff 25 60 c0 04 08    	jmp    *0x804c060
 8048886:	68 a8 00 00 00       	push   $0xa8
 804888b:	e9 90 fe ff ff       	jmp    8048720 <_init+0x2c>

08048890 <connect@plt>:
 8048890:	ff 25 64 c0 04 08    	jmp    *0x804c064
 8048896:	68 b0 00 00 00       	push   $0xb0
 804889b:	e9 80 fe ff ff       	jmp    8048720 <_init+0x2c>

080488a0 <close@plt>:
 80488a0:	ff 25 68 c0 04 08    	jmp    *0x804c068
 80488a6:	68 b8 00 00 00       	push   $0xb8
 80488ab:	e9 70 fe ff ff       	jmp    8048720 <_init+0x2c>

080488b0 <__ctype_b_loc@plt>:
 80488b0:	ff 25 6c c0 04 08    	jmp    *0x804c06c
 80488b6:	68 c0 00 00 00       	push   $0xc0
 80488bb:	e9 60 fe ff ff       	jmp    8048720 <_init+0x2c>

080488c0 <__sprintf_chk@plt>:
 80488c0:	ff 25 70 c0 04 08    	jmp    *0x804c070
 80488c6:	68 c8 00 00 00       	push   $0xc8
 80488cb:	e9 50 fe ff ff       	jmp    8048720 <_init+0x2c>

Disassembly of section .plt.got:

080488d0 <.plt.got>:
 80488d0:	ff 25 fc bf 04 08    	jmp    *0x804bffc
 80488d6:	66 90                	xchg   %ax,%ax

Disassembly of section .text:

080488e0 <_start>:
 80488e0:	31 ed                	xor    %ebp,%ebp
 80488e2:	5e                   	pop    %esi
 80488e3:	89 e1                	mov    %esp,%ecx
 80488e5:	83 e4 f0             	and    $0xfffffff0,%esp
 80488e8:	50                   	push   %eax
 80488e9:	54                   	push   %esp
 80488ea:	52                   	push   %edx
 80488eb:	68 a0 9e 04 08       	push   $0x8049ea0
 80488f0:	68 40 9e 04 08       	push   $0x8049e40
 80488f5:	51                   	push   %ecx
 80488f6:	56                   	push   %esi
 80488f7:	68 db 89 04 08       	push   $0x80489db
 80488fc:	e8 ef fe ff ff       	call   80487f0 <__libc_start_main@plt>
 8048901:	f4                   	hlt    
 8048902:	66 90                	xchg   %ax,%ax
 8048904:	66 90                	xchg   %ax,%ax
 8048906:	66 90                	xchg   %ax,%ax
 8048908:	66 90                	xchg   %ax,%ax
 804890a:	66 90                	xchg   %ax,%ax
 804890c:	66 90                	xchg   %ax,%ax
 804890e:	66 90                	xchg   %ax,%ax

08048910 <__x86.get_pc_thunk.bx>:
 8048910:	8b 1c 24             	mov    (%esp),%ebx
 8048913:	c3                   	ret    
 8048914:	66 90                	xchg   %ax,%ax
 8048916:	66 90                	xchg   %ax,%ax
 8048918:	66 90                	xchg   %ax,%ax
 804891a:	66 90                	xchg   %ax,%ax
 804891c:	66 90                	xchg   %ax,%ax
 804891e:	66 90                	xchg   %ax,%ax

08048920 <deregister_tm_clones>:
 8048920:	b8 a3 c3 04 08       	mov    $0x804c3a3,%eax
 8048925:	2d a0 c3 04 08       	sub    $0x804c3a0,%eax
 804892a:	83 f8 06             	cmp    $0x6,%eax
 804892d:	76 1a                	jbe    8048949 <deregister_tm_clones+0x29>
 804892f:	b8 00 00 00 00       	mov    $0x0,%eax
 8048934:	85 c0                	test   %eax,%eax
 8048936:	74 11                	je     8048949 <deregister_tm_clones+0x29>
 8048938:	55                   	push   %ebp
 8048939:	89 e5                	mov    %esp,%ebp
 804893b:	83 ec 14             	sub    $0x14,%esp
 804893e:	68 a0 c3 04 08       	push   $0x804c3a0
 8048943:	ff d0                	call   *%eax
 8048945:	83 c4 10             	add    $0x10,%esp
 8048948:	c9                   	leave  
 8048949:	f3 c3                	repz ret 
 804894b:	90                   	nop
 804894c:	8d 74 26 00          	lea    0x0(%esi,%eiz,1),%esi

08048950 <register_tm_clones>:
 8048950:	b8 a0 c3 04 08       	mov    $0x804c3a0,%eax
 8048955:	2d a0 c3 04 08       	sub    $0x804c3a0,%eax
 804895a:	c1 f8 02             	sar    $0x2,%eax
 804895d:	89 c2                	mov    %eax,%edx
 804895f:	c1 ea 1f             	shr    $0x1f,%edx
 8048962:	01 d0                	add    %edx,%eax
 8048964:	d1 f8                	sar    %eax
 8048966:	74 1b                	je     8048983 <register_tm_clones+0x33>
 8048968:	ba 00 00 00 00       	mov    $0x0,%edx
 804896d:	85 d2                	test   %edx,%edx
 804896f:	74 12                	je     8048983 <register_tm_clones+0x33>
 8048971:	55                   	push   %ebp
 8048972:	89 e5                	mov    %esp,%ebp
 8048974:	83 ec 10             	sub    $0x10,%esp
 8048977:	50                   	push   %eax
 8048978:	68 a0 c3 04 08       	push   $0x804c3a0
 804897d:	ff d2                	call   *%edx
 804897f:	83 c4 10             	add    $0x10,%esp
 8048982:	c9                   	leave  
 8048983:	f3 c3                	repz ret 
 8048985:	8d 74 26 00          	lea    0x0(%esi,%eiz,1),%esi
 8048989:	8d bc 27 00 00 00 00 	lea    0x0(%edi,%eiz,1),%edi

08048990 <__do_global_dtors_aux>:
 8048990:	80 3d c8 c3 04 08 00 	cmpb   $0x0,0x804c3c8
 8048997:	75 13                	jne    80489ac <__do_global_dtors_aux+0x1c>
 8048999:	55                   	push   %ebp
 804899a:	89 e5                	mov    %esp,%ebp
 804899c:	83 ec 08             	sub    $0x8,%esp
 804899f:	e8 7c ff ff ff       	call   8048920 <deregister_tm_clones>
 80489a4:	c6 05 c8 c3 04 08 01 	movb   $0x1,0x804c3c8
 80489ab:	c9                   	leave  
 80489ac:	f3 c3                	repz ret 
 80489ae:	66 90                	xchg   %ax,%ax

080489b0 <frame_dummy>:
 80489b0:	b8 10 bf 04 08       	mov    $0x804bf10,%eax
 80489b5:	8b 10                	mov    (%eax),%edx
 80489b7:	85 d2                	test   %edx,%edx
 80489b9:	75 05                	jne    80489c0 <frame_dummy+0x10>
 80489bb:	eb 93                	jmp    8048950 <register_tm_clones>
 80489bd:	8d 76 00             	lea    0x0(%esi),%esi
 80489c0:	ba 00 00 00 00       	mov    $0x0,%edx
 80489c5:	85 d2                	test   %edx,%edx
 80489c7:	74 f2                	je     80489bb <frame_dummy+0xb>
 80489c9:	55                   	push   %ebp
 80489ca:	89 e5                	mov    %esp,%ebp
 80489cc:	83 ec 14             	sub    $0x14,%esp
 80489cf:	50                   	push   %eax
 80489d0:	ff d2                	call   *%edx
 80489d2:	83 c4 10             	add    $0x10,%esp
 80489d5:	c9                   	leave  
 80489d6:	e9 75 ff ff ff       	jmp    8048950 <register_tm_clones>

080489db <main>:
 80489db:	8d 4c 24 04          	lea    0x4(%esp),%ecx
 80489df:	83 e4 f0             	and    $0xfffffff0,%esp
 80489e2:	ff 71 fc             	pushl  -0x4(%ecx)
 80489e5:	55                   	push   %ebp
 80489e6:	89 e5                	mov    %esp,%ebp
 80489e8:	53                   	push   %ebx
 80489e9:	51                   	push   %ecx
 80489ea:	8b 01                	mov    (%ecx),%eax
 80489ec:	8b 59 04             	mov    0x4(%ecx),%ebx
 80489ef:	83 f8 01             	cmp    $0x1,%eax
 80489f2:	75 0c                	jne    8048a00 <main+0x25>
 80489f4:	a1 c0 c3 04 08       	mov    0x804c3c0,%eax
 80489f9:	a3 d0 c3 04 08       	mov    %eax,0x804c3d0
 80489fe:	eb 5b                	jmp    8048a5b <main+0x80>
 8048a00:	83 f8 02             	cmp    $0x2,%eax
 8048a03:	75 39                	jne    8048a3e <main+0x63>
 8048a05:	83 ec 08             	sub    $0x8,%esp
 8048a08:	68 c0 9e 04 08       	push   $0x8049ec0
 8048a0d:	ff 73 04             	pushl  0x4(%ebx)
 8048a10:	e8 0b fe ff ff       	call   8048820 <fopen@plt>
 8048a15:	a3 d0 c3 04 08       	mov    %eax,0x804c3d0
 8048a1a:	83 c4 10             	add    $0x10,%esp
 8048a1d:	85 c0                	test   %eax,%eax
 8048a1f:	75 3a                	jne    8048a5b <main+0x80>
 8048a21:	ff 73 04             	pushl  0x4(%ebx)
 8048a24:	ff 33                	pushl  (%ebx)
 8048a26:	68 c2 9e 04 08       	push   $0x8049ec2
 8048a2b:	6a 01                	push   $0x1
 8048a2d:	e8 0e fe ff ff       	call   8048840 <__printf_chk@plt>
 8048a32:	c7 04 24 08 00 00 00 	movl   $0x8,(%esp)
 8048a39:	e8 a2 fd ff ff       	call   80487e0 <exit@plt>
 8048a3e:	83 ec 04             	sub    $0x4,%esp
 8048a41:	ff 33                	pushl  (%ebx)
 8048a43:	68 df 9e 04 08       	push   $0x8049edf
 8048a48:	6a 01                	push   $0x1
 8048a4a:	e8 f1 fd ff ff       	call   8048840 <__printf_chk@plt>
 8048a4f:	c7 04 24 08 00 00 00 	movl   $0x8,(%esp)
 8048a56:	e8 85 fd ff ff       	call   80487e0 <exit@plt>
 8048a5b:	e8 06 06 00 00       	call   8049066 <initialize_bomb>
 8048a60:	83 ec 0c             	sub    $0xc,%esp
 8048a63:	68 44 9f 04 08       	push   $0x8049f44
 8048a68:	e8 53 fd ff ff       	call   80487c0 <puts@plt>
 8048a6d:	c7 04 24 80 9f 04 08 	movl   $0x8049f80,(%esp)
 8048a74:	e8 47 fd ff ff       	call   80487c0 <puts@plt>
 8048a79:	e8 da 06 00 00       	call   8049158 <read_line>
 8048a7e:	89 04 24             	mov    %eax,(%esp)
 8048a81:	e8 ad 00 00 00       	call   8048b33 <phase_1>
 8048a86:	e8 c6 07 00 00       	call   8049251 <phase_defused>
 8048a8b:	c7 04 24 ac 9f 04 08 	movl   $0x8049fac,(%esp)
 8048a92:	e8 29 fd ff ff       	call   80487c0 <puts@plt>
 8048a97:	e8 bc 06 00 00       	call   8049158 <read_line>
 8048a9c:	89 04 24             	mov    %eax,(%esp)
 8048a9f:	e8 b0 00 00 00       	call   8048b54 <phase_2>
 8048aa4:	e8 a8 07 00 00       	call   8049251 <phase_defused>
 8048aa9:	c7 04 24 f9 9e 04 08 	movl   $0x8049ef9,(%esp)
 8048ab0:	e8 0b fd ff ff       	call   80487c0 <puts@plt>
 8048ab5:	e8 9e 06 00 00       	call   8049158 <read_line>
 8048aba:	89 04 24             	mov    %eax,(%esp)
 8048abd:	e8 f3 00 00 00       	call   8048bb5 <phase_3>
 8048ac2:	e8 8a 07 00 00       	call   8049251 <phase_defused>
 8048ac7:	c7 04 24 17 9f 04 08 	movl   $0x8049f17,(%esp)
 8048ace:	e8 ed fc ff ff       	call   80487c0 <puts@plt>
 8048ad3:	e8 80 06 00 00       	call   8049158 <read_line>
 8048ad8:	89 04 24             	mov    %eax,(%esp)
 8048adb:	e8 01 02 00 00       	call   8048ce1 <phase_4>
 8048ae0:	e8 6c 07 00 00       	call   8049251 <phase_defused>
 8048ae5:	c7 04 24 d8 9f 04 08 	movl   $0x8049fd8,(%esp)
 8048aec:	e8 cf fc ff ff       	call   80487c0 <puts@plt>
 8048af1:	e8 62 06 00 00       	call   8049158 <read_line>
 8048af6:	89 04 24             	mov    %eax,(%esp)
 8048af9:	e8 58 02 00 00       	call   8048d56 <phase_5>
 8048afe:	e8 4e 07 00 00       	call   8049251 <phase_defused>
 8048b03:	c7 04 24 26 9f 04 08 	movl   $0x8049f26,(%esp)
 8048b0a:	e8 b1 fc ff ff       	call   80487c0 <puts@plt>
 8048b0f:	e8 44 06 00 00       	call   8049158 <read_line>
 8048b14:	89 04 24             	mov    %eax,(%esp)
 8048b17:	e8 ba 02 00 00       	call   8048dd6 <phase_6>
 8048b1c:	e8 30 07 00 00       	call   8049251 <phase_defused>
 8048b21:	83 c4 10             	add    $0x10,%esp
 8048b24:	b8 00 00 00 00       	mov    $0x0,%eax
 8048b29:	8d 65 f8             	lea    -0x8(%ebp),%esp
 8048b2c:	59                   	pop    %ecx
 8048b2d:	5b                   	pop    %ebx
 8048b2e:	5d                   	pop    %ebp
 8048b2f:	8d 61 fc             	lea    -0x4(%ecx),%esp
 8048b32:	c3                   	ret    

08048b33 <phase_1>:
 8048b33:	83 ec 14             	sub    $0x14,%esp
 8048b36:	68 fc 9f 04 08       	push   $0x8049ffc
 8048b3b:	ff 74 24 1c          	pushl  0x1c(%esp)
 8048b3f:	e8 bd 04 00 00       	call   8049001 <strings_not_equal>
 8048b44:	83 c4 10             	add    $0x10,%esp
 8048b47:	85 c0                	test   %eax,%eax
 8048b49:	74 05                	je     8048b50 <phase_1+0x1d>
 8048b4b:	e8 a8 05 00 00       	call   80490f8 <explode_bomb>
 8048b50:	83 c4 0c             	add    $0xc,%esp
 8048b53:	c3                   	ret    

08048b54 <phase_2>:
 8048b54:	53                   	push   %ebx
 8048b55:	83 ec 30             	sub    $0x30,%esp
 8048b58:	65 a1 14 00 00 00    	mov    %gs:0x14,%eax
 8048b5e:	89 44 24 24          	mov    %eax,0x24(%esp)
 8048b62:	31 c0                	xor    %eax,%eax
 8048b64:	8d 44 24 0c          	lea    0xc(%esp),%eax
 8048b68:	50                   	push   %eax
 8048b69:	ff 74 24 3c          	pushl  0x3c(%esp)
 8048b6d:	e8 ab 05 00 00       	call   804911d <read_six_numbers>
 8048b72:	83 c4 10             	add    $0x10,%esp
 8048b75:	83 7c 24 04 00       	cmpl   $0x0,0x4(%esp)
 8048b7a:	79 05                	jns    8048b81 <phase_2+0x2d>
 8048b7c:	e8 77 05 00 00       	call   80490f8 <explode_bomb>
 8048b81:	bb 01 00 00 00       	mov    $0x1,%ebx
 8048b86:	89 d8                	mov    %ebx,%eax
 8048b88:	03 04 9c             	add    (%esp,%ebx,4),%eax
 8048b8b:	39 44 9c 04          	cmp    %eax,0x4(%esp,%ebx,4)
 8048b8f:	74 05                	je     8048b96 <phase_2+0x42>
 8048b91:	e8 62 05 00 00       	call   80490f8 <explode_bomb>
 8048b96:	83 c3 01             	add    $0x1,%ebx
 8048b99:	83 fb 06             	cmp    $0x6,%ebx
 8048b9c:	75 e8                	jne    8048b86 <phase_2+0x32>
 8048b9e:	8b 44 24 1c          	mov    0x1c(%esp),%eax
 8048ba2:	65 33 05 14 00 00 00 	xor    %gs:0x14,%eax
 8048ba9:	74 05                	je     8048bb0 <phase_2+0x5c>
 8048bab:	e8 e0 fb ff ff       	call   8048790 <__stack_chk_fail@plt>
 8048bb0:	83 c4 28             	add    $0x28,%esp
 8048bb3:	5b                   	pop    %ebx
 8048bb4:	c3                   	ret    

08048bb5 <phase_3>:
 8048bb5:	83 ec 1c             	sub    $0x1c,%esp
 8048bb8:	65 a1 14 00 00 00    	mov    %gs:0x14,%eax
 8048bbe:	89 44 24 0c          	mov    %eax,0xc(%esp)
 8048bc2:	31 c0                	xor    %eax,%eax
 8048bc4:	8d 44 24 08          	lea    0x8(%esp),%eax
 8048bc8:	50                   	push   %eax
 8048bc9:	8d 44 24 08          	lea    0x8(%esp),%eax
 8048bcd:	50                   	push   %eax
 8048bce:	68 9f a1 04 08       	push   $0x804a19f
 8048bd3:	ff 74 24 2c          	pushl  0x2c(%esp)
 8048bd7:	e8 34 fc ff ff       	call   8048810 <__isoc99_sscanf@plt>
 8048bdc:	83 c4 10             	add    $0x10,%esp
 8048bdf:	83 f8 01             	cmp    $0x1,%eax
 8048be2:	7f 05                	jg     8048be9 <phase_3+0x34>
 8048be4:	e8 0f 05 00 00       	call   80490f8 <explode_bomb>
 8048be9:	83 7c 24 04 07       	cmpl   $0x7,0x4(%esp)
 8048bee:	77 66                	ja     8048c56 <phase_3+0xa1>
 8048bf0:	8b 44 24 04          	mov    0x4(%esp),%eax
 8048bf4:	ff 24 85 60 a0 04 08 	jmp    *0x804a060(,%eax,4)
 8048bfb:	b8 2d 02 00 00       	mov    $0x22d,%eax
 8048c00:	eb 05                	jmp    8048c07 <phase_3+0x52>
 8048c02:	b8 00 00 00 00       	mov    $0x0,%eax
 8048c07:	2d 20 02 00 00       	sub    $0x220,%eax
 8048c0c:	eb 05                	jmp    8048c13 <phase_3+0x5e>
 8048c0e:	b8 00 00 00 00       	mov    $0x0,%eax
 8048c13:	05 aa 01 00 00       	add    $0x1aa,%eax
 8048c18:	eb 05                	jmp    8048c1f <phase_3+0x6a>
 8048c1a:	b8 00 00 00 00       	mov    $0x0,%eax
 8048c1f:	2d 05 03 00 00       	sub    $0x305,%eax
 8048c24:	eb 05                	jmp    8048c2b <phase_3+0x76>
 8048c26:	b8 00 00 00 00       	mov    $0x0,%eax
 8048c2b:	05 05 03 00 00       	add    $0x305,%eax
 8048c30:	eb 05                	jmp    8048c37 <phase_3+0x82>
 8048c32:	b8 00 00 00 00       	mov    $0x0,%eax
 8048c37:	2d 05 03 00 00       	sub    $0x305,%eax
 8048c3c:	eb 05                	jmp    8048c43 <phase_3+0x8e>
 8048c3e:	b8 00 00 00 00       	mov    $0x0,%eax
 8048c43:	05 05 03 00 00       	add    $0x305,%eax
 8048c48:	eb 05                	jmp    8048c4f <phase_3+0x9a>
 8048c4a:	b8 00 00 00 00       	mov    $0x0,%eax
 8048c4f:	2d 05 03 00 00       	sub    $0x305,%eax
 8048c54:	eb 0a                	jmp    8048c60 <phase_3+0xab>
 8048c56:	e8 9d 04 00 00       	call   80490f8 <explode_bomb>
 8048c5b:	b8 00 00 00 00       	mov    $0x0,%eax
 8048c60:	83 7c 24 04 05       	cmpl   $0x5,0x4(%esp)
 8048c65:	7f 06                	jg     8048c6d <phase_3+0xb8>
 8048c67:	3b 44 24 08          	cmp    0x8(%esp),%eax
 8048c6b:	74 05                	je     8048c72 <phase_3+0xbd>
 8048c6d:	e8 86 04 00 00       	call   80490f8 <explode_bomb>
 8048c72:	8b 44 24 0c          	mov    0xc(%esp),%eax
 8048c76:	65 33 05 14 00 00 00 	xor    %gs:0x14,%eax
 8048c7d:	74 05                	je     8048c84 <phase_3+0xcf>
 8048c7f:	e8 0c fb ff ff       	call   8048790 <__stack_chk_fail@plt>
 8048c84:	83 c4 1c             	add    $0x1c,%esp
 8048c87:	c3                   	ret    

08048c88 <func4>:
 8048c88:	56                   	push   %esi
 8048c89:	53                   	push   %ebx
 8048c8a:	83 ec 04             	sub    $0x4,%esp
 8048c8d:	8b 54 24 10          	mov    0x10(%esp),%edx
 8048c91:	8b 74 24 14          	mov    0x14(%esp),%esi
 8048c95:	8b 4c 24 18          	mov    0x18(%esp),%ecx
 8048c99:	89 c8                	mov    %ecx,%eax
 8048c9b:	29 f0                	sub    %esi,%eax
 8048c9d:	89 c3                	mov    %eax,%ebx
 8048c9f:	c1 eb 1f             	shr    $0x1f,%ebx
 8048ca2:	01 d8                	add    %ebx,%eax
 8048ca4:	d1 f8                	sar    %eax
 8048ca6:	8d 1c 30             	lea    (%eax,%esi,1),%ebx
 8048ca9:	39 d3                	cmp    %edx,%ebx
 8048cab:	7e 15                	jle    8048cc2 <func4+0x3a>
 8048cad:	83 ec 04             	sub    $0x4,%esp
 8048cb0:	8d 43 ff             	lea    -0x1(%ebx),%eax
 8048cb3:	50                   	push   %eax
 8048cb4:	56                   	push   %esi
 8048cb5:	52                   	push   %edx
 8048cb6:	e8 cd ff ff ff       	call   8048c88 <func4>
 8048cbb:	83 c4 10             	add    $0x10,%esp
 8048cbe:	01 d8                	add    %ebx,%eax
 8048cc0:	eb 19                	jmp    8048cdb <func4+0x53>
 8048cc2:	89 d8                	mov    %ebx,%eax
 8048cc4:	39 d3                	cmp    %edx,%ebx
 8048cc6:	7d 13                	jge    8048cdb <func4+0x53>
 8048cc8:	83 ec 04             	sub    $0x4,%esp
 8048ccb:	51                   	push   %ecx
 8048ccc:	8d 43 01             	lea    0x1(%ebx),%eax
 8048ccf:	50                   	push   %eax
 8048cd0:	52                   	push   %edx
 8048cd1:	e8 b2 ff ff ff       	call   8048c88 <func4>
 8048cd6:	83 c4 10             	add    $0x10,%esp
 8048cd9:	01 d8                	add    %ebx,%eax
 8048cdb:	83 c4 04             	add    $0x4,%esp
 8048cde:	5b                   	pop    %ebx
 8048cdf:	5e                   	pop    %esi
 8048ce0:	c3                   	ret    

08048ce1 <phase_4>:
 8048ce1:	83 ec 1c             	sub    $0x1c,%esp
 8048ce4:	65 a1 14 00 00 00    	mov    %gs:0x14,%eax
 8048cea:	89 44 24 0c          	mov    %eax,0xc(%esp)
 8048cee:	31 c0                	xor    %eax,%eax
 8048cf0:	8d 44 24 08          	lea    0x8(%esp),%eax
 8048cf4:	50                   	push   %eax
 8048cf5:	8d 44 24 08          	lea    0x8(%esp),%eax
 8048cf9:	50                   	push   %eax
 8048cfa:	68 9f a1 04 08       	push   $0x804a19f
 8048cff:	ff 74 24 2c          	pushl  0x2c(%esp)
 8048d03:	e8 08 fb ff ff       	call   8048810 <__isoc99_sscanf@plt>
 8048d08:	83 c4 10             	add    $0x10,%esp
 8048d0b:	83 f8 02             	cmp    $0x2,%eax
 8048d0e:	75 07                	jne    8048d17 <phase_4+0x36>
 8048d10:	83 7c 24 04 0e       	cmpl   $0xe,0x4(%esp)
 8048d15:	76 05                	jbe    8048d1c <phase_4+0x3b>
 8048d17:	e8 dc 03 00 00       	call   80490f8 <explode_bomb>
 8048d1c:	83 ec 04             	sub    $0x4,%esp
 8048d1f:	6a 0e                	push   $0xe
 8048d21:	6a 00                	push   $0x0
 8048d23:	ff 74 24 10          	pushl  0x10(%esp)
 8048d27:	e8 5c ff ff ff       	call   8048c88 <func4>
 8048d2c:	83 c4 10             	add    $0x10,%esp
 8048d2f:	83 f8 2d             	cmp    $0x2d,%eax
 8048d32:	75 07                	jne    8048d3b <phase_4+0x5a>
 8048d34:	83 7c 24 08 2d       	cmpl   $0x2d,0x8(%esp)
 8048d39:	74 05                	je     8048d40 <phase_4+0x5f>
 8048d3b:	e8 b8 03 00 00       	call   80490f8 <explode_bomb>
 8048d40:	8b 44 24 0c          	mov    0xc(%esp),%eax
 8048d44:	65 33 05 14 00 00 00 	xor    %gs:0x14,%eax
 8048d4b:	74 05                	je     8048d52 <phase_4+0x71>
 8048d4d:	e8 3e fa ff ff       	call   8048790 <__stack_chk_fail@plt>
 8048d52:	83 c4 1c             	add    $0x1c,%esp
 8048d55:	c3                   	ret    

08048d56 <phase_5>:
 8048d56:	53                   	push   %ebx
 8048d57:	83 ec 24             	sub    $0x24,%esp
 8048d5a:	8b 5c 24 2c          	mov    0x2c(%esp),%ebx
 8048d5e:	65 a1 14 00 00 00    	mov    %gs:0x14,%eax
 8048d64:	89 44 24 18          	mov    %eax,0x18(%esp)
 8048d68:	31 c0                	xor    %eax,%eax
 8048d6a:	53                   	push   %ebx
 8048d6b:	e8 72 02 00 00       	call   8048fe2 <string_length>
 8048d70:	83 c4 10             	add    $0x10,%esp
 8048d73:	83 f8 06             	cmp    $0x6,%eax
 8048d76:	74 05                	je     8048d7d <phase_5+0x27>
 8048d78:	e8 7b 03 00 00       	call   80490f8 <explode_bomb>
 8048d7d:	b8 00 00 00 00       	mov    $0x0,%eax
 8048d82:	0f b6 14 03          	movzbl (%ebx,%eax,1),%edx
 8048d86:	83 e2 0f             	and    $0xf,%edx
 8048d89:	0f b6 92 80 a0 04 08 	movzbl 0x804a080(%edx),%edx
 8048d90:	88 54 04 05          	mov    %dl,0x5(%esp,%eax,1)
 8048d94:	83 c0 01             	add    $0x1,%eax
 8048d97:	83 f8 06             	cmp    $0x6,%eax
 8048d9a:	75 e6                	jne    8048d82 <phase_5+0x2c>
 8048d9c:	c6 44 24 0b 00       	movb   $0x0,0xb(%esp)
 8048da1:	83 ec 08             	sub    $0x8,%esp
 8048da4:	68 56 a0 04 08       	push   $0x804a056
 8048da9:	8d 44 24 11          	lea    0x11(%esp),%eax
 8048dad:	50                   	push   %eax
 8048dae:	e8 4e 02 00 00       	call   8049001 <strings_not_equal>
 8048db3:	83 c4 10             	add    $0x10,%esp
 8048db6:	85 c0                	test   %eax,%eax
 8048db8:	74 05                	je     8048dbf <phase_5+0x69>
 8048dba:	e8 39 03 00 00       	call   80490f8 <explode_bomb>
 8048dbf:	8b 44 24 0c          	mov    0xc(%esp),%eax
 8048dc3:	65 33 05 14 00 00 00 	xor    %gs:0x14,%eax
 8048dca:	74 05                	je     8048dd1 <phase_5+0x7b>
 8048dcc:	e8 bf f9 ff ff       	call   8048790 <__stack_chk_fail@plt>
 8048dd1:	83 c4 18             	add    $0x18,%esp
 8048dd4:	5b                   	pop    %ebx
 8048dd5:	c3                   	ret    

08048dd6 <phase_6>:
 8048dd6:	56                   	push   %esi
 8048dd7:	53                   	push   %ebx
 8048dd8:	83 ec 4c             	sub    $0x4c,%esp
 8048ddb:	65 a1 14 00 00 00    	mov    %gs:0x14,%eax
 8048de1:	89 44 24 44          	mov    %eax,0x44(%esp)
 8048de5:	31 c0                	xor    %eax,%eax
 8048de7:	8d 44 24 14          	lea    0x14(%esp),%eax
 8048deb:	50                   	push   %eax
 8048dec:	ff 74 24 5c          	pushl  0x5c(%esp)
 8048df0:	e8 28 03 00 00       	call   804911d <read_six_numbers>
 8048df5:	83 c4 10             	add    $0x10,%esp
 8048df8:	be 00 00 00 00       	mov    $0x0,%esi
 8048dfd:	8b 44 b4 0c          	mov    0xc(%esp,%esi,4),%eax
 8048e01:	83 e8 01             	sub    $0x1,%eax
 8048e04:	83 f8 05             	cmp    $0x5,%eax
 8048e07:	76 05                	jbe    8048e0e <phase_6+0x38>
 8048e09:	e8 ea 02 00 00       	call   80490f8 <explode_bomb>
 8048e0e:	83 c6 01             	add    $0x1,%esi
 8048e11:	83 fe 06             	cmp    $0x6,%esi
 8048e14:	74 33                	je     8048e49 <phase_6+0x73>
 8048e16:	89 f3                	mov    %esi,%ebx
 8048e18:	8b 44 9c 0c          	mov    0xc(%esp,%ebx,4),%eax
 8048e1c:	39 44 b4 08          	cmp    %eax,0x8(%esp,%esi,4)
 8048e20:	75 05                	jne    8048e27 <phase_6+0x51>
 8048e22:	e8 d1 02 00 00       	call   80490f8 <explode_bomb>
 8048e27:	83 c3 01             	add    $0x1,%ebx
 8048e2a:	83 fb 05             	cmp    $0x5,%ebx
 8048e2d:	7e e9                	jle    8048e18 <phase_6+0x42>
 8048e2f:	eb cc                	jmp    8048dfd <phase_6+0x27>
 8048e31:	8b 52 08             	mov    0x8(%edx),%edx
 8048e34:	83 c0 01             	add    $0x1,%eax
 8048e37:	39 c8                	cmp    %ecx,%eax
 8048e39:	75 f6                	jne    8048e31 <phase_6+0x5b>
 8048e3b:	89 54 b4 24          	mov    %edx,0x24(%esp,%esi,4)
 8048e3f:	83 c3 01             	add    $0x1,%ebx
 8048e42:	83 fb 06             	cmp    $0x6,%ebx
 8048e45:	75 07                	jne    8048e4e <phase_6+0x78>
 8048e47:	eb 1c                	jmp    8048e65 <phase_6+0x8f>
 8048e49:	bb 00 00 00 00       	mov    $0x0,%ebx
 8048e4e:	89 de                	mov    %ebx,%esi
 8048e50:	8b 4c 9c 0c          	mov    0xc(%esp,%ebx,4),%ecx
 8048e54:	b8 01 00 00 00       	mov    $0x1,%eax
 8048e59:	ba 3c c1 04 08       	mov    $0x804c13c,%edx
 8048e5e:	83 f9 01             	cmp    $0x1,%ecx
 8048e61:	7f ce                	jg     8048e31 <phase_6+0x5b>
 8048e63:	eb d6                	jmp    8048e3b <phase_6+0x65>
 8048e65:	8b 5c 24 24          	mov    0x24(%esp),%ebx
 8048e69:	8d 44 24 24          	lea    0x24(%esp),%eax
 8048e6d:	8d 74 24 38          	lea    0x38(%esp),%esi
 8048e71:	89 d9                	mov    %ebx,%ecx
 8048e73:	8b 50 04             	mov    0x4(%eax),%edx
 8048e76:	89 51 08             	mov    %edx,0x8(%ecx)
 8048e79:	83 c0 04             	add    $0x4,%eax
 8048e7c:	89 d1                	mov    %edx,%ecx
 8048e7e:	39 f0                	cmp    %esi,%eax
 8048e80:	75 f1                	jne    8048e73 <phase_6+0x9d>
 8048e82:	c7 42 08 00 00 00 00 	movl   $0x0,0x8(%edx)
 8048e89:	be 05 00 00 00       	mov    $0x5,%esi
 8048e8e:	8b 43 08             	mov    0x8(%ebx),%eax
 8048e91:	8b 00                	mov    (%eax),%eax
 8048e93:	39 03                	cmp    %eax,(%ebx)
 8048e95:	7d 05                	jge    8048e9c <phase_6+0xc6>
 8048e97:	e8 5c 02 00 00       	call   80490f8 <explode_bomb>
 8048e9c:	8b 5b 08             	mov    0x8(%ebx),%ebx
 8048e9f:	83 ee 01             	sub    $0x1,%esi
 8048ea2:	75 ea                	jne    8048e8e <phase_6+0xb8>
 8048ea4:	8b 44 24 3c          	mov    0x3c(%esp),%eax
 8048ea8:	65 33 05 14 00 00 00 	xor    %gs:0x14,%eax
 8048eaf:	74 05                	je     8048eb6 <phase_6+0xe0>
 8048eb1:	e8 da f8 ff ff       	call   8048790 <__stack_chk_fail@plt>
 8048eb6:	83 c4 44             	add    $0x44,%esp
 8048eb9:	5b                   	pop    %ebx
 8048eba:	5e                   	pop    %esi
 8048ebb:	c3                   	ret    

08048ebc <fun7>:
 8048ebc:	53                   	push   %ebx
 8048ebd:	83 ec 08             	sub    $0x8,%esp
 8048ec0:	8b 54 24 10          	mov    0x10(%esp),%edx
 8048ec4:	8b 4c 24 14          	mov    0x14(%esp),%ecx
 8048ec8:	85 d2                	test   %edx,%edx
 8048eca:	74 37                	je     8048f03 <fun7+0x47>
 8048ecc:	8b 1a                	mov    (%edx),%ebx
 8048ece:	39 cb                	cmp    %ecx,%ebx
 8048ed0:	7e 13                	jle    8048ee5 <fun7+0x29>
 8048ed2:	83 ec 08             	sub    $0x8,%esp
 8048ed5:	51                   	push   %ecx
 8048ed6:	ff 72 04             	pushl  0x4(%edx)
 8048ed9:	e8 de ff ff ff       	call   8048ebc <fun7>
 8048ede:	83 c4 10             	add    $0x10,%esp
 8048ee1:	01 c0                	add    %eax,%eax
 8048ee3:	eb 23                	jmp    8048f08 <fun7+0x4c>
 8048ee5:	b8 00 00 00 00       	mov    $0x0,%eax
 8048eea:	39 cb                	cmp    %ecx,%ebx
 8048eec:	74 1a                	je     8048f08 <fun7+0x4c>
 8048eee:	83 ec 08             	sub    $0x8,%esp
 8048ef1:	51                   	push   %ecx
 8048ef2:	ff 72 08             	pushl  0x8(%edx)
 8048ef5:	e8 c2 ff ff ff       	call   8048ebc <fun7>
 8048efa:	83 c4 10             	add    $0x10,%esp
 8048efd:	8d 44 00 01          	lea    0x1(%eax,%eax,1),%eax
 8048f01:	eb 05                	jmp    8048f08 <fun7+0x4c>
 8048f03:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
 8048f08:	83 c4 08             	add    $0x8,%esp
 8048f0b:	5b                   	pop    %ebx
 8048f0c:	c3                   	ret    

08048f0d <secret_phase>:
 8048f0d:	53                   	push   %ebx
 8048f0e:	83 ec 08             	sub    $0x8,%esp
 8048f11:	e8 42 02 00 00       	call   8049158 <read_line>
 8048f16:	83 ec 04             	sub    $0x4,%esp
 8048f19:	6a 0a                	push   $0xa
 8048f1b:	6a 00                	push   $0x0
 8048f1d:	50                   	push   %eax
 8048f1e:	e8 5d f9 ff ff       	call   8048880 <strtol@plt>
 8048f23:	89 c3                	mov    %eax,%ebx
 8048f25:	8d 40 ff             	lea    -0x1(%eax),%eax
 8048f28:	83 c4 10             	add    $0x10,%esp
 8048f2b:	3d e8 03 00 00       	cmp    $0x3e8,%eax
 8048f30:	76 05                	jbe    8048f37 <secret_phase+0x2a>
 8048f32:	e8 c1 01 00 00       	call   80490f8 <explode_bomb>
 8048f37:	83 ec 08             	sub    $0x8,%esp
 8048f3a:	53                   	push   %ebx
 8048f3b:	68 88 c0 04 08       	push   $0x804c088
 8048f40:	e8 77 ff ff ff       	call   8048ebc <fun7>
 8048f45:	83 c4 10             	add    $0x10,%esp
 8048f48:	83 f8 07             	cmp    $0x7,%eax
 8048f4b:	74 05                	je     8048f52 <secret_phase+0x45>
 8048f4d:	e8 a6 01 00 00       	call   80490f8 <explode_bomb>
 8048f52:	83 ec 0c             	sub    $0xc,%esp
 8048f55:	68 30 a0 04 08       	push   $0x804a030
 8048f5a:	e8 61 f8 ff ff       	call   80487c0 <puts@plt>
 8048f5f:	e8 ed 02 00 00       	call   8049251 <phase_defused>
 8048f64:	83 c4 18             	add    $0x18,%esp
 8048f67:	5b                   	pop    %ebx
 8048f68:	c3                   	ret    

08048f69 <sig_handler>:
 8048f69:	83 ec 18             	sub    $0x18,%esp
 8048f6c:	68 90 a0 04 08       	push   $0x804a090
 8048f71:	e8 4a f8 ff ff       	call   80487c0 <puts@plt>
 8048f76:	c7 04 24 03 00 00 00 	movl   $0x3,(%esp)
 8048f7d:	e8 ee f7 ff ff       	call   8048770 <sleep@plt>
 8048f82:	83 c4 08             	add    $0x8,%esp
 8048f85:	68 52 a1 04 08       	push   $0x804a152
 8048f8a:	6a 01                	push   $0x1
 8048f8c:	e8 af f8 ff ff       	call   8048840 <__printf_chk@plt>
 8048f91:	83 c4 04             	add    $0x4,%esp
 8048f94:	ff 35 c4 c3 04 08    	pushl  0x804c3c4
 8048f9a:	e8 a1 f7 ff ff       	call   8048740 <fflush@plt>
 8048f9f:	c7 04 24 01 00 00 00 	movl   $0x1,(%esp)
 8048fa6:	e8 c5 f7 ff ff       	call   8048770 <sleep@plt>
 8048fab:	c7 04 24 5a a1 04 08 	movl   $0x804a15a,(%esp)
 8048fb2:	e8 09 f8 ff ff       	call   80487c0 <puts@plt>
 8048fb7:	c7 04 24 10 00 00 00 	movl   $0x10,(%esp)
 8048fbe:	e8 1d f8 ff ff       	call   80487e0 <exit@plt>

08048fc3 <invalid_phase>:
 8048fc3:	83 ec 10             	sub    $0x10,%esp
 8048fc6:	ff 74 24 14          	pushl  0x14(%esp)
 8048fca:	68 62 a1 04 08       	push   $0x804a162
 8048fcf:	6a 01                	push   $0x1
 8048fd1:	e8 6a f8 ff ff       	call   8048840 <__printf_chk@plt>
 8048fd6:	c7 04 24 08 00 00 00 	movl   $0x8,(%esp)
 8048fdd:	e8 fe f7 ff ff       	call   80487e0 <exit@plt>

08048fe2 <string_length>:
 8048fe2:	8b 54 24 04          	mov    0x4(%esp),%edx
 8048fe6:	80 3a 00             	cmpb   $0x0,(%edx)
 8048fe9:	74 10                	je     8048ffb <string_length+0x19>
 8048feb:	b8 00 00 00 00       	mov    $0x0,%eax
 8048ff0:	83 c0 01             	add    $0x1,%eax
 8048ff3:	80 3c 02 00          	cmpb   $0x0,(%edx,%eax,1)
 8048ff7:	75 f7                	jne    8048ff0 <string_length+0xe>
 8048ff9:	f3 c3                	repz ret 
 8048ffb:	b8 00 00 00 00       	mov    $0x0,%eax
 8049000:	c3                   	ret    

08049001 <strings_not_equal>:
 8049001:	57                   	push   %edi
 8049002:	56                   	push   %esi
 8049003:	53                   	push   %ebx
 8049004:	8b 5c 24 10          	mov    0x10(%esp),%ebx
 8049008:	8b 74 24 14          	mov    0x14(%esp),%esi
 804900c:	53                   	push   %ebx
 804900d:	e8 d0 ff ff ff       	call   8048fe2 <string_length>
 8049012:	89 c7                	mov    %eax,%edi
 8049014:	89 34 24             	mov    %esi,(%esp)
 8049017:	e8 c6 ff ff ff       	call   8048fe2 <string_length>
 804901c:	83 c4 04             	add    $0x4,%esp
 804901f:	ba 01 00 00 00       	mov    $0x1,%edx
 8049024:	39 c7                	cmp    %eax,%edi
 8049026:	75 38                	jne    8049060 <strings_not_equal+0x5f>
 8049028:	0f b6 03             	movzbl (%ebx),%eax
 804902b:	84 c0                	test   %al,%al
 804902d:	74 1e                	je     804904d <strings_not_equal+0x4c>
 804902f:	3a 06                	cmp    (%esi),%al
 8049031:	74 06                	je     8049039 <strings_not_equal+0x38>
 8049033:	eb 1f                	jmp    8049054 <strings_not_equal+0x53>
 8049035:	3a 06                	cmp    (%esi),%al
 8049037:	75 22                	jne    804905b <strings_not_equal+0x5a>
 8049039:	83 c3 01             	add    $0x1,%ebx
 804903c:	83 c6 01             	add    $0x1,%esi
 804903f:	0f b6 03             	movzbl (%ebx),%eax
 8049042:	84 c0                	test   %al,%al
 8049044:	75 ef                	jne    8049035 <strings_not_equal+0x34>
 8049046:	ba 00 00 00 00       	mov    $0x0,%edx
 804904b:	eb 13                	jmp    8049060 <strings_not_equal+0x5f>
 804904d:	ba 00 00 00 00       	mov    $0x0,%edx
 8049052:	eb 0c                	jmp    8049060 <strings_not_equal+0x5f>
 8049054:	ba 01 00 00 00       	mov    $0x1,%edx
 8049059:	eb 05                	jmp    8049060 <strings_not_equal+0x5f>
 804905b:	ba 01 00 00 00       	mov    $0x1,%edx
 8049060:	89 d0                	mov    %edx,%eax
 8049062:	5b                   	pop    %ebx
 8049063:	5e                   	pop    %esi
 8049064:	5f                   	pop    %edi
 8049065:	c3                   	ret    

08049066 <initialize_bomb>:
 8049066:	83 ec 14             	sub    $0x14,%esp
 8049069:	68 69 8f 04 08       	push   $0x8048f69
 804906e:	6a 02                	push   $0x2
 8049070:	e8 eb f6 ff ff       	call   8048760 <signal@plt>
 8049075:	83 c4 1c             	add    $0x1c,%esp
 8049078:	c3                   	ret    

08049079 <initialize_bomb_solve>:
 8049079:	f3 c3                	repz ret 

0804907b <blank_line>:
 804907b:	56                   	push   %esi
 804907c:	53                   	push   %ebx
 804907d:	83 ec 04             	sub    $0x4,%esp
 8049080:	8b 74 24 10          	mov    0x10(%esp),%esi
 8049084:	eb 14                	jmp    804909a <blank_line+0x1f>
 8049086:	e8 25 f8 ff ff       	call   80488b0 <__ctype_b_loc@plt>
 804908b:	83 c6 01             	add    $0x1,%esi
 804908e:	0f be db             	movsbl %bl,%ebx
 8049091:	8b 00                	mov    (%eax),%eax
 8049093:	f6 44 58 01 20       	testb  $0x20,0x1(%eax,%ebx,2)
 8049098:	74 0e                	je     80490a8 <blank_line+0x2d>
 804909a:	0f b6 1e             	movzbl (%esi),%ebx
 804909d:	84 db                	test   %bl,%bl
 804909f:	75 e5                	jne    8049086 <blank_line+0xb>
 80490a1:	b8 01 00 00 00       	mov    $0x1,%eax
 80490a6:	eb 05                	jmp    80490ad <blank_line+0x32>
 80490a8:	b8 00 00 00 00       	mov    $0x0,%eax
 80490ad:	83 c4 04             	add    $0x4,%esp
 80490b0:	5b                   	pop    %ebx
 80490b1:	5e                   	pop    %esi
 80490b2:	c3                   	ret    

080490b3 <skip>:
 80490b3:	53                   	push   %ebx
 80490b4:	83 ec 08             	sub    $0x8,%esp
 80490b7:	83 ec 04             	sub    $0x4,%esp
 80490ba:	ff 35 d0 c3 04 08    	pushl  0x804c3d0
 80490c0:	6a 50                	push   $0x50
 80490c2:	a1 cc c3 04 08       	mov    0x804c3cc,%eax
 80490c7:	8d 04 80             	lea    (%eax,%eax,4),%eax
 80490ca:	c1 e0 04             	shl    $0x4,%eax
 80490cd:	05 e0 c3 04 08       	add    $0x804c3e0,%eax
 80490d2:	50                   	push   %eax
 80490d3:	e8 78 f6 ff ff       	call   8048750 <fgets@plt>
 80490d8:	89 c3                	mov    %eax,%ebx
 80490da:	83 c4 10             	add    $0x10,%esp
 80490dd:	85 c0                	test   %eax,%eax
 80490df:	74 10                	je     80490f1 <skip+0x3e>
 80490e1:	83 ec 0c             	sub    $0xc,%esp
 80490e4:	50                   	push   %eax
 80490e5:	e8 91 ff ff ff       	call   804907b <blank_line>
 80490ea:	83 c4 10             	add    $0x10,%esp
 80490ed:	85 c0                	test   %eax,%eax
 80490ef:	75 c6                	jne    80490b7 <skip+0x4>
 80490f1:	89 d8                	mov    %ebx,%eax
 80490f3:	83 c4 08             	add    $0x8,%esp
 80490f6:	5b                   	pop    %ebx
 80490f7:	c3                   	ret    

080490f8 <explode_bomb>:
 80490f8:	83 ec 18             	sub    $0x18,%esp
 80490fb:	68 73 a1 04 08       	push   $0x804a173
 8049100:	e8 bb f6 ff ff       	call   80487c0 <puts@plt>
 8049105:	c7 04 24 7c a1 04 08 	movl   $0x804a17c,(%esp)
 804910c:	e8 af f6 ff ff       	call   80487c0 <puts@plt>
 8049111:	c7 04 24 08 00 00 00 	movl   $0x8,(%esp)
 8049118:	e8 c3 f6 ff ff       	call   80487e0 <exit@plt>

0804911d <read_six_numbers>:
 804911d:	83 ec 0c             	sub    $0xc,%esp
 8049120:	8b 44 24 14          	mov    0x14(%esp),%eax
 8049124:	8d 50 14             	lea    0x14(%eax),%edx
 8049127:	52                   	push   %edx
 8049128:	8d 50 10             	lea    0x10(%eax),%edx
 804912b:	52                   	push   %edx
 804912c:	8d 50 0c             	lea    0xc(%eax),%edx
 804912f:	52                   	push   %edx
 8049130:	8d 50 08             	lea    0x8(%eax),%edx
 8049133:	52                   	push   %edx
 8049134:	8d 50 04             	lea    0x4(%eax),%edx
 8049137:	52                   	push   %edx
 8049138:	50                   	push   %eax
 8049139:	68 93 a1 04 08       	push   $0x804a193
 804913e:	ff 74 24 2c          	pushl  0x2c(%esp)
 8049142:	e8 c9 f6 ff ff       	call   8048810 <__isoc99_sscanf@plt>
 8049147:	83 c4 20             	add    $0x20,%esp
 804914a:	83 f8 05             	cmp    $0x5,%eax
 804914d:	7f 05                	jg     8049154 <read_six_numbers+0x37>
 804914f:	e8 a4 ff ff ff       	call   80490f8 <explode_bomb>
 8049154:	83 c4 0c             	add    $0xc,%esp
 8049157:	c3                   	ret    

08049158 <read_line>:
 8049158:	57                   	push   %edi
 8049159:	56                   	push   %esi
 804915a:	53                   	push   %ebx
 804915b:	e8 53 ff ff ff       	call   80490b3 <skip>
 8049160:	85 c0                	test   %eax,%eax
 8049162:	75 70                	jne    80491d4 <read_line+0x7c>
 8049164:	a1 c0 c3 04 08       	mov    0x804c3c0,%eax
 8049169:	39 05 d0 c3 04 08    	cmp    %eax,0x804c3d0
 804916f:	75 19                	jne    804918a <read_line+0x32>
 8049171:	83 ec 0c             	sub    $0xc,%esp
 8049174:	68 a5 a1 04 08       	push   $0x804a1a5
 8049179:	e8 42 f6 ff ff       	call   80487c0 <puts@plt>
 804917e:	c7 04 24 08 00 00 00 	movl   $0x8,(%esp)
 8049185:	e8 56 f6 ff ff       	call   80487e0 <exit@plt>
 804918a:	83 ec 0c             	sub    $0xc,%esp
 804918d:	68 c3 a1 04 08       	push   $0x804a1c3
 8049192:	e8 19 f6 ff ff       	call   80487b0 <getenv@plt>
 8049197:	83 c4 10             	add    $0x10,%esp
 804919a:	85 c0                	test   %eax,%eax
 804919c:	74 0a                	je     80491a8 <read_line+0x50>
 804919e:	83 ec 0c             	sub    $0xc,%esp
 80491a1:	6a 00                	push   $0x0
 80491a3:	e8 38 f6 ff ff       	call   80487e0 <exit@plt>
 80491a8:	a1 c0 c3 04 08       	mov    0x804c3c0,%eax
 80491ad:	a3 d0 c3 04 08       	mov    %eax,0x804c3d0
 80491b2:	e8 fc fe ff ff       	call   80490b3 <skip>
 80491b7:	85 c0                	test   %eax,%eax
 80491b9:	75 19                	jne    80491d4 <read_line+0x7c>
 80491bb:	83 ec 0c             	sub    $0xc,%esp
 80491be:	68 a5 a1 04 08       	push   $0x804a1a5
 80491c3:	e8 f8 f5 ff ff       	call   80487c0 <puts@plt>
 80491c8:	c7 04 24 00 00 00 00 	movl   $0x0,(%esp)
 80491cf:	e8 0c f6 ff ff       	call   80487e0 <exit@plt>
 80491d4:	8b 15 cc c3 04 08    	mov    0x804c3cc,%edx
 80491da:	8d 1c 92             	lea    (%edx,%edx,4),%ebx
 80491dd:	c1 e3 04             	shl    $0x4,%ebx
 80491e0:	81 c3 e0 c3 04 08    	add    $0x804c3e0,%ebx
 80491e6:	b8 00 00 00 00       	mov    $0x0,%eax
 80491eb:	b9 ff ff ff ff       	mov    $0xffffffff,%ecx
 80491f0:	89 df                	mov    %ebx,%edi
 80491f2:	f2 ae                	repnz scas %es:(%edi),%al
 80491f4:	f7 d1                	not    %ecx
 80491f6:	83 e9 01             	sub    $0x1,%ecx
 80491f9:	83 f9 4e             	cmp    $0x4e,%ecx
 80491fc:	7e 36                	jle    8049234 <read_line+0xdc>
 80491fe:	83 ec 0c             	sub    $0xc,%esp
 8049201:	68 ce a1 04 08       	push   $0x804a1ce
 8049206:	e8 b5 f5 ff ff       	call   80487c0 <puts@plt>
 804920b:	a1 cc c3 04 08       	mov    0x804c3cc,%eax
 8049210:	8d 50 01             	lea    0x1(%eax),%edx
 8049213:	89 15 cc c3 04 08    	mov    %edx,0x804c3cc
 8049219:	6b c0 50             	imul   $0x50,%eax,%eax
 804921c:	05 e0 c3 04 08       	add    $0x804c3e0,%eax
 8049221:	be e9 a1 04 08       	mov    $0x804a1e9,%esi
 8049226:	b9 04 00 00 00       	mov    $0x4,%ecx
 804922b:	89 c7                	mov    %eax,%edi
 804922d:	f3 a5                	rep movsl %ds:(%esi),%es:(%edi)
 804922f:	e8 c4 fe ff ff       	call   80490f8 <explode_bomb>
 8049234:	8d 04 92             	lea    (%edx,%edx,4),%eax
 8049237:	c1 e0 04             	shl    $0x4,%eax
 804923a:	c6 84 01 df c3 04 08 	movb   $0x0,0x804c3df(%ecx,%eax,1)
 8049241:	00 
 8049242:	83 c2 01             	add    $0x1,%edx
 8049245:	89 15 cc c3 04 08    	mov    %edx,0x804c3cc
 804924b:	89 d8                	mov    %ebx,%eax
 804924d:	5b                   	pop    %ebx
 804924e:	5e                   	pop    %esi
 804924f:	5f                   	pop    %edi
 8049250:	c3                   	ret    

08049251 <phase_defused>:
 8049251:	83 ec 6c             	sub    $0x6c,%esp
 8049254:	65 a1 14 00 00 00    	mov    %gs:0x14,%eax
 804925a:	89 44 24 5c          	mov    %eax,0x5c(%esp)
 804925e:	31 c0                	xor    %eax,%eax
 8049260:	83 3d cc c3 04 08 06 	cmpl   $0x6,0x804c3cc
 8049267:	75 73                	jne    80492dc <phase_defused+0x8b>
 8049269:	83 ec 0c             	sub    $0xc,%esp
 804926c:	8d 44 24 18          	lea    0x18(%esp),%eax
 8049270:	50                   	push   %eax
 8049271:	8d 44 24 18          	lea    0x18(%esp),%eax
 8049275:	50                   	push   %eax
 8049276:	8d 44 24 18          	lea    0x18(%esp),%eax
 804927a:	50                   	push   %eax
 804927b:	68 f9 a1 04 08       	push   $0x804a1f9	; "%d %d %s"
 8049280:	68 d0 c4 04 08       	push   $0x804c4d0	; "0 0"
 8049285:	e8 86 f5 ff ff       	call   8048810 <__isoc99_sscanf@plt>
 804928a:	83 c4 20             	add    $0x20,%esp
 804928d:	83 f8 03             	cmp    $0x3,%eax
 8049290:	75 3a                	jne    80492cc <phase_defused+0x7b>
 8049292:	83 ec 08             	sub    $0x8,%esp
 8049295:	68 02 a2 04 08       	push   $0x804a202	; "DrEvil"
 804929a:	8d 44 24 18          	lea    0x18(%esp),%eax
 804929e:	50                   	push   %eax
 804929f:	e8 5d fd ff ff       	call   8049001 <strings_not_equal>
 80492a4:	83 c4 10             	add    $0x10,%esp
 80492a7:	85 c0                	test   %eax,%eax
 80492a9:	75 21                	jne    80492cc <phase_defused+0x7b>
 80492ab:	83 ec 0c             	sub    $0xc,%esp
 80492ae:	68 c8 a0 04 08       	push   $0x804a0c8	; "Curses, you've found the secret phase!"
 80492b3:	e8 08 f5 ff ff       	call   80487c0 <puts@plt>
 80492b8:	c7 04 24 f0 a0 04 08 	movl   $0x804a0f0,(%esp)	; "But finding it and solving it are quite different..."
 80492bf:	e8 fc f4 ff ff       	call   80487c0 <puts@plt>
 80492c4:	e8 44 fc ff ff       	call   8048f0d <secret_phase>
 80492c9:	83 c4 10             	add    $0x10,%esp
 80492cc:	83 ec 0c             	sub    $0xc,%esp
 80492cf:	68 28 a1 04 08       	push   $0x804a128	; "Congratulations! You've defused the bomb!"
 80492d4:	e8 e7 f4 ff ff       	call   80487c0 <puts@plt>
 80492d9:	83 c4 10             	add    $0x10,%esp
 80492dc:	8b 44 24 5c          	mov    0x5c(%esp),%eax
 80492e0:	65 33 05 14 00 00 00 	xor    %gs:0x14,%eax
 80492e7:	74 05                	je     80492ee <phase_defused+0x9d>
 80492e9:	e8 a2 f4 ff ff       	call   8048790 <__stack_chk_fail@plt>
 80492ee:	83 c4 6c             	add    $0x6c,%esp
 80492f1:	c3                   	ret    

080492f2 <sigalrm_handler>:
 80492f2:	83 ec 0c             	sub    $0xc,%esp
 80492f5:	6a 00                	push   $0x0
 80492f7:	68 58 a2 04 08       	push   $0x804a258
 80492fc:	6a 01                	push   $0x1
 80492fe:	ff 35 a0 c3 04 08    	pushl  0x804c3a0
 8049304:	e8 57 f5 ff ff       	call   8048860 <__fprintf_chk@plt>
 8049309:	c7 04 24 01 00 00 00 	movl   $0x1,(%esp)
 8049310:	e8 cb f4 ff ff       	call   80487e0 <exit@plt>

08049315 <rio_readlineb>:
 8049315:	55                   	push   %ebp
 8049316:	57                   	push   %edi
 8049317:	56                   	push   %esi
 8049318:	53                   	push   %ebx
 8049319:	83 ec 2c             	sub    $0x2c,%esp
 804931c:	89 d7                	mov    %edx,%edi
 804931e:	89 4c 24 0c          	mov    %ecx,0xc(%esp)
 8049322:	65 8b 15 14 00 00 00 	mov    %gs:0x14,%edx
 8049329:	89 54 24 1c          	mov    %edx,0x1c(%esp)
 804932d:	31 d2                	xor    %edx,%edx
 804932f:	83 f9 01             	cmp    $0x1,%ecx
 8049332:	76 79                	jbe    80493ad <rio_readlineb+0x98>
 8049334:	89 c3                	mov    %eax,%ebx
 8049336:	89 4c 24 08          	mov    %ecx,0x8(%esp)
 804933a:	bd 01 00 00 00       	mov    $0x1,%ebp
 804933f:	8d 73 0c             	lea    0xc(%ebx),%esi
 8049342:	eb 2d                	jmp    8049371 <rio_readlineb+0x5c>
 8049344:	83 ec 04             	sub    $0x4,%esp
 8049347:	68 00 20 00 00       	push   $0x2000
 804934c:	56                   	push   %esi
 804934d:	ff 33                	pushl  (%ebx)
 804934f:	e8 dc f3 ff ff       	call   8048730 <read@plt>
 8049354:	89 43 04             	mov    %eax,0x4(%ebx)
 8049357:	83 c4 10             	add    $0x10,%esp
 804935a:	85 c0                	test   %eax,%eax
 804935c:	79 0c                	jns    804936a <rio_readlineb+0x55>
 804935e:	e8 cd f4 ff ff       	call   8048830 <__errno_location@plt>
 8049363:	83 38 04             	cmpl   $0x4,(%eax)
 8049366:	74 09                	je     8049371 <rio_readlineb+0x5c>
 8049368:	eb 62                	jmp    80493cc <rio_readlineb+0xb7>
 804936a:	85 c0                	test   %eax,%eax
 804936c:	74 63                	je     80493d1 <rio_readlineb+0xbc>
 804936e:	89 73 08             	mov    %esi,0x8(%ebx)
 8049371:	8b 43 04             	mov    0x4(%ebx),%eax
 8049374:	85 c0                	test   %eax,%eax
 8049376:	7e cc                	jle    8049344 <rio_readlineb+0x2f>
 8049378:	8b 4b 08             	mov    0x8(%ebx),%ecx
 804937b:	0f b6 11             	movzbl (%ecx),%edx
 804937e:	88 54 24 1b          	mov    %dl,0x1b(%esp)
 8049382:	83 c1 01             	add    $0x1,%ecx
 8049385:	89 4b 08             	mov    %ecx,0x8(%ebx)
 8049388:	83 e8 01             	sub    $0x1,%eax
 804938b:	89 43 04             	mov    %eax,0x4(%ebx)
 804938e:	83 c7 01             	add    $0x1,%edi
 8049391:	88 57 ff             	mov    %dl,-0x1(%edi)
 8049394:	80 fa 0a             	cmp    $0xa,%dl
 8049397:	75 09                	jne    80493a2 <rio_readlineb+0x8d>
 8049399:	eb 1d                	jmp    80493b8 <rio_readlineb+0xa3>
 804939b:	83 fd 01             	cmp    $0x1,%ebp
 804939e:	75 18                	jne    80493b8 <rio_readlineb+0xa3>
 80493a0:	eb 1b                	jmp    80493bd <rio_readlineb+0xa8>
 80493a2:	83 c5 01             	add    $0x1,%ebp
 80493a5:	3b 6c 24 08          	cmp    0x8(%esp),%ebp
 80493a9:	74 09                	je     80493b4 <rio_readlineb+0x9f>
 80493ab:	eb c4                	jmp    8049371 <rio_readlineb+0x5c>
 80493ad:	bd 01 00 00 00       	mov    $0x1,%ebp
 80493b2:	eb 04                	jmp    80493b8 <rio_readlineb+0xa3>
 80493b4:	8b 6c 24 0c          	mov    0xc(%esp),%ebp
 80493b8:	c6 07 00             	movb   $0x0,(%edi)
 80493bb:	89 e8                	mov    %ebp,%eax
 80493bd:	8b 54 24 1c          	mov    0x1c(%esp),%edx
 80493c1:	65 33 15 14 00 00 00 	xor    %gs:0x14,%edx
 80493c8:	74 17                	je     80493e1 <rio_readlineb+0xcc>
 80493ca:	eb 10                	jmp    80493dc <rio_readlineb+0xc7>
 80493cc:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
 80493d1:	85 c0                	test   %eax,%eax
 80493d3:	74 c6                	je     804939b <rio_readlineb+0x86>
 80493d5:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
 80493da:	eb e1                	jmp    80493bd <rio_readlineb+0xa8>
 80493dc:	e8 af f3 ff ff       	call   8048790 <__stack_chk_fail@plt>
 80493e1:	83 c4 2c             	add    $0x2c,%esp
 80493e4:	5b                   	pop    %ebx
 80493e5:	5e                   	pop    %esi
 80493e6:	5f                   	pop    %edi
 80493e7:	5d                   	pop    %ebp
 80493e8:	c3                   	ret    

080493e9 <submitr>:
 80493e9:	55                   	push   %ebp
 80493ea:	57                   	push   %edi
 80493eb:	56                   	push   %esi
 80493ec:	53                   	push   %ebx
 80493ed:	81 ec 60 a0 00 00    	sub    $0xa060,%esp
 80493f3:	8b b4 24 74 a0 00 00 	mov    0xa074(%esp),%esi
 80493fa:	8b 84 24 7c a0 00 00 	mov    0xa07c(%esp),%eax
 8049401:	89 44 24 10          	mov    %eax,0x10(%esp)
 8049405:	8b 84 24 80 a0 00 00 	mov    0xa080(%esp),%eax
 804940c:	89 44 24 14          	mov    %eax,0x14(%esp)
 8049410:	8b 84 24 84 a0 00 00 	mov    0xa084(%esp),%eax
 8049417:	89 44 24 18          	mov    %eax,0x18(%esp)
 804941b:	8b 9c 24 88 a0 00 00 	mov    0xa088(%esp),%ebx
 8049422:	8b 84 24 8c a0 00 00 	mov    0xa08c(%esp),%eax
 8049429:	89 44 24 1c          	mov    %eax,0x1c(%esp)
 804942d:	65 a1 14 00 00 00    	mov    %gs:0x14,%eax
 8049433:	89 84 24 50 a0 00 00 	mov    %eax,0xa050(%esp)
 804943a:	31 c0                	xor    %eax,%eax
 804943c:	c7 44 24 30 00 00 00 	movl   $0x0,0x30(%esp)
 8049443:	00 
 8049444:	6a 00                	push   $0x0
 8049446:	6a 01                	push   $0x1
 8049448:	6a 02                	push   $0x2
 804944a:	e8 01 f4 ff ff       	call   8048850 <socket@plt>
 804944f:	89 44 24 18          	mov    %eax,0x18(%esp)
 8049453:	83 c4 10             	add    $0x10,%esp
 8049456:	85 c0                	test   %eax,%eax
 8049458:	79 52                	jns    80494ac <submitr+0xc3>
 804945a:	8b 44 24 18          	mov    0x18(%esp),%eax
 804945e:	c7 00 45 72 72 6f    	movl   $0x6f727245,(%eax)
 8049464:	c7 40 04 72 3a 20 43 	movl   $0x43203a72,0x4(%eax)
 804946b:	c7 40 08 6c 69 65 6e 	movl   $0x6e65696c,0x8(%eax)
 8049472:	c7 40 0c 74 20 75 6e 	movl   $0x6e752074,0xc(%eax)
 8049479:	c7 40 10 61 62 6c 65 	movl   $0x656c6261,0x10(%eax)
 8049480:	c7 40 14 20 74 6f 20 	movl   $0x206f7420,0x14(%eax)
 8049487:	c7 40 18 63 72 65 61 	movl   $0x61657263,0x18(%eax)
 804948e:	c7 40 1c 74 65 20 73 	movl   $0x73206574,0x1c(%eax)
 8049495:	c7 40 20 6f 63 6b 65 	movl   $0x656b636f,0x20(%eax)
 804949c:	66 c7 40 24 74 00    	movw   $0x74,0x24(%eax)
 80494a2:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
 80494a7:	e9 3f 06 00 00       	jmp    8049aeb <submitr+0x702>
 80494ac:	83 ec 0c             	sub    $0xc,%esp
 80494af:	56                   	push   %esi
 80494b0:	e8 bb f3 ff ff       	call   8048870 <gethostbyname@plt>
 80494b5:	83 c4 10             	add    $0x10,%esp
 80494b8:	85 c0                	test   %eax,%eax
 80494ba:	75 73                	jne    804952f <submitr+0x146>
 80494bc:	8b 44 24 18          	mov    0x18(%esp),%eax
 80494c0:	c7 00 45 72 72 6f    	movl   $0x6f727245,(%eax)
 80494c6:	c7 40 04 72 3a 20 44 	movl   $0x44203a72,0x4(%eax)
 80494cd:	c7 40 08 4e 53 20 69 	movl   $0x6920534e,0x8(%eax)
 80494d4:	c7 40 0c 73 20 75 6e 	movl   $0x6e752073,0xc(%eax)
 80494db:	c7 40 10 61 62 6c 65 	movl   $0x656c6261,0x10(%eax)
 80494e2:	c7 40 14 20 74 6f 20 	movl   $0x206f7420,0x14(%eax)
 80494e9:	c7 40 18 72 65 73 6f 	movl   $0x6f736572,0x18(%eax)
 80494f0:	c7 40 1c 6c 76 65 20 	movl   $0x2065766c,0x1c(%eax)
 80494f7:	c7 40 20 73 65 72 76 	movl   $0x76726573,0x20(%eax)
 80494fe:	c7 40 24 65 72 20 61 	movl   $0x61207265,0x24(%eax)
 8049505:	c7 40 28 64 64 72 65 	movl   $0x65726464,0x28(%eax)
 804950c:	66 c7 40 2c 73 73    	movw   $0x7373,0x2c(%eax)
 8049512:	c6 40 2e 00          	movb   $0x0,0x2e(%eax)
 8049516:	83 ec 0c             	sub    $0xc,%esp
 8049519:	ff 74 24 14          	pushl  0x14(%esp)
 804951d:	e8 7e f3 ff ff       	call   80488a0 <close@plt>
 8049522:	83 c4 10             	add    $0x10,%esp
 8049525:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
 804952a:	e9 bc 05 00 00       	jmp    8049aeb <submitr+0x702>
 804952f:	8d 74 24 30          	lea    0x30(%esp),%esi
 8049533:	c7 44 24 30 00 00 00 	movl   $0x0,0x30(%esp)
 804953a:	00 
 804953b:	c7 44 24 34 00 00 00 	movl   $0x0,0x34(%esp)
 8049542:	00 
 8049543:	c7 44 24 38 00 00 00 	movl   $0x0,0x38(%esp)
 804954a:	00 
 804954b:	c7 44 24 3c 00 00 00 	movl   $0x0,0x3c(%esp)
 8049552:	00 
 8049553:	66 c7 44 24 30 02 00 	movw   $0x2,0x30(%esp)
 804955a:	6a 0c                	push   $0xc
 804955c:	ff 70 0c             	pushl  0xc(%eax)
 804955f:	8b 40 10             	mov    0x10(%eax),%eax
 8049562:	ff 30                	pushl  (%eax)
 8049564:	8d 44 24 40          	lea    0x40(%esp),%eax
 8049568:	50                   	push   %eax
 8049569:	e8 62 f2 ff ff       	call   80487d0 <__memmove_chk@plt>
 804956e:	0f b7 84 24 84 a0 00 	movzwl 0xa084(%esp),%eax
 8049575:	00 
 8049576:	66 c1 c8 08          	ror    $0x8,%ax
 804957a:	66 89 44 24 42       	mov    %ax,0x42(%esp)
 804957f:	83 c4 0c             	add    $0xc,%esp
 8049582:	6a 10                	push   $0x10
 8049584:	56                   	push   %esi
 8049585:	ff 74 24 14          	pushl  0x14(%esp)
 8049589:	e8 02 f3 ff ff       	call   8048890 <connect@plt>
 804958e:	83 c4 10             	add    $0x10,%esp
 8049591:	85 c0                	test   %eax,%eax
 8049593:	79 65                	jns    80495fa <submitr+0x211>
 8049595:	8b 44 24 18          	mov    0x18(%esp),%eax
 8049599:	c7 00 45 72 72 6f    	movl   $0x6f727245,(%eax)
 804959f:	c7 40 04 72 3a 20 55 	movl   $0x55203a72,0x4(%eax)
 80495a6:	c7 40 08 6e 61 62 6c 	movl   $0x6c62616e,0x8(%eax)
 80495ad:	c7 40 0c 65 20 74 6f 	movl   $0x6f742065,0xc(%eax)
 80495b4:	c7 40 10 20 63 6f 6e 	movl   $0x6e6f6320,0x10(%eax)
 80495bb:	c7 40 14 6e 65 63 74 	movl   $0x7463656e,0x14(%eax)
 80495c2:	c7 40 18 20 74 6f 20 	movl   $0x206f7420,0x18(%eax)
 80495c9:	c7 40 1c 74 68 65 20 	movl   $0x20656874,0x1c(%eax)
 80495d0:	c7 40 20 73 65 72 76 	movl   $0x76726573,0x20(%eax)
 80495d7:	66 c7 40 24 65 72    	movw   $0x7265,0x24(%eax)
 80495dd:	c6 40 26 00          	movb   $0x0,0x26(%eax)
 80495e1:	83 ec 0c             	sub    $0xc,%esp
 80495e4:	ff 74 24 14          	pushl  0x14(%esp)
 80495e8:	e8 b3 f2 ff ff       	call   80488a0 <close@plt>
 80495ed:	83 c4 10             	add    $0x10,%esp
 80495f0:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
 80495f5:	e9 f1 04 00 00       	jmp    8049aeb <submitr+0x702>
 80495fa:	be ff ff ff ff       	mov    $0xffffffff,%esi
 80495ff:	b8 00 00 00 00       	mov    $0x0,%eax
 8049604:	89 f1                	mov    %esi,%ecx
 8049606:	89 df                	mov    %ebx,%edi
 8049608:	f2 ae                	repnz scas %es:(%edi),%al
 804960a:	f7 d1                	not    %ecx
 804960c:	89 cd                	mov    %ecx,%ebp
 804960e:	89 f1                	mov    %esi,%ecx
 8049610:	8b 7c 24 0c          	mov    0xc(%esp),%edi
 8049614:	f2 ae                	repnz scas %es:(%edi),%al
 8049616:	89 4c 24 1c          	mov    %ecx,0x1c(%esp)
 804961a:	89 f1                	mov    %esi,%ecx
 804961c:	8b 7c 24 10          	mov    0x10(%esp),%edi
 8049620:	f2 ae                	repnz scas %es:(%edi),%al
 8049622:	89 ca                	mov    %ecx,%edx
 8049624:	f7 d2                	not    %edx
 8049626:	89 f1                	mov    %esi,%ecx
 8049628:	8b 7c 24 14          	mov    0x14(%esp),%edi
 804962c:	f2 ae                	repnz scas %es:(%edi),%al
 804962e:	2b 54 24 1c          	sub    0x1c(%esp),%edx
 8049632:	29 ca                	sub    %ecx,%edx
 8049634:	8d 44 6d fd          	lea    -0x3(%ebp,%ebp,2),%eax
 8049638:	8d 44 02 7b          	lea    0x7b(%edx,%eax,1),%eax
 804963c:	3d 00 20 00 00       	cmp    $0x2000,%eax
 8049641:	76 7e                	jbe    80496c1 <submitr+0x2d8>
 8049643:	8b 44 24 18          	mov    0x18(%esp),%eax
 8049647:	c7 00 45 72 72 6f    	movl   $0x6f727245,(%eax)
 804964d:	c7 40 04 72 3a 20 52 	movl   $0x52203a72,0x4(%eax)
 8049654:	c7 40 08 65 73 75 6c 	movl   $0x6c757365,0x8(%eax)
 804965b:	c7 40 0c 74 20 73 74 	movl   $0x74732074,0xc(%eax)
 8049662:	c7 40 10 72 69 6e 67 	movl   $0x676e6972,0x10(%eax)
 8049669:	c7 40 14 20 74 6f 6f 	movl   $0x6f6f7420,0x14(%eax)
 8049670:	c7 40 18 20 6c 61 72 	movl   $0x72616c20,0x18(%eax)
 8049677:	c7 40 1c 67 65 2e 20 	movl   $0x202e6567,0x1c(%eax)
 804967e:	c7 40 20 49 6e 63 72 	movl   $0x72636e49,0x20(%eax)
 8049685:	c7 40 24 65 61 73 65 	movl   $0x65736165,0x24(%eax)
 804968c:	c7 40 28 20 53 55 42 	movl   $0x42555320,0x28(%eax)
 8049693:	c7 40 2c 4d 49 54 52 	movl   $0x5254494d,0x2c(%eax)
 804969a:	c7 40 30 5f 4d 41 58 	movl   $0x58414d5f,0x30(%eax)
 80496a1:	c7 40 34 42 55 46 00 	movl   $0x465542,0x34(%eax)
 80496a8:	83 ec 0c             	sub    $0xc,%esp
 80496ab:	ff 74 24 14          	pushl  0x14(%esp)
 80496af:	e8 ec f1 ff ff       	call   80488a0 <close@plt>
 80496b4:	83 c4 10             	add    $0x10,%esp
 80496b7:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
 80496bc:	e9 2a 04 00 00       	jmp    8049aeb <submitr+0x702>
 80496c1:	8d 94 24 4c 40 00 00 	lea    0x404c(%esp),%edx
 80496c8:	b9 00 08 00 00       	mov    $0x800,%ecx
 80496cd:	b8 00 00 00 00       	mov    $0x0,%eax
 80496d2:	89 d7                	mov    %edx,%edi
 80496d4:	f3 ab                	rep stos %eax,%es:(%edi)
 80496d6:	b9 ff ff ff ff       	mov    $0xffffffff,%ecx
 80496db:	89 df                	mov    %ebx,%edi
 80496dd:	f2 ae                	repnz scas %es:(%edi),%al
 80496df:	f7 d1                	not    %ecx
 80496e1:	89 ce                	mov    %ecx,%esi
 80496e3:	83 ee 01             	sub    $0x1,%esi
 80496e6:	0f 84 5c 04 00 00    	je     8049b48 <submitr+0x75f>
 80496ec:	89 d5                	mov    %edx,%ebp
 80496ee:	bf d9 ff 00 00       	mov    $0xffd9,%edi
 80496f3:	0f b6 13             	movzbl (%ebx),%edx
 80496f6:	8d 4a d6             	lea    -0x2a(%edx),%ecx
 80496f9:	b8 01 00 00 00       	mov    $0x1,%eax
 80496fe:	80 f9 0f             	cmp    $0xf,%cl
 8049701:	77 0a                	ja     804970d <submitr+0x324>
 8049703:	89 f8                	mov    %edi,%eax
 8049705:	d3 e8                	shr    %cl,%eax
 8049707:	83 f0 01             	xor    $0x1,%eax
 804970a:	83 e0 01             	and    $0x1,%eax
 804970d:	80 fa 5f             	cmp    $0x5f,%dl
 8049710:	0f 94 c1             	sete   %cl
 8049713:	38 c1                	cmp    %al,%cl
 8049715:	73 0c                	jae    8049723 <submitr+0x33a>
 8049717:	89 d0                	mov    %edx,%eax
 8049719:	83 e0 df             	and    $0xffffffdf,%eax
 804971c:	83 e8 41             	sub    $0x41,%eax
 804971f:	3c 19                	cmp    $0x19,%al
 8049721:	77 08                	ja     804972b <submitr+0x342>
 8049723:	88 55 00             	mov    %dl,0x0(%ebp)
 8049726:	8d 6d 01             	lea    0x1(%ebp),%ebp
 8049729:	eb 62                	jmp    804978d <submitr+0x3a4>
 804972b:	80 fa 20             	cmp    $0x20,%dl
 804972e:	75 09                	jne    8049739 <submitr+0x350>
 8049730:	c6 45 00 2b          	movb   $0x2b,0x0(%ebp)
 8049734:	8d 6d 01             	lea    0x1(%ebp),%ebp
 8049737:	eb 54                	jmp    804978d <submitr+0x3a4>
 8049739:	8d 42 e0             	lea    -0x20(%edx),%eax
 804973c:	3c 5f                	cmp    $0x5f,%al
 804973e:	76 09                	jbe    8049749 <submitr+0x360>
 8049740:	80 fa 09             	cmp    $0x9,%dl
 8049743:	0f 85 bb 03 00 00    	jne    8049b04 <submitr+0x71b>
 8049749:	83 ec 0c             	sub    $0xc,%esp
 804974c:	0f b6 d2             	movzbl %dl,%edx
 804974f:	52                   	push   %edx
 8049750:	68 64 a3 04 08       	push   $0x804a364
 8049755:	6a 08                	push   $0x8
 8049757:	6a 01                	push   $0x1
 8049759:	8d 84 24 68 80 00 00 	lea    0x8068(%esp),%eax
 8049760:	50                   	push   %eax
 8049761:	e8 5a f1 ff ff       	call   80488c0 <__sprintf_chk@plt>
 8049766:	0f b6 84 24 6c 80 00 	movzbl 0x806c(%esp),%eax
 804976d:	00 
 804976e:	88 45 00             	mov    %al,0x0(%ebp)
 8049771:	0f b6 84 24 6d 80 00 	movzbl 0x806d(%esp),%eax
 8049778:	00 
 8049779:	88 45 01             	mov    %al,0x1(%ebp)
 804977c:	0f b6 84 24 6e 80 00 	movzbl 0x806e(%esp),%eax
 8049783:	00 
 8049784:	88 45 02             	mov    %al,0x2(%ebp)
 8049787:	83 c4 20             	add    $0x20,%esp
 804978a:	8d 6d 03             	lea    0x3(%ebp),%ebp
 804978d:	83 c3 01             	add    $0x1,%ebx
 8049790:	83 ee 01             	sub    $0x1,%esi
 8049793:	0f 85 5a ff ff ff    	jne    80496f3 <submitr+0x30a>
 8049799:	e9 aa 03 00 00       	jmp    8049b48 <submitr+0x75f>
 804979e:	83 ec 04             	sub    $0x4,%esp
 80497a1:	53                   	push   %ebx
 80497a2:	56                   	push   %esi
 80497a3:	55                   	push   %ebp
 80497a4:	e8 57 f0 ff ff       	call   8048800 <write@plt>
 80497a9:	83 c4 10             	add    $0x10,%esp
 80497ac:	85 c0                	test   %eax,%eax
 80497ae:	7f 0f                	jg     80497bf <submitr+0x3d6>
 80497b0:	e8 7b f0 ff ff       	call   8048830 <__errno_location@plt>
 80497b5:	83 38 04             	cmpl   $0x4,(%eax)
 80497b8:	75 0f                	jne    80497c9 <submitr+0x3e0>
 80497ba:	b8 00 00 00 00       	mov    $0x0,%eax
 80497bf:	01 c6                	add    %eax,%esi
 80497c1:	29 c3                	sub    %eax,%ebx
 80497c3:	75 d9                	jne    804979e <submitr+0x3b5>
 80497c5:	85 ff                	test   %edi,%edi
 80497c7:	79 69                	jns    8049832 <submitr+0x449>
 80497c9:	8b 44 24 18          	mov    0x18(%esp),%eax
 80497cd:	c7 00 45 72 72 6f    	movl   $0x6f727245,(%eax)
 80497d3:	c7 40 04 72 3a 20 43 	movl   $0x43203a72,0x4(%eax)
 80497da:	c7 40 08 6c 69 65 6e 	movl   $0x6e65696c,0x8(%eax)
 80497e1:	c7 40 0c 74 20 75 6e 	movl   $0x6e752074,0xc(%eax)
 80497e8:	c7 40 10 61 62 6c 65 	movl   $0x656c6261,0x10(%eax)
 80497ef:	c7 40 14 20 74 6f 20 	movl   $0x206f7420,0x14(%eax)
 80497f6:	c7 40 18 77 72 69 74 	movl   $0x74697277,0x18(%eax)
 80497fd:	c7 40 1c 65 20 74 6f 	movl   $0x6f742065,0x1c(%eax)
 8049804:	c7 40 20 20 74 68 65 	movl   $0x65687420,0x20(%eax)
 804980b:	c7 40 24 20 73 65 72 	movl   $0x72657320,0x24(%eax)
 8049812:	c7 40 28 76 65 72 00 	movl   $0x726576,0x28(%eax)
 8049819:	83 ec 0c             	sub    $0xc,%esp
 804981c:	ff 74 24 14          	pushl  0x14(%esp)
 8049820:	e8 7b f0 ff ff       	call   80488a0 <close@plt>
 8049825:	83 c4 10             	add    $0x10,%esp
 8049828:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
 804982d:	e9 b9 02 00 00       	jmp    8049aeb <submitr+0x702>
 8049832:	8b 44 24 08          	mov    0x8(%esp),%eax
 8049836:	89 44 24 40          	mov    %eax,0x40(%esp)
 804983a:	c7 44 24 44 00 00 00 	movl   $0x0,0x44(%esp)
 8049841:	00 
 8049842:	8d 44 24 4c          	lea    0x4c(%esp),%eax
 8049846:	89 44 24 48          	mov    %eax,0x48(%esp)
 804984a:	b9 00 20 00 00       	mov    $0x2000,%ecx
 804984f:	8d 94 24 4c 20 00 00 	lea    0x204c(%esp),%edx
 8049856:	8d 44 24 40          	lea    0x40(%esp),%eax
 804985a:	e8 b6 fa ff ff       	call   8049315 <rio_readlineb>
 804985f:	85 c0                	test   %eax,%eax
 8049861:	7f 7d                	jg     80498e0 <submitr+0x4f7>
 8049863:	8b 44 24 18          	mov    0x18(%esp),%eax
 8049867:	c7 00 45 72 72 6f    	movl   $0x6f727245,(%eax)
 804986d:	c7 40 04 72 3a 20 43 	movl   $0x43203a72,0x4(%eax)
 8049874:	c7 40 08 6c 69 65 6e 	movl   $0x6e65696c,0x8(%eax)
 804987b:	c7 40 0c 74 20 75 6e 	movl   $0x6e752074,0xc(%eax)
 8049882:	c7 40 10 61 62 6c 65 	movl   $0x656c6261,0x10(%eax)
 8049889:	c7 40 14 20 74 6f 20 	movl   $0x206f7420,0x14(%eax)
 8049890:	c7 40 18 72 65 61 64 	movl   $0x64616572,0x18(%eax)
 8049897:	c7 40 1c 20 66 69 72 	movl   $0x72696620,0x1c(%eax)
 804989e:	c7 40 20 73 74 20 68 	movl   $0x68207473,0x20(%eax)
 80498a5:	c7 40 24 65 61 64 65 	movl   $0x65646165,0x24(%eax)
 80498ac:	c7 40 28 72 20 66 72 	movl   $0x72662072,0x28(%eax)
 80498b3:	c7 40 2c 6f 6d 20 73 	movl   $0x73206d6f,0x2c(%eax)
 80498ba:	c7 40 30 65 72 76 65 	movl   $0x65767265,0x30(%eax)
 80498c1:	66 c7 40 34 72 00    	movw   $0x72,0x34(%eax)
 80498c7:	83 ec 0c             	sub    $0xc,%esp
 80498ca:	ff 74 24 14          	pushl  0x14(%esp)
 80498ce:	e8 cd ef ff ff       	call   80488a0 <close@plt>
 80498d3:	83 c4 10             	add    $0x10,%esp
 80498d6:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
 80498db:	e9 0b 02 00 00       	jmp    8049aeb <submitr+0x702>
 80498e0:	83 ec 0c             	sub    $0xc,%esp
 80498e3:	8d 84 24 58 80 00 00 	lea    0x8058(%esp),%eax
 80498ea:	50                   	push   %eax
 80498eb:	8d 44 24 3c          	lea    0x3c(%esp),%eax
 80498ef:	50                   	push   %eax
 80498f0:	8d 84 24 60 60 00 00 	lea    0x6060(%esp),%eax
 80498f7:	50                   	push   %eax
 80498f8:	68 6b a3 04 08       	push   $0x804a36b
 80498fd:	8d 84 24 68 20 00 00 	lea    0x2068(%esp),%eax
 8049904:	50                   	push   %eax
 8049905:	e8 06 ef ff ff       	call   8048810 <__isoc99_sscanf@plt>
 804990a:	8b 44 24 4c          	mov    0x4c(%esp),%eax
 804990e:	83 c4 20             	add    $0x20,%esp
 8049911:	3d c8 00 00 00       	cmp    $0xc8,%eax
 8049916:	0f 84 c4 00 00 00    	je     80499e0 <submitr+0x5f7>
 804991c:	83 ec 08             	sub    $0x8,%esp
 804991f:	8d 94 24 54 80 00 00 	lea    0x8054(%esp),%edx
 8049926:	52                   	push   %edx
 8049927:	50                   	push   %eax
 8049928:	68 7c a2 04 08       	push   $0x804a27c
 804992d:	6a ff                	push   $0xffffffff
 804992f:	6a 01                	push   $0x1
 8049931:	ff 74 24 34          	pushl  0x34(%esp)
 8049935:	e8 86 ef ff ff       	call   80488c0 <__sprintf_chk@plt>
 804993a:	83 c4 14             	add    $0x14,%esp
 804993d:	ff 74 24 14          	pushl  0x14(%esp)
 8049941:	e8 5a ef ff ff       	call   80488a0 <close@plt>
 8049946:	83 c4 10             	add    $0x10,%esp
 8049949:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
 804994e:	e9 98 01 00 00       	jmp    8049aeb <submitr+0x702>
 8049953:	b9 00 20 00 00       	mov    $0x2000,%ecx
 8049958:	8d 94 24 4c 20 00 00 	lea    0x204c(%esp),%edx
 804995f:	8d 44 24 40          	lea    0x40(%esp),%eax
 8049963:	e8 ad f9 ff ff       	call   8049315 <rio_readlineb>
 8049968:	85 c0                	test   %eax,%eax
 804996a:	7f 74                	jg     80499e0 <submitr+0x5f7>
 804996c:	8b 44 24 18          	mov    0x18(%esp),%eax
 8049970:	c7 00 45 72 72 6f    	movl   $0x6f727245,(%eax)
 8049976:	c7 40 04 72 3a 20 43 	movl   $0x43203a72,0x4(%eax)
 804997d:	c7 40 08 6c 69 65 6e 	movl   $0x6e65696c,0x8(%eax)
 8049984:	c7 40 0c 74 20 75 6e 	movl   $0x6e752074,0xc(%eax)
 804998b:	c7 40 10 61 62 6c 65 	movl   $0x656c6261,0x10(%eax)
 8049992:	c7 40 14 20 74 6f 20 	movl   $0x206f7420,0x14(%eax)
 8049999:	c7 40 18 72 65 61 64 	movl   $0x64616572,0x18(%eax)
 80499a0:	c7 40 1c 20 68 65 61 	movl   $0x61656820,0x1c(%eax)
 80499a7:	c7 40 20 64 65 72 73 	movl   $0x73726564,0x20(%eax)
 80499ae:	c7 40 24 20 66 72 6f 	movl   $0x6f726620,0x24(%eax)
 80499b5:	c7 40 28 6d 20 73 65 	movl   $0x6573206d,0x28(%eax)
 80499bc:	c7 40 2c 72 76 65 72 	movl   $0x72657672,0x2c(%eax)
 80499c3:	c6 40 30 00          	movb   $0x0,0x30(%eax)
 80499c7:	83 ec 0c             	sub    $0xc,%esp
 80499ca:	ff 74 24 14          	pushl  0x14(%esp)
 80499ce:	e8 cd ee ff ff       	call   80488a0 <close@plt>
 80499d3:	83 c4 10             	add    $0x10,%esp
 80499d6:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
 80499db:	e9 0b 01 00 00       	jmp    8049aeb <submitr+0x702>
 80499e0:	80 bc 24 4c 20 00 00 	cmpb   $0xd,0x204c(%esp)
 80499e7:	0d 
 80499e8:	0f 85 65 ff ff ff    	jne    8049953 <submitr+0x56a>
 80499ee:	80 bc 24 4d 20 00 00 	cmpb   $0xa,0x204d(%esp)
 80499f5:	0a 
 80499f6:	0f 85 57 ff ff ff    	jne    8049953 <submitr+0x56a>
 80499fc:	80 bc 24 4e 20 00 00 	cmpb   $0x0,0x204e(%esp)
 8049a03:	00 
 8049a04:	0f 85 49 ff ff ff    	jne    8049953 <submitr+0x56a>
 8049a0a:	b9 00 20 00 00       	mov    $0x2000,%ecx
 8049a0f:	8d 94 24 4c 20 00 00 	lea    0x204c(%esp),%edx
 8049a16:	8d 44 24 40          	lea    0x40(%esp),%eax
 8049a1a:	e8 f6 f8 ff ff       	call   8049315 <rio_readlineb>
 8049a1f:	85 c0                	test   %eax,%eax
 8049a21:	7f 7b                	jg     8049a9e <submitr+0x6b5>
 8049a23:	8b 44 24 18          	mov    0x18(%esp),%eax
 8049a27:	c7 00 45 72 72 6f    	movl   $0x6f727245,(%eax)
 8049a2d:	c7 40 04 72 3a 20 43 	movl   $0x43203a72,0x4(%eax)
 8049a34:	c7 40 08 6c 69 65 6e 	movl   $0x6e65696c,0x8(%eax)
 8049a3b:	c7 40 0c 74 20 75 6e 	movl   $0x6e752074,0xc(%eax)
 8049a42:	c7 40 10 61 62 6c 65 	movl   $0x656c6261,0x10(%eax)
 8049a49:	c7 40 14 20 74 6f 20 	movl   $0x206f7420,0x14(%eax)
 8049a50:	c7 40 18 72 65 61 64 	movl   $0x64616572,0x18(%eax)
 8049a57:	c7 40 1c 20 73 74 61 	movl   $0x61747320,0x1c(%eax)
 8049a5e:	c7 40 20 74 75 73 20 	movl   $0x20737574,0x20(%eax)
 8049a65:	c7 40 24 6d 65 73 73 	movl   $0x7373656d,0x24(%eax)
 8049a6c:	c7 40 28 61 67 65 20 	movl   $0x20656761,0x28(%eax)
 8049a73:	c7 40 2c 66 72 6f 6d 	movl   $0x6d6f7266,0x2c(%eax)
 8049a7a:	c7 40 30 20 73 65 72 	movl   $0x72657320,0x30(%eax)
 8049a81:	c7 40 34 76 65 72 00 	movl   $0x726576,0x34(%eax)
 8049a88:	83 ec 0c             	sub    $0xc,%esp
 8049a8b:	ff 74 24 14          	pushl  0x14(%esp)
 8049a8f:	e8 0c ee ff ff       	call   80488a0 <close@plt>
 8049a94:	83 c4 10             	add    $0x10,%esp
 8049a97:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
 8049a9c:	eb 4d                	jmp    8049aeb <submitr+0x702>
 8049a9e:	83 ec 08             	sub    $0x8,%esp
 8049aa1:	8d 84 24 54 20 00 00 	lea    0x2054(%esp),%eax
 8049aa8:	50                   	push   %eax
 8049aa9:	8b 7c 24 24          	mov    0x24(%esp),%edi
 8049aad:	57                   	push   %edi
 8049aae:	e8 ed ec ff ff       	call   80487a0 <strcpy@plt>
 8049ab3:	83 c4 04             	add    $0x4,%esp
 8049ab6:	ff 74 24 14          	pushl  0x14(%esp)
 8049aba:	e8 e1 ed ff ff       	call   80488a0 <close@plt>
 8049abf:	0f b6 17             	movzbl (%edi),%edx
 8049ac2:	b8 4f 00 00 00       	mov    $0x4f,%eax
 8049ac7:	83 c4 10             	add    $0x10,%esp
 8049aca:	29 d0                	sub    %edx,%eax
 8049acc:	75 13                	jne    8049ae1 <submitr+0x6f8>
 8049ace:	0f b6 57 01          	movzbl 0x1(%edi),%edx
 8049ad2:	b8 4b 00 00 00       	mov    $0x4b,%eax
 8049ad7:	29 d0                	sub    %edx,%eax
 8049ad9:	75 06                	jne    8049ae1 <submitr+0x6f8>
 8049adb:	0f b6 47 02          	movzbl 0x2(%edi),%eax
 8049adf:	f7 d8                	neg    %eax
 8049ae1:	85 c0                	test   %eax,%eax
 8049ae3:	0f 95 c0             	setne  %al
 8049ae6:	0f b6 c0             	movzbl %al,%eax
 8049ae9:	f7 d8                	neg    %eax
 8049aeb:	8b bc 24 4c a0 00 00 	mov    0xa04c(%esp),%edi
 8049af2:	65 33 3d 14 00 00 00 	xor    %gs:0x14,%edi
 8049af9:	0f 84 a9 00 00 00    	je     8049ba8 <submitr+0x7bf>
 8049aff:	e9 9f 00 00 00       	jmp    8049ba3 <submitr+0x7ba>
 8049b04:	a1 ac a2 04 08       	mov    0x804a2ac,%eax
 8049b09:	8b 7c 24 18          	mov    0x18(%esp),%edi
 8049b0d:	89 07                	mov    %eax,(%edi)
 8049b0f:	a1 eb a2 04 08       	mov    0x804a2eb,%eax
 8049b14:	89 47 3f             	mov    %eax,0x3f(%edi)
 8049b17:	89 f8                	mov    %edi,%eax
 8049b19:	83 c7 04             	add    $0x4,%edi
 8049b1c:	83 e7 fc             	and    $0xfffffffc,%edi
 8049b1f:	29 f8                	sub    %edi,%eax
 8049b21:	be ac a2 04 08       	mov    $0x804a2ac,%esi
 8049b26:	29 c6                	sub    %eax,%esi
 8049b28:	83 c0 43             	add    $0x43,%eax
 8049b2b:	c1 e8 02             	shr    $0x2,%eax
 8049b2e:	89 c1                	mov    %eax,%ecx
 8049b30:	f3 a5                	rep movsl %ds:(%esi),%es:(%edi)
 8049b32:	83 ec 0c             	sub    $0xc,%esp
 8049b35:	ff 74 24 14          	pushl  0x14(%esp)
 8049b39:	e8 62 ed ff ff       	call   80488a0 <close@plt>
 8049b3e:	83 c4 10             	add    $0x10,%esp
 8049b41:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
 8049b46:	eb a3                	jmp    8049aeb <submitr+0x702>
 8049b48:	8d 84 24 4c 40 00 00 	lea    0x404c(%esp),%eax
 8049b4f:	50                   	push   %eax
 8049b50:	ff 74 24 18          	pushl  0x18(%esp)
 8049b54:	ff 74 24 18          	pushl  0x18(%esp)
 8049b58:	ff 74 24 18          	pushl  0x18(%esp)
 8049b5c:	68 f0 a2 04 08       	push   $0x804a2f0
 8049b61:	68 00 20 00 00       	push   $0x2000
 8049b66:	6a 01                	push   $0x1
 8049b68:	8d bc 24 68 20 00 00 	lea    0x2068(%esp),%edi
 8049b6f:	57                   	push   %edi
 8049b70:	e8 4b ed ff ff       	call   80488c0 <__sprintf_chk@plt>
 8049b75:	b8 00 00 00 00       	mov    $0x0,%eax
 8049b7a:	b9 ff ff ff ff       	mov    $0xffffffff,%ecx
 8049b7f:	f2 ae                	repnz scas %es:(%edi),%al
 8049b81:	f7 d1                	not    %ecx
 8049b83:	8d 79 ff             	lea    -0x1(%ecx),%edi
 8049b86:	83 c4 20             	add    $0x20,%esp
 8049b89:	89 fb                	mov    %edi,%ebx
 8049b8b:	8d b4 24 4c 20 00 00 	lea    0x204c(%esp),%esi
 8049b92:	8b 6c 24 08          	mov    0x8(%esp),%ebp
 8049b96:	85 ff                	test   %edi,%edi
 8049b98:	0f 85 00 fc ff ff    	jne    804979e <submitr+0x3b5>
 8049b9e:	e9 8f fc ff ff       	jmp    8049832 <submitr+0x449>
 8049ba3:	e8 e8 eb ff ff       	call   8048790 <__stack_chk_fail@plt>
 8049ba8:	81 c4 5c a0 00 00    	add    $0xa05c,%esp
 8049bae:	5b                   	pop    %ebx
 8049baf:	5e                   	pop    %esi
 8049bb0:	5f                   	pop    %edi
 8049bb1:	5d                   	pop    %ebp
 8049bb2:	c3                   	ret    

08049bb3 <init_timeout>:
 8049bb3:	53                   	push   %ebx
 8049bb4:	83 ec 08             	sub    $0x8,%esp
 8049bb7:	8b 5c 24 10          	mov    0x10(%esp),%ebx
 8049bbb:	85 db                	test   %ebx,%ebx
 8049bbd:	74 24                	je     8049be3 <init_timeout+0x30>
 8049bbf:	83 ec 08             	sub    $0x8,%esp
 8049bc2:	68 f2 92 04 08       	push   $0x80492f2
 8049bc7:	6a 0e                	push   $0xe
 8049bc9:	e8 92 eb ff ff       	call   8048760 <signal@plt>
 8049bce:	85 db                	test   %ebx,%ebx
 8049bd0:	b8 00 00 00 00       	mov    $0x0,%eax
 8049bd5:	0f 48 d8             	cmovs  %eax,%ebx
 8049bd8:	89 1c 24             	mov    %ebx,(%esp)
 8049bdb:	e8 a0 eb ff ff       	call   8048780 <alarm@plt>
 8049be0:	83 c4 10             	add    $0x10,%esp
 8049be3:	83 c4 08             	add    $0x8,%esp
 8049be6:	5b                   	pop    %ebx
 8049be7:	c3                   	ret    

08049be8 <init_driver>:
 8049be8:	57                   	push   %edi
 8049be9:	56                   	push   %esi
 8049bea:	53                   	push   %ebx
 8049beb:	83 ec 28             	sub    $0x28,%esp
 8049bee:	8b 74 24 38          	mov    0x38(%esp),%esi
 8049bf2:	65 a1 14 00 00 00    	mov    %gs:0x14,%eax
 8049bf8:	89 44 24 24          	mov    %eax,0x24(%esp)
 8049bfc:	31 c0                	xor    %eax,%eax
 8049bfe:	6a 01                	push   $0x1
 8049c00:	6a 0d                	push   $0xd
 8049c02:	e8 59 eb ff ff       	call   8048760 <signal@plt>
 8049c07:	83 c4 08             	add    $0x8,%esp
 8049c0a:	6a 01                	push   $0x1
 8049c0c:	6a 1d                	push   $0x1d
 8049c0e:	e8 4d eb ff ff       	call   8048760 <signal@plt>
 8049c13:	83 c4 08             	add    $0x8,%esp
 8049c16:	6a 01                	push   $0x1
 8049c18:	6a 1d                	push   $0x1d
 8049c1a:	e8 41 eb ff ff       	call   8048760 <signal@plt>
 8049c1f:	83 c4 0c             	add    $0xc,%esp
 8049c22:	6a 00                	push   $0x0
 8049c24:	6a 01                	push   $0x1
 8049c26:	6a 02                	push   $0x2
 8049c28:	e8 23 ec ff ff       	call   8048850 <socket@plt>
 8049c2d:	83 c4 10             	add    $0x10,%esp
 8049c30:	85 c0                	test   %eax,%eax
 8049c32:	79 4e                	jns    8049c82 <init_driver+0x9a>
 8049c34:	c7 06 45 72 72 6f    	movl   $0x6f727245,(%esi)
 8049c3a:	c7 46 04 72 3a 20 43 	movl   $0x43203a72,0x4(%esi)
 8049c41:	c7 46 08 6c 69 65 6e 	movl   $0x6e65696c,0x8(%esi)
 8049c48:	c7 46 0c 74 20 75 6e 	movl   $0x6e752074,0xc(%esi)
 8049c4f:	c7 46 10 61 62 6c 65 	movl   $0x656c6261,0x10(%esi)
 8049c56:	c7 46 14 20 74 6f 20 	movl   $0x206f7420,0x14(%esi)
 8049c5d:	c7 46 18 63 72 65 61 	movl   $0x61657263,0x18(%esi)
 8049c64:	c7 46 1c 74 65 20 73 	movl   $0x73206574,0x1c(%esi)
 8049c6b:	c7 46 20 6f 63 6b 65 	movl   $0x656b636f,0x20(%esi)
 8049c72:	66 c7 46 24 74 00    	movw   $0x74,0x24(%esi)
 8049c78:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
 8049c7d:	e9 1f 01 00 00       	jmp    8049da1 <init_driver+0x1b9>
 8049c82:	89 c3                	mov    %eax,%ebx
 8049c84:	83 ec 0c             	sub    $0xc,%esp
 8049c87:	68 7c a3 04 08       	push   $0x804a37c
 8049c8c:	e8 df eb ff ff       	call   8048870 <gethostbyname@plt>
 8049c91:	83 c4 10             	add    $0x10,%esp
 8049c94:	85 c0                	test   %eax,%eax
 8049c96:	75 6c                	jne    8049d04 <init_driver+0x11c>
 8049c98:	c7 06 45 72 72 6f    	movl   $0x6f727245,(%esi)
 8049c9e:	c7 46 04 72 3a 20 44 	movl   $0x44203a72,0x4(%esi)
 8049ca5:	c7 46 08 4e 53 20 69 	movl   $0x6920534e,0x8(%esi)
 8049cac:	c7 46 0c 73 20 75 6e 	movl   $0x6e752073,0xc(%esi)
 8049cb3:	c7 46 10 61 62 6c 65 	movl   $0x656c6261,0x10(%esi)
 8049cba:	c7 46 14 20 74 6f 20 	movl   $0x206f7420,0x14(%esi)
 8049cc1:	c7 46 18 72 65 73 6f 	movl   $0x6f736572,0x18(%esi)
 8049cc8:	c7 46 1c 6c 76 65 20 	movl   $0x2065766c,0x1c(%esi)
 8049ccf:	c7 46 20 73 65 72 76 	movl   $0x76726573,0x20(%esi)
 8049cd6:	c7 46 24 65 72 20 61 	movl   $0x61207265,0x24(%esi)
 8049cdd:	c7 46 28 64 64 72 65 	movl   $0x65726464,0x28(%esi)
 8049ce4:	66 c7 46 2c 73 73    	movw   $0x7373,0x2c(%esi)
 8049cea:	c6 46 2e 00          	movb   $0x0,0x2e(%esi)
 8049cee:	83 ec 0c             	sub    $0xc,%esp
 8049cf1:	53                   	push   %ebx
 8049cf2:	e8 a9 eb ff ff       	call   80488a0 <close@plt>
 8049cf7:	83 c4 10             	add    $0x10,%esp
 8049cfa:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
 8049cff:	e9 9d 00 00 00       	jmp    8049da1 <init_driver+0x1b9>
 8049d04:	8d 7c 24 0c          	lea    0xc(%esp),%edi
 8049d08:	c7 44 24 0c 00 00 00 	movl   $0x0,0xc(%esp)
 8049d0f:	00 
 8049d10:	c7 44 24 10 00 00 00 	movl   $0x0,0x10(%esp)
 8049d17:	00 
 8049d18:	c7 44 24 14 00 00 00 	movl   $0x0,0x14(%esp)
 8049d1f:	00 
 8049d20:	c7 44 24 18 00 00 00 	movl   $0x0,0x18(%esp)
 8049d27:	00 
 8049d28:	66 c7 44 24 0c 02 00 	movw   $0x2,0xc(%esp)
 8049d2f:	6a 0c                	push   $0xc
 8049d31:	ff 70 0c             	pushl  0xc(%eax)
 8049d34:	8b 40 10             	mov    0x10(%eax),%eax
 8049d37:	ff 30                	pushl  (%eax)
 8049d39:	8d 44 24 1c          	lea    0x1c(%esp),%eax
 8049d3d:	50                   	push   %eax
 8049d3e:	e8 8d ea ff ff       	call   80487d0 <__memmove_chk@plt>
 8049d43:	66 c7 44 24 1e 3b 6e 	movw   $0x6e3b,0x1e(%esp)
 8049d4a:	83 c4 0c             	add    $0xc,%esp
 8049d4d:	6a 10                	push   $0x10
 8049d4f:	57                   	push   %edi
 8049d50:	53                   	push   %ebx
 8049d51:	e8 3a eb ff ff       	call   8048890 <connect@plt>
 8049d56:	83 c4 10             	add    $0x10,%esp
 8049d59:	85 c0                	test   %eax,%eax
 8049d5b:	79 2a                	jns    8049d87 <init_driver+0x19f>
 8049d5d:	83 ec 0c             	sub    $0xc,%esp
 8049d60:	68 7c a3 04 08       	push   $0x804a37c
 8049d65:	68 3c a3 04 08       	push   $0x804a33c
 8049d6a:	6a ff                	push   $0xffffffff
 8049d6c:	6a 01                	push   $0x1
 8049d6e:	56                   	push   %esi
 8049d6f:	e8 4c eb ff ff       	call   80488c0 <__sprintf_chk@plt>
 8049d74:	83 c4 14             	add    $0x14,%esp
 8049d77:	53                   	push   %ebx
 8049d78:	e8 23 eb ff ff       	call   80488a0 <close@plt>
 8049d7d:	83 c4 10             	add    $0x10,%esp
 8049d80:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
 8049d85:	eb 1a                	jmp    8049da1 <init_driver+0x1b9>
 8049d87:	83 ec 0c             	sub    $0xc,%esp
 8049d8a:	53                   	push   %ebx
 8049d8b:	e8 10 eb ff ff       	call   80488a0 <close@plt>
 8049d90:	66 c7 06 4f 4b       	movw   $0x4b4f,(%esi)
 8049d95:	c6 46 02 00          	movb   $0x0,0x2(%esi)
 8049d99:	83 c4 10             	add    $0x10,%esp
 8049d9c:	b8 00 00 00 00       	mov    $0x0,%eax
 8049da1:	8b 54 24 1c          	mov    0x1c(%esp),%edx
 8049da5:	65 33 15 14 00 00 00 	xor    %gs:0x14,%edx
 8049dac:	74 05                	je     8049db3 <init_driver+0x1cb>
 8049dae:	e8 dd e9 ff ff       	call   8048790 <__stack_chk_fail@plt>
 8049db3:	83 c4 20             	add    $0x20,%esp
 8049db6:	5b                   	pop    %ebx
 8049db7:	5e                   	pop    %esi
 8049db8:	5f                   	pop    %edi
 8049db9:	c3                   	ret    

08049dba <driver_post>:
 8049dba:	53                   	push   %ebx
 8049dbb:	83 ec 08             	sub    $0x8,%esp
 8049dbe:	8b 44 24 10          	mov    0x10(%esp),%eax
 8049dc2:	8b 5c 24 1c          	mov    0x1c(%esp),%ebx
 8049dc6:	83 7c 24 18 00       	cmpl   $0x0,0x18(%esp)
 8049dcb:	74 26                	je     8049df3 <driver_post+0x39>
 8049dcd:	83 ec 04             	sub    $0x4,%esp
 8049dd0:	ff 74 24 18          	pushl  0x18(%esp)
 8049dd4:	68 8a a3 04 08       	push   $0x804a38a
 8049dd9:	6a 01                	push   $0x1
 8049ddb:	e8 60 ea ff ff       	call   8048840 <__printf_chk@plt>
 8049de0:	66 c7 03 4f 4b       	movw   $0x4b4f,(%ebx)
 8049de5:	c6 43 02 00          	movb   $0x0,0x2(%ebx)
 8049de9:	83 c4 10             	add    $0x10,%esp
 8049dec:	b8 00 00 00 00       	mov    $0x0,%eax
 8049df1:	eb 3e                	jmp    8049e31 <driver_post+0x77>
 8049df3:	85 c0                	test   %eax,%eax
 8049df5:	74 2c                	je     8049e23 <driver_post+0x69>
 8049df7:	80 38 00             	cmpb   $0x0,(%eax)
 8049dfa:	74 27                	je     8049e23 <driver_post+0x69>
 8049dfc:	83 ec 04             	sub    $0x4,%esp
 8049dff:	53                   	push   %ebx
 8049e00:	ff 74 24 1c          	pushl  0x1c(%esp)
 8049e04:	68 a1 a3 04 08       	push   $0x804a3a1
 8049e09:	50                   	push   %eax
 8049e0a:	68 a9 a3 04 08       	push   $0x804a3a9
 8049e0f:	68 6e 3b 00 00       	push   $0x3b6e
 8049e14:	68 7c a3 04 08       	push   $0x804a37c
 8049e19:	e8 cb f5 ff ff       	call   80493e9 <submitr>
 8049e1e:	83 c4 20             	add    $0x20,%esp
 8049e21:	eb 0e                	jmp    8049e31 <driver_post+0x77>
 8049e23:	66 c7 03 4f 4b       	movw   $0x4b4f,(%ebx)
 8049e28:	c6 43 02 00          	movb   $0x0,0x2(%ebx)
 8049e2c:	b8 00 00 00 00       	mov    $0x0,%eax
 8049e31:	83 c4 08             	add    $0x8,%esp
 8049e34:	5b                   	pop    %ebx
 8049e35:	c3                   	ret    
 8049e36:	66 90                	xchg   %ax,%ax
 8049e38:	66 90                	xchg   %ax,%ax
 8049e3a:	66 90                	xchg   %ax,%ax
 8049e3c:	66 90                	xchg   %ax,%ax
 8049e3e:	66 90                	xchg   %ax,%ax

08049e40 <__libc_csu_init>:
 8049e40:	55                   	push   %ebp
 8049e41:	57                   	push   %edi
 8049e42:	56                   	push   %esi
 8049e43:	53                   	push   %ebx
 8049e44:	e8 c7 ea ff ff       	call   8048910 <__x86.get_pc_thunk.bx>
 8049e49:	81 c3 b7 21 00 00    	add    $0x21b7,%ebx
 8049e4f:	83 ec 0c             	sub    $0xc,%esp
 8049e52:	8b 6c 24 20          	mov    0x20(%esp),%ebp
 8049e56:	8d b3 0c ff ff ff    	lea    -0xf4(%ebx),%esi
 8049e5c:	e8 93 e8 ff ff       	call   80486f4 <_init>
 8049e61:	8d 83 08 ff ff ff    	lea    -0xf8(%ebx),%eax
 8049e67:	29 c6                	sub    %eax,%esi
 8049e69:	c1 fe 02             	sar    $0x2,%esi
 8049e6c:	85 f6                	test   %esi,%esi
 8049e6e:	74 25                	je     8049e95 <__libc_csu_init+0x55>
 8049e70:	31 ff                	xor    %edi,%edi
 8049e72:	8d b6 00 00 00 00    	lea    0x0(%esi),%esi
 8049e78:	83 ec 04             	sub    $0x4,%esp
 8049e7b:	ff 74 24 2c          	pushl  0x2c(%esp)
 8049e7f:	ff 74 24 2c          	pushl  0x2c(%esp)
 8049e83:	55                   	push   %ebp
 8049e84:	ff 94 bb 08 ff ff ff 	call   *-0xf8(%ebx,%edi,4)
 8049e8b:	83 c7 01             	add    $0x1,%edi
 8049e8e:	83 c4 10             	add    $0x10,%esp
 8049e91:	39 f7                	cmp    %esi,%edi
 8049e93:	75 e3                	jne    8049e78 <__libc_csu_init+0x38>
 8049e95:	83 c4 0c             	add    $0xc,%esp
 8049e98:	5b                   	pop    %ebx
 8049e99:	5e                   	pop    %esi
 8049e9a:	5f                   	pop    %edi
 8049e9b:	5d                   	pop    %ebp
 8049e9c:	c3                   	ret    
 8049e9d:	8d 76 00             	lea    0x0(%esi),%esi

08049ea0 <__libc_csu_fini>:
 8049ea0:	f3 c3                	repz ret 

Disassembly of section .fini:

08049ea4 <_fini>:
 8049ea4:	53                   	push   %ebx
 8049ea5:	83 ec 08             	sub    $0x8,%esp
 8049ea8:	e8 63 ea ff ff       	call   8048910 <__x86.get_pc_thunk.bx>
 8049ead:	81 c3 53 21 00 00    	add    $0x2153,%ebx
 8049eb3:	83 c4 08             	add    $0x8,%esp
 8049eb6:	5b                   	pop    %ebx
 8049eb7:	c3                   	ret    

```

