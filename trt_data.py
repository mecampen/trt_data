from matplotlib import pyplot as plt
import numpy as np

class TrtData:
    def __init__(self):
        self.data = [[], []]
        self.metadata = ""

    def read(self, path, line_skip=7):
        """reads a .trt-file and stores data in python array in TrtData.data

        Args:
            path (string): Path to the .trt file that should be stored
            line_skip (int): number of lines on top of file that should be skipped by the parser
        """
        line_skip_count = line_skip
        row_index = 0
        with open(path) as file:
            for row in file:
                #ignore number of lines specified in line_skip
                if line_skip_count == 0:
                    #replace all commas with dots so python understands
                    row = row.replace(',', '.')

                    #store each column in respective array
                    first, second = row.split(';')
                    self.data[0].append(float(first))
                    self.data[1].append(float(second))
                else:
                    line_skip_count -= 1
    def norm(self, maximum):
        values = np.array(self.data[1])
        self.data[1] = values/maximum

    def zoom(self, minBorder, maxBorder):
        minIndex = None
        maxIndex = None
        for (index, xval) in enumerate(self.data[0]):
            if minIndex is not None and maxIndex is not None:
                break
            if minIndex is None and xval>minBorder:
                minIndex = index
            if maxIndex is None and xval>maxBorder:
                maxIndex = index
        print(maxIndex)
        print(minIndex)
        self.data[0] = self.data[0][minIndex:maxIndex]
        self.data[1] = self.data[1][minIndex:maxIndex]

    def plot(self):
        X = self.data[0]
        Y = self.data[1]
        plt.plot(X, Y)
        plt.legend(["gemessene Intensität"])
        plt.xlabel("Wellenlänge [nm]")
        plt.ylabel("relative Zählrate")
        plt.show()

if __name__ == '__main__':
    trt_data = TrtData()
    trt_data.read("example.trt")
    trt_data.norm(maximum=8854)
    trt_data.zoom(minBorder=510, maxBorder=550)
    trt_data.plot()
    #print(len(trt_data.data))
    #print(len(trt_data.data[0]))
    #print(len(trt_data.data[1]))
    #print(trt_data.data[0])
    #print(trt_data.data[1])