#!/usr/bin/env python3

import binascii
# from evtx_xml import EvtxXML

debug = False
# debug = True

def checksum_check(checksum, blob, name):
    calculated_checksum = binascii.crc32(blob)
    if checksum != calculated_checksum:
        print("[!] - %s Failed [%s] <> [%s]" % (name, checksum, calculated_checksum))
        return False
    return True

def val_to_int(s):
    total = 0
    p = 0
    for c in s:
        total += c * (256 ** p)
        p += 1
    return total

# class EvtxChunk:
#     def __init__(self, c):
#         self.first_record_number = val_to_int(c[8:16])
#         self.last_record_number = val_to_int(c[16:24])
#         self.first_record_identifier = val_to_int(c[24:32])
#         self.last_record_identifier = val_to_int(c[32:40])
#         checksum_check(val_to_int(c[124:128]), c[0:120] + c[128:512], "Chunk %d Checksum" % 3)
#         # print(self.first_record_number, self.last_record_number)
#         # print(self.first_record_identifier, self.last_record_identifier)
#         self.records = []
#         offset = 512
#         while c[offset:offset + 4] == b'\x2a\x2a\x00\x00':
#             record = EvtxRecord(c[offset:])
#             self.records.append(record)
#             offset += record.size
#         checksum_check(val_to_int(c[52:56]), c[512:offset], "Event Records Checksum")

# class EvtxRecord:
#     def __init__(self, c):
#         self.size = val_to_int(c[4:8])
#         self.c = c[:self.size]
#         self.id = val_to_int(c[8:16])
#         self.filetime = val_to_int(c[16:24])
#         self.xml = EvtxXML(c[24:])
#         if debug:
#             print("ID: %d" % self.id)
#             print("Filetime: %s" % self.filetime)
        

class EvtxHeader:
    def __init__(self, h):
        self.header_value_array = []
        self.h = h
        self.errors = []
        if len(h) != 4096:
            self.errors.append(["Invalid header length. [%d]" % len(h), True])
        self.signature = h[0:8]
        if self.signature != b'ElfFile\x00':
            self.errors.append(["Invalid File Header: [%s]" % self.signature, True])
        if len(self.errors) == 0:
            self.parse_headers()
            self.h = h

    def parse_headers(self):
        header_blob = self.h[:120]
        self.hread(8) # ElfFile
        self.first_chunk_number = self.hread(8)
        self.last_chunk_number = self.hread(8)
        self.next_record_identifier = self.hread(8)
        self.header_size = self.hread(4)
        self.minor_format_version = self.hread(2)
        self.major_format_version = self.hread(2)
        self.header_block_size = self.hread(2)
        self.number_of_chunks=self.hread(2)
        self.hread(76) #Unknown
        self.file_flags = self.hread(4)
        self.header_checksum = self.hread(4)
        self.checksum_valid = checksum_check(self.header_checksum, header_blob, "File Header Checksum")


    def hread(self, i):
        p = self.h[:i]
        self.h = self.h[i:]
        return val_to_int(p)

class EvtxFile:
    def __init__(self, filename):
        evtx = open(filename, 'rb').read()
        self.header = EvtxHeader(evtx[:4096])
# #         self.chunks = self.chunks_parse(evtx[4096:])

# #     def chunks_parse(self, d):
# #         chunks = []
# #         offset  = 0
# #         while d[offset:offset + 8] == b'ElfChnk\x00':
# #             if debug:
# #                 print("Chunk: %d" % len(chunks))
# #             chunks.append(EvtxChunk(d[offset:offset + 65536]))
# #             offset += 65536
# #         if len(chunks) != self.header.number_of_chunks:
# #             print("[!] - Unexpected Number of Chunks: [%d / %d]" % (len(chunks), self.header.number_of_chunks))


if __name__ == '__main__':
    e = EvtxFile('evtx-sample.evtx')