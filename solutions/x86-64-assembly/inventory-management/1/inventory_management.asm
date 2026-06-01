; Everything that comes after a semicolon (;) is a comment

WEIGHT_OF_EMPTY_BOX equ 500
TRUCK_HEIGHT equ 300
PAY_PER_BOX equ 5
PAY_PER_TRUCK_TRIP equ 220

section .text

; You should implement functions in the .text section
; A skeleton is provided for the first function

; the global directive makes a function visible to the test files
global get_box_weight
get_box_weight:
    imul edi, esi
    imul edx, ecx
    mov eax, edi
    add eax, edx
    add eax, WEIGHT_OF_EMPTY_BOX
    ret

global max_number_of_boxes
max_number_of_boxes:
    mov eax, TRUCK_HEIGHT
    xor edx, edx
    div edi
    ret

global items_to_be_moved
items_to_be_moved:
    sub edi, esi
    mov eax, edi
    ret

global calculate_payment
calculate_payment:
    ; TODO: define the 'calculate_payment' function
    ; This function takes the following parameters:
    ; - The upfront payment, as a 64-bit non-negative integer
    ; - The total number of boxes moved, as a 32-bit non-negative integer
    ; - The number of truck trips made, as a 32-bit non-negative integer
    ; - The number of lost items, as a 32-bit non-negative integer
    ; - The value of each lost item, as a 64-bit non-negative integer
    ; - The number of other workers to split the payment/debt with you, as a 8-bit positive integer
    ; The function must return how much you should be paid, or pay, at the end, as a 64-bit integer (possibly negative)
    ; Remember that you get your share and also the remainder of the division
    ;Total to be paid
    mov eax, esi
    imul rax, 5 ;per box
    mov r10d, edx
    imul r10, 220 ;per trip
    add rax, r10 ;total

    ; Deduct losses
    mov r11d, ecx
    imul r11, r8

    sub rax, r11 ;lost boxes
    sub rax, rdi ; upfront pay

    ;Split amount
    movzx r9, r9b
    add r9, 1 ;add owner

    cqo
    idiv r9

    add rax, rdx
    
    ret

%ifidn __OUTPUT_FORMAT__,elf64
section .note.GNU-stack noalloc noexec nowrite progbits
%endif
