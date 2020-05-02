/* 
 * Copyright (c) 2001-2002 Secure Software, Inc
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
 *
 */

#ifndef PERL_TOKENS_H
#define PERL_TOKENS_H

/*
 * Tokens that are specific to the Python language
 */

#define TOKEN_ID_SCALAR             (TOKEN_PERL_START +  0)
#define TOKEN_ID_ARRAY              (TOKEN_PERL_START +  1)
#define TOKEN_ID_HASHT              (TOKEN_PERL_START +  2)
#define TOKEN_ID_HANDLE             TOKEN_IDENTIFIER
#define TOKEN_REPEAT_ASSIGN	      (TOKEN_PERL_START +  3)
#define TOKEN_CONCAT_ASSIGN	      (TOKEN_PERL_START +  4)
#define TOKEN_BACKTICK_LITERAL      (TOKEN_PERL_START +  5)
#define TOKEN_QQSTRING_LITERAL      TOKEN_STRING_CONST
#define TOKEN_QSTRING_LITERAL	      TOKEN_STRING_CONST 
#define TOKEN_NULL	      (TOKEN_PERL_START +  8)
#define TOKEN_DATA	      (TOKEN_PERL_START +  9)
#define TOKEN_FILE	      (TOKEN_PERL_START + 10)
#define TOKEN_LINE	      (TOKEN_PERL_START + 11)
#define TOKEN_PACKAGE	      (TOKEN_PERL_START + 12)
#define TOKEN_REGEXP		      (TOKEN_PERL_START + 13)
#define TOKEN_PERLPOD               (TOKEN_PERL_START + 14)

