; Everything that comes after a semicolon (;) is a comment

C2 equ 2
C3 equ 3
C4 equ 4
C5 equ 5
C6 equ 6
C7 equ 7
C8 equ 8
C9 equ 9
C10 equ 10
CJ equ 11
CQ equ 12
CK equ 13
CA equ 14

TRUE equ 1
FALSE equ 0

section .text

; You should implement functions in the .text section

; the global directive makes a function visible to the test files
global value_of_card
value_of_card:
    ; This function takes as parameter a number representing a card
    ; The function should return the numerical value of the passed-in card
    mov rax, rdi ; default case
    cmp rdi, 14
    je .ace
    
    cmp rdi, 10
    jle .ncard
    
    mov rax, 10
    jmp .ncard
    
    .ace:
        mov rax, 1
    
    .ncard:
        ret
    

global higher_card
higher_card:
    ; This function takes as parameters two numbers each representing a card
    ; The function should return which card has the higher value
    ; If both have the same value, both should be returned
    ; If one is higher, the second one should be 0
    ;Defaults
    mov rax, rdi
    mov rdx, rsi
    
    ;Normalize cards
    ;Normalize first card
    mov r8, rdi
    cmp rdi, 14
    je .ace1
    cmp rdi, 10
    jle .norm2
    mov r8, 10
    jmp .norm2
    .ace1:
        mov r8, 1
        
    ;Normalize second card
    .norm2:
    mov r9, rsi
    cmp rsi, 14
    je .ace2
    cmp rsi, 10
    jle .compare
    mov r9, 10
    jmp .compare
    .ace2:
        mov r9, 1

    .compare:
        cmp r8, r9
        jg .first ;first is bigger
        jl .second ;second is bigger
        ret

    .first:
        mov rdx, 0
        ret
        
    .second:
        mov rax, rdx
        mov rdx, 0
        ret


global value_of_ace
value_of_ace:
    ; This function takes as parameters two numbers each representing a card
    ; The function should return the value of an upcoming ace
    mov r8, rdi
    add r8, rsi ;sum of both cards
    cmp r8, 10 ;would adding 11 cause a bust, i.e total exceeds 21?
    jg .ace1 ;if yes then ace musts be 1
    mov rax, 11
    ret
    .ace1: 
        mov rax, 1
        ret

global is_blackjack
is_blackjack:
    ; This function takes as parameters two numbers each representing a card
    ; The function should return TRUE if the two cards form a blackjack, and FALSE otherwise
    cmp rdi, 14
    je .10card ;looks for a card of val 10
    cmp rdi, 10
    jge .acecard ;looks for ace
    mov rax, FALSE
    ret

    .10card:
        cmp rsi, 14
        je .default
        cmp rsi,10
        jge .other
        mov rax, FALSE
        ret
    
    .acecard:
        cmp rsi, 14
        je .other
        mov rax, FALSE
        ret

    .other:
        mov rax, TRUE
        ret

    .default:
        mov rax, FALSE
        ret


global can_split_pairs
can_split_pairs:
    ; This function takes as parameters two numbers each representing a card
    ; The function should return TRUE if the two cards can be split into two pairs, and FALSE otherwise
    cmp rdi, 14
    je .ace
    cmp rdi, 10
    jge .tens
    cmp rdi, rsi
    je .true
    jmp .false

    .ace:
        cmp rsi, 14
        je .true
        jmp .false

    .tens:
        cmp rsi, 14
        je .false
        cmp rsi, 10
        jge .true
        jmp .false

    .true:
        mov rax, TRUE
        ret

    .false:
        mov rax, FALSE
        ret

global can_double_down
can_double_down:
    ; This function takes as parameters two numbers each representing a card
    ; The function should return TRUE if the two cards form a hand that can be doubled down, and FALSE otherwise
    cmp rdi, 14
    je .lowereight ;find at least 8
    cmp rdi, 10
    jge .findace ;find ace
    
    mov r9, rdi
    add r9, rsi
    cmp r9, 9
    jl .false
    cmp r9, 11
    jle .true
    jmp .false

    .lowereight:
        cmp rsi, 14
        je .false
        cmp rsi, 8
        jge .true
        jmp .false

    .findace:
        cmp rsi, 14
        je .true
        jmp .false

    .false:
        mov rax, FALSE
        ret
    .true:
        mov rax, TRUE
        ret

%ifidn __OUTPUT_FORMAT__,elf64
section .note.GNU-stack noalloc noexec nowrite progbits
%endif
