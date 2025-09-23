Consider this code
```c
typedef struct {
uint8_t a;
uint8_t b;
uint32_t c;
} my_struct_t;
```
- On a 32 bit machine, the processor would align each byte of an address that is a multiple of 4
	- So that the last two address bits can be omitted
	- The architecture reads out 4 bytes at a time, so memory is aligned to 4 bytes
- Thus the two 8-bit integers a and b are placed in the same 4 byte word with 2 bytes of padding
- Without this padding, the CPU must perform two memory reads to access the `c` variable
- However, the `#pragma pack(1)` directive will force the memory to be packed tight with no padding

For class #embedded