/*
#define ABS		      TOKEN_IDENTIIER
#define ACCEPT                TOKEN_IDENTIIER
#define ALARM		      TOKEN_IDENTIIER
#define ATAN2		      TOKEN_IDENTIIER
#define BIND		      TOKEN_IDENTIIER
#define BINMODE		      TOKEN_IDENTIIER
#define BLESS		      TOKEN_IDENTIIER
#define CALLER		      TOKEN_IDENTIIER
#define CHDIR		      TOKEN_IDENTIIER
#define CHMOD		      TOKEN_IDENTIIER
#define CHOMP                 TOKEN_IDENTIIER
#define CHOP	              TOKEN_IDENTIIER
#define CHOWN	              TOKEN_IDENTIIER
#define CHR	              TOKEN_IDENTIIER
#define CHROOT	              TOKEN_IDENTIIER
#define CLOSE	              TOKEN_IDENTIIER
#define CLOSEDIR              TOKEN_IDENTIIER
#define CMP	              TOKEN_IDENTIIER
#define CONNECT	              TOKEN_IDENTIIER
#define COS	              TOKEN_IDENTIIER
#define CRYPT	              TOKEN_IDENTIIER
#define DBMCLOSE              TOKEN_IDENTIIER
#define DBMOPEN               TOKEN_IDENTIIER
#define DEFINED               TOKEN_IDENTIIER
#define DELETE                TOKEN_IDENTIIER
#define DIE                   TOKEN_IDENTIIER
#define DUMP                  TOKEN_IDENTIIER
#define EACH                  TOKEN_IDENTIIER
#define ELSIF                 TOKEN_IDENTIIER
#define ENDGRENT              TOKEN_IDENTIIER
#define ENDHOSTENT		TOKEN_IDENTIIER
#define ENDNETENT		TOKEN_IDENTIIER
#define ENDPROTOENT		TOKEN_IDENTIIER
#define ENDPWENT		TOKEN_IDENTIIER
#define ENDSERVENT		TOKEN_IDENTIIER
#define EQ		TOKEN_IDENTIIER
#define EVAL		TOKEN_IDENTIIER
#define EXISTS		TOKEN_IDENTIIER
#define EXIT		TOKEN_IDENTIIER
#define EXP		TOKEN_IDENTIIER
#define FCNTL		TOKEN_IDENTIIER
#define FILENO		TOKEN_IDENTIIER
#define FLOCK		TOKEN_IDENTIIER
#define FOREACH		TOKEN_IDENTIIER
#define FORK		TOKEN_IDENTIIER
#define FORMAT		TOKEN_IDENTIIER
#define FORMLINE		TOKEN_IDENTIIER
#define GE		TOKEN_IDENTIIER
#define GETC		TOKEN_IDENTIIER
#define GETGRENT		TOKEN_IDENTIIER
#define GETGRGID		TOKEN_IDENTIIER
#define GETGRNAM		TOKEN_IDENTIIER
#define GETHOSTBYADDR		TOKEN_IDENTIIER
#define GETHOSTBYNAME		TOKEN_IDENTIIER
#define GETHOSTENT		TOKEN_IDENTIIER
#define GETLOGIN		TOKEN_IDENTIIER
#define GETNETBYADDR		TOKEN_IDENTIIER
#define GETNETBYNAME		TOKEN_IDENTIIER
#define GETNETENT		TOKEN_IDENTIIER
#define GETPEERNAME		TOKEN_IDENTIIER
#define GETPGRP		TOKEN_IDENTIIER
#define GETPPID		TOKEN_IDENTIIER
#define GETPRIORITY		TOKEN_IDENTIIER
#define GETPROTOBYNAME		TOKEN_IDENTIIER
#define GETPROTOBYNUMBER		TOKEN_IDENTIIER
#define GETPROTOENT		TOKEN_IDENTIIER
#define GETPWENT		TOKEN_IDENTIIER
#define GETPWNAM		TOKEN_IDENTIIER
#define GETPWUID		TOKEN_IDENTIIER
#define GETSERVBYNAME		TOKEN_IDENTIIER
#define GETSERVBYPORT		TOKEN_IDENTIIER
#define GETSERVENT		TOKEN_IDENTIIER
#define GETSOCKNAME		TOKEN_IDENTIIER
#define GETSOCKOPT		TOKEN_IDENTIIER
#define GLOB		TOKEN_IDENTIIER
#define GMTIME		TOKEN_IDENTIIER
#define GREP		TOKEN_IDENTIIER
#define GT		TOKEN_IDENTIIER
#define HEX		TOKEN_IDENTIIER
#define INDEX		TOKEN_IDENTIIER
#define IOCTL		TOKEN_IDENTIIER
#define JOIN		TOKEN_IDENTIIER
#define KEYS		TOKEN_IDENTIIER
#define KILL		TOKEN_IDENTIIER
#define LAST		TOKEN_IDENTIIER
#define LC		TOKEN_IDENTIIER
#define LCFIRST		TOKEN_IDENTIIER
#define LE		TOKEN_IDENTIIER
#define LENGTH		TOKEN_IDENTIIER
#define LINK		TOKEN_IDENTIIER
#define LISTEN		TOKEN_IDENTIIER
#define LOCAL		TOKEN_IDENTIIER
#define LOCALTIME		TOKEN_IDENTIIER
#define LOCK		TOKEN_IDENTIIER
#define LOG		TOKEN_IDENTIIER
#define LSTAT		TOKEN_IDENTIIER
#define LT		TOKEN_IDENTIIER
#define MAP		TOKEN_IDENTIIER
#define MKDIR		TOKEN_IDENTIIER
#define MSGCTL		TOKEN_IDENTIIER
#define MSGGET		TOKEN_IDENTIIER
#define MSGRCV		TOKEN_IDENTIIER
#define MSGSND		TOKEN_IDENTIIER
#define MY		TOKEN_IDENTIIER
#define NE		TOKEN_IDENTIIER
#define NEXT		TOKEN_IDENTIIER
#define NO		TOKEN_IDENTIIER
#define OCT		TOKEN_IDENTIIER
#define OPEN		TOKEN_IDENTIIER
#define OPENDIR		TOKEN_IDENTIIER
#define ORD		TOKEN_IDENTIIER
#define OUR		TOKEN_IDENTIIER
#define PACK		TOKEN_IDENTIIER
#define PACKAGE		TOKEN_IDENTIIER
#define PIPE		TOKEN_IDENTIIER
#define POP		TOKEN_IDENTIIER
#define POS		TOKEN_IDENTIIER
#define PRINTF		TOKEN_IDENTIIER
#define PROTOTYPE		TOKEN_IDENTIIER
#define PUSH		TOKEN_IDENTIIER
#define QQ		TOKEN_IDENTIIER
#define QR		TOKEN_IDENTIIER
#define QUOTEMETA		TOKEN_IDENTIIER
#define QW		TOKEN_IDENTIIER
#define QX		TOKEN_IDENTIIER
#define RAND		TOKEN_IDENTIIER
#define READ		TOKEN_IDENTIIER
#define READDIR		TOKEN_IDENTIIER
#define READLINE		TOKEN_IDENTIIER
#define READLINK		TOKEN_IDENTIIER
#define READPIPE		TOKEN_IDENTIIER
#define RECV		TOKEN_IDENTIIER
#define REDO		TOKEN_IDENTIIER
#define REF		TOKEN_IDENTIIER
#define RENAME		TOKEN_IDENTIIER
#define REQUIRE		TOKEN_IDENTIIER
#define RESET		TOKEN_IDENTIIER
#define REVERSE		TOKEN_IDENTIIER
#define REWINDDIR		TOKEN_IDENTIIER
#define RINDEX		TOKEN_IDENTIIER
#define RMDIR		TOKEN_IDENTIIER
#define SCALAR		TOKEN_IDENTIIER
#define SEEK		TOKEN_IDENTIIER
#define SEEKDIR		TOKEN_IDENTIIER
#define SELECT		TOKEN_IDENTIIER
#define SEMCTL		TOKEN_IDENTIIER
#define SEMGET		TOKEN_IDENTIIER
#define SEMOP		TOKEN_IDENTIIER
#define SEND		TOKEN_IDENTIIER
#define SETGRENT		TOKEN_IDENTIIER
#define SETHOSTENT		TOKEN_IDENTIIER
#define SETNETENT		TOKEN_IDENTIIER
#define SETPGRP		TOKEN_IDENTIIER
#define SETPRIORITY		TOKEN_IDENTIIER
#define SETPROTOENT		TOKEN_IDENTIIER
#define SETPWENT		TOKEN_IDENTIIER
#define SETSERVENT		TOKEN_IDENTIIER
#define SETSOCKOPT		TOKEN_IDENTIIER
#define SHIFT		TOKEN_IDENTIIER
#define SHMCTL		TOKEN_IDENTIIER
#define SHMGET		TOKEN_IDENTIIER
#define SHMREAD		TOKEN_IDENTIIER
#define SHMWRITE		TOKEN_IDENTIIER
#define SHUTDOWN		TOKEN_IDENTIIER
#define SIN		TOKEN_IDENTIIER
#define SLEEP		TOKEN_IDENTIIER
#define SOCKET		TOKEN_IDENTIIER
#define SOCKETPAIR		TOKEN_IDENTIIER
#define SORT		TOKEN_IDENTIIER
#define SPLICE		TOKEN_IDENTIIER
#define SPLIT		TOKEN_IDENTIIER
#define SPRINTF		TOKEN_IDENTIIER
#define SQRT		TOKEN_IDENTIIER
#define SRAND		TOKEN_IDENTIIER
#define STAT		TOKEN_IDENTIIER
#define STUDY		TOKEN_IDENTIIER
#define SUB		TOKEN_IDENTIIER
#define SUBSTR		TOKEN_IDENTIIER
#define SYMLINK		TOKEN_IDENTIIER
#define SYSCALL		TOKEN_IDENTIIER
#define SYSOPEN		TOKEN_IDENTIIER
#define SYSREAD		TOKEN_IDENTIIER
#define SYSSEEK		TOKEN_IDENTIIER
#define SYSTEM		TOKEN_IDENTIIER
#define SYSWRITE		TOKEN_IDENTIIER
#define TELL		TOKEN_IDENTIIER
#define TELLDIR		TOKEN_IDENTIIER
#define TIE		TOKEN_IDENTIIER
#define TIED		TOKEN_IDENTIIER
#define TIME		TOKEN_IDENTIIER
#define TIMES		TOKEN_IDENTIIER
#define TR		TOKEN_IDENTIIER
#define TRUNCATE		TOKEN_IDENTIIER
#define UC		TOKEN_IDENTIIER
#define UCFIRST		TOKEN_IDENTIIER
#define UMASK		TOKEN_IDENTIIER
#define UNDEF		TOKEN_IDENTIIER
#define UNLESS		TOKEN_IDENTIIER
#define UNLINK		TOKEN_IDENTIIER
#define UNPACK		TOKEN_IDENTIIER
#define UNSHIFT		TOKEN_IDENTIIER
#define UNTIE		TOKEN_IDENTIIER
#define UNTIL		TOKEN_IDENTIIER
#define USE		TOKEN_IDENTIIER
#define UTIME		TOKEN_IDENTIIER
#define VALUES		TOKEN_IDENTIIER
#define VEC		TOKEN_IDENTIIER
#define WAIT		TOKEN_IDENTIIER
#define WAITPID		TOKEN_IDENTIIER
#define WANTARRAY		TOKEN_IDENTIIER
#define WARN		TOKEN_IDENTIIER
#define WRITE		TOKEN_IDENTIIER
#define XOR		TOKEN_IDENTIIER
*/

#endif /*PERL_TOKENS_H*/