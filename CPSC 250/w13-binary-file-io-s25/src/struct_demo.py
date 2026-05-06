import struct

#difference between integer and short (less bytes)
x = struct.pack('iii',3,5,7)
print("three integers = ",len(x), x)
y = struct.pack('hhh',14,7,1)
print("three shorts = ",len(y), y)

#difference between endian representations
# big endian uses greater than ">" symbol
y = struct.pack('>hhh',14,7,1)
print("big endian = ",len(y), y)
# little endian uses less than "<" symbol
y = struct.pack('<hhh',14,7,1)
print("little endian = ",len(y), y)

#lots of mixed values
z = struct.pack('ihiilih',14,13,19,5,7,10,9)
print("lots of mixed values = ",len(z), z)

#show unpacking
x_unpacked = struct.unpack('iii', x)
print ("x_unpacked = ", x_unpacked)

#show sizes
three_int_size = struct.calcsize('iii')
print("three integers is size", three_int_size, "bytes")
print("one_short_size = ", struct.calcsize('h'), "bytes")

#so, remember that the format must be correct when unpacking.
# what if we try to unpack x (three ints = 12 bytes) as 6 shorts?
wrong_unpack = struct.unpack('hhhhhh',x)
print("three integers (3,5,7) as 6 shorts = ", wrong_unpack)

#Another demo with packing and unpacking incorrectly
q = struct.pack('ii',2147483647,8761)
print("q (2147483647, 8761) = ",q)
wrong_unpack = struct.unpack('hhhh',q)
print("q unpacked as three shorts = ", wrong_unpack)

#this will generate an error, because the byte string size
# won't match what is specified by the format string
#uncomment this for an error
#error = struct.unpack('h',q)
