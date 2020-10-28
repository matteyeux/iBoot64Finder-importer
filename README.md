# iBoot64Finder-importer

Binja plugin to import [iBoot64Finder](https://github.com/haiyuidesu/iBoot64Finder) content

## Usage

Run iBoot64Finder and redirect output to a file :
```
λ ~/Desktop » iBoot64Finder -f SecureROM.8030.bin > securerom.txt
λ ~/Desktop » cat securerom.txt 
[main]: starting..
[main]: detected iBoot-4479.0.0.100.4!
[main]: base_addr = 0x100000000
[main]: PACed bootloader detected!
[locate_func]: _uart_init = 0x100002bec
[locate_func]: _image_load = 0x100001ca0
[locate_func]: _image4_load = 0x1000059dc
[locate_func]: _Img4DecodeInit = 0x100013d30
[locate_func]: _image_load_file = 0x10000af0c
[locate_func]: _image4_get_partial = 0x100004f28
[locate_func]: _Img4DecodeGetPayload = 0x100013260
[locate_func]: _image_create_from_memory = 0x10000b060
[locate_func]: _Img4DecodeEvaluateDictionaryProperties = 0x100013c14
[locate_func]: _Img4DecodeGetPropertyBoolean = 0x1000138ac
[locate_func]: _Img4DecodeGetPropertyData = 0x100013928
[locate_func]: _Img4DecodeManifestExists = 0x100013530
[locate_func]: _platform_quiesce_hardware = 0x100008aa8
[locate_func]: _platform_get_nonce = 0x1000077bc
[locate_func]: _platform_disable_keys = 0x1000073a8
[locate_func]: _DERImg4DecodeTagCompare = 0x1000028dc
[locate_func]: _DERParseSequence = 0x100015014
[locate_func]: _DERImg4Decode = 0x100012bd0
[locate_func]: _DERParseInteger = 0x100014dc4
[locate_func]: _DERParseBoolean = 0x100014db4
[locate_func]: _DERParseBitString = 0x100014d68
[locate_func]: _DERDecodeSeqInit = 0x100014ec0
[locate_func]: _DERDecodeSeqNext = 0x100014f7c
[locate_func]: _DERImg4DecodePayload = 0x100012e14
[locate_func]: _DERImg4DecodeRestoreInfo = 0x100012bd0
[locate_func]: _DERImg4DecodeFindInSequence = 0x100012a8c
[locate_func]: _load_sepos = 0x10000261c
[locate_func]: _usb_core_start = 0x10000e154
[locate_func]: _usb_core_init = 0x10000df9c
[locate_func]: _mmu_kvtop = 0x100000548
[locate_func]: _memalign = 0x100010114
[locate_func]: _calloc = 0x10000fe68
[locate_func]: _strlen = 0x100011bd0
[locate_func]: _malloc = 0x10000fc90
[locate_func]: _memcpy = 0x100011770
[locate_func]: _memset = 0x1000119a0
[locate_func]: _bzero = 0x100011920
[locate_func]: _free = 0x10000fef4
[locate_func]: _panic = 0x100008f90
[main]: done!
```


## Installation Instructions

### Darwin

Copy to `~/Library/Application Support/Binary Ninja/plugins/` or use Plugin Manager

### Windows

Copy to `%APPDATA%\Binary Ninja\plugins` or use Plugin Manager

### Linux

Copy to `~/.binaryninja/plugins/` or use Plugin Manager

