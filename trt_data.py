from matplotlib import pyplot as plt

class TrtData:
    def __init__(self):
        self.data = [[], []]
        self.metadata = ""

    def read(self, path, line_skip=7):
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

    def plot(self):
        X = trt_data.data[0]
        Y = trt_data.data[1]
        plt.plot(X, Y)
        plt.show()

if __name__ == '__main__':
    trt_data = TrtData()
    trt_data.read("example.trt")
    trt_data.plot()
    #print(len(trt_data.data))
    #print(len(trt_data.data[0]))
    #print(len(trt_data.data[1]))
    #print(trt_data.data[0])
    #print(trt_data.data[1])