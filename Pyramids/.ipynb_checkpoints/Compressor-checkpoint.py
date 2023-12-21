class Compressor():
    
    def __init__(self):
        pass
    
    def to_pyramid(self, inp):
        '''
        :param inp: a sring whose length is a power of 4. 
        :returns: an array. This array is a right triangle (call it 2D pyramid), 
                  where the vertex is the end of the original string. The steps of the 
                  pyramid are the subsequent elements. The lengths of the steps including 
                  the top are 1, 3, 5, 7, etc.
        '''
        arr = []
        inp = inp[::-1]
        lim = int((len(inp)) ** 0.5)
        
        for i in range(lim):
            k = 2 * i + 1
            arr.append(list(inp[:k]))
            inp = inp[k:]
        
        return arr
    
    def to_parts(self, pyramid):
        '''
        :param pyramid: the pyramid, created by the function to_pyramid.
        :returns: an array. This array contains part of the initial pyramid with 4 elements each. 
                  Every part represent "subpyramid" like in the description pyramids.txt.
        '''
        parts = []
        for i in range(0, len(pyramid), 2):
            for j in range(0, len(pyramid[i]), 4):
                odd = pyramid[i][j] + pyramid[i + 1][j] + pyramid[i + 1][j + 1] + pyramid[i + 1][j + 2]
                parts.append(odd)
                try:
                    k = j + 2
                    even = pyramid[i][k - 1] + pyramid[i][k] + pyramid[i][k + 1] + pyramid[i + 1][k + 1]
                    parts.append(even)
                except:
                    pass

        return parts
                
    def checker(self, parts, inp):
        '''
        :param parts: the array, created by the function to_parts.
        :param inp: a sring whose length is a power of 4. 
        :returns: a string. If all elements in each part ("subpyramid") are identical - this string 
                  represent compressed pyramid (subpyramid size 4 -> 1 ). 
                  If not all elements in each part are identical - this string equals to inial one (inp).
        '''
        check = set([len(set(elem)) for elem in parts])
    
        if check == {1}:
            res = ''.join([elem[0] for elem in parts[::-1]])
        else:
            res = inp
        
        return res
            
    def forward(self, inp):
        '''
        :param inp: a sring whose length is a power of 4. 
        :returns: a string. If inp cannot be compressed - returns inp. 
                  If inp can be compressed - compress this string to minimum size.
        '''
        if len(inp) == 1:
            return inp 
        elif len(inp) == 4 and len(set(inp)) != 1:
            return inp
        
        pyramid = self.to_pyramid(inp)
        parts = self.to_parts(pyramid)
        out = self.checker(parts, inp)
        
        if out == inp:
            return inp
        else:
            return self.forward(out)
        
    def compress(self, input_name):
        '''
        :param input_name: a name of the input file ("input.txt") in the same folder with uncompressed pyramid 
                           (1D string with length equals a power of 4).
        :returns: output file ("output.txt") with compressed pyramid (1D string).
        '''
        with open(input_name, 'r') as input_file:
            inp = input_file.read()
        input_file.close()
        
        compressed_pyramid = self.forward(inp)
        
        output_file = open('output.txt', 'w+')
        output_file.write(compressed_pyramid)
        output_file.close()