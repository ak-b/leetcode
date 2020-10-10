'''
Given a file and assume that you can only read the file using a given method read4, implement a method read to read n characters. Your method read may be called multiple times.

Method read4:

The API read4 reads 4 consecutive characters from the file, then writes those characters into the buffer array buf.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:

    Parameter:  char[] buf4
    Returns:    int

Note: buf4[] is destination not source, the results from read4 will be copied to buf4[]
'''
class Solution:
    def __init__(self):
        self.__local_buf = [0]*4
        self.__local_buf_offset = 0
        self.__local_buf_size = 0
        
    def __read_one(self, buf, index):
        if (self.__local_buf_size == 0 or
            self.__local_buf_offset == self.__local_buf_size):
            self.__local_buf_size = read4(self.__local_buf)
            self.__local_buf_offset = 0
        if self.__local_buf_size == 0:
            return False
        buf[index] = self.__local_buf[self.__local_buf_offset]
        self.__local_buf_offset += 1
        return True
        
    def read(self, buf: List[str], n: int) -> int:
        charsRead = 0
        while charsRead < n and self.__read_one(buf, charsRead):
            charsRead += 1
        return charsRead
