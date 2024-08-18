from tkinter import *
import tkinter as tk
from tkinter import ttk, font
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
import math
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

global time
global signal


def loadfile(type):
    x = []
    y = []
    filename = filedialog.askopenfilename(title='select a file.')
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            if i >= 3:
                t, yt = line.split(' ')
                x.append(type(t))
                y.append(type(yt))
    return x, y


def loadfileneg():
    column1 = []
    column2 = []
    filename = filedialog.askopenfilename(title='select a file.')
    with open(filename, 'r') as f:
        for _ in range(3):
            next(f)
        data = [list(map(float, line.strip().split())) for line in f]
        column1, column2 = zip(*data)
    return column1, column2


def readfile(filename, type):
    list1 = []
    list2 = []
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            if i >= 3:
                # print(line.strip())
                x, y = line.split()
                list1.append(type(x))
                list2.append(type(y))
    return list1, list2


def readfiledirectly():
    x = []
    y = []
    filename = filedialog.askopenfilename(title='select a file.')
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            t, yt = line.split(' ')
            x.append(float(t))
            y.append(float(yt))
    return x, y


def readIDFTInputFIle(type):
    x = []
    y = []
    final_x = []
    final_y = []
    filename = filedialog.askopenfilename(title='select a file.')
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            if i >= 3:
                t, yt = line.strip().split(',')
                x.append(type(t))
                y.append(type(yt))
    for i in x:
        if i[-1] == 'f':
            i = i.rstrip(i[-1])
        final_x.append(round(float(i), 12))
    for i in y:
        if i[-1] == 'f':
            i = i.rstrip(i[-1])
        final_y.append(round(float(i), 12))
    return final_x, final_y


def writeIDFTFile(list1, list2, filename, length):
    list = zip(list1, list2)
    with open(filename, 'w') as f:
        f.write("0\n")
        f.write("0\n")
        f.write("%s\n" % length)
        for (list1, list2) in list:
            f.write("{0} {1}\n".format(list1, list2))
    f.close()
    print("File created successfully")


def writeDCTFile(filename, length, outputlist, indexlist):
    list = zip(indexlist, outputlist)
    with open(filename, 'w') as f:
        f.write("0\n")
        f.write("1\n")
        f.write("%s\n" % length)
        for (list1, list2) in list:
            f.write("{0} {1}\n".format(list1, list2))
    f.close()
    print("DCT File created successfully")


def writeToFile(list1, list2, filename):
    list = zip(list1, list2)
    with open(filename, 'w') as f:
        for (list1, list2) in list:
            f.write("{0} {1}\n".format(list1, list2))
    f.close()
    print("File created successfully")


def plot_task1(x, y, xlabel1, xlabel2, ylabel):
    plt.figure(figsize=(10, 10))
    plt.subplot(2, 2, 1)
    plt.xlabel(xlabel1)
    plt.ylabel(ylabel)
    plt.stem(x, y)

    plt.subplot(2, 2, 2)
    plt.xlabel(xlabel2)
    plt.ylabel(ylabel)
    plt.plot(x, y)
    plt.show()


def task1part1():
    x, y = loadfileneg()
    plot_task1(x, y, "DISCRETE SIGNAL", "CONTINOUS SIGNAL", "Amplitude")


def SignalSamplesAreEqual(file_name, indices, samples):
    expected_indices = []
    expected_samples = []
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L = line.strip()
            if len(L.split(' ')) == 2:
                L = line.split(' ')
                V1 = int(L[0])
                V2 = float(L[1])
                expected_indices.append(V1)
                expected_samples.append(V2)
                line = f.readline()
            else:
                break

    if len(expected_samples) != len(samples):
        print("Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(expected_samples)):
        if abs(samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Test case failed, your signal have different values from the expected one")
            return
    print("Test case passed successfully")


def task2part2():
    new_window = Toplevel(root)
    new_window.geometry('1500x800')
    new_window.title('Task 1')
    new_window['background'] = '#00868B'
    framee = Frame(new_window)
    framee.pack(side="top", expand=True, fill="both")

    tk.Label(new_window, text="Select Sin or Cos").place(x=20, y=40)
    combo = ttk.Combobox(new_window, values=["Sin", "Cos"])
    combo.pack()
    combo.place(x=180, y=40)
    combo.current(0)
    selected_choice = combo.get()

    tk.Label(new_window, text="Amplitude").place(x=20, y=80)
    amp_entry = tk.Entry(new_window, width=30)
    amp_entry.pack()
    amp_entry.place(x=180, y=80)
    # amplitude = amp_entry.get()

    tk.Label(new_window, text="Phase Shift").place(x=20, y=120)
    phase_entry = tk.Entry(new_window, width=30)
    phase_entry.pack()
    phase_entry.place(x=180, y=120)
    # phase_shift = phase_entry.get()

    tk.Label(new_window, text="Analog Frequency").place(x=20, y=160)
    ana_freq = tk.Entry(new_window, width=30)
    ana_freq.pack()
    ana_freq.place(x=180, y=160)
    # analog_frequency = ana_freq.get()

    tk.Label(new_window, text="Sampling Frequency").place(x=20, y=200)
    samp_freq = tk.Entry(new_window, width=30)
    samp_freq.pack()
    samp_freq.place(x=180, y=200)

    # sampling_frequency = samp_freq.get()

    def generate_signal():
        amplitude = int(amp_entry.get())
        phase_shift = float(phase_entry.get())
        analog_frequency = int(ana_freq.get())
        sampling_frequency = int(samp_freq.get())
        # print(amplitude,phase_shift,analog_frequency,sampling_frequency)
        if (sampling_frequency <= 0):
            time = np.arange(0, 1, 1 / 2 * analog_frequency)

        time = np.arange(0, 1, 1 / sampling_frequency)
        if (sampling_frequency >= (2 * analog_frequency)):
            if (selected_choice == 'Sin'):
                signal = amplitude * np.sin(2 * np.pi * analog_frequency * time + phase_shift)
            elif (selected_choice == 'Cos'):
                signal = amplitude * np.cos(2 * np.pi * analog_frequency * time + phase_shift)
            else:
                raise ValueError("Invalid signal type!")

        figure1 = plt.Figure(figsize=(7, 6), dpi=100)
        figure1Canvas = FigureCanvasTkAgg(figure1, framee)
        NavigationToolbar2Tk(figure1Canvas, framee)
        axes = figure1.add_subplot(111)
        axes.plot(time, signal, linewidth=3)
        figure1Canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
        SignalSamplesAreEqual(file_name="SinOutput.txt", samples=signal)

    b = tk.Button(new_window, text="generate", command=generate_signal)
    b.pack()
    b.place(x=200, y=250)

    new_window.mainloop()


def plotx(xold, xnew, y, xlabel1, xlabel2, ylabel):
    plt.figure(figsize=(10, 10))
    plt.subplot(2, 2, 1)
    plt.xlabel(xlabel1)
    plt.ylabel(ylabel)
    plt.plot(xold, y)

    plt.subplot(2, 2, 2)
    plt.xlabel(xlabel2)
    plt.ylabel(ylabel)
    plt.plot(xnew, y)
    plt.show()


def task1():
    task1_window = Toplevel(root)
    task1_window.geometry('300x180')
    task1_window.title('Task 1')
    task1_window['background'] = '#00868B'

    tk.Button(task1_window, text="Task 1 Part 1", font=label_font, padx=5, pady=5, width=25, background='#EEA2AD',
              activebackground='yellow', command=task1part1).place(x=50, y=15)

    tk.Button(task1_window, text="Task 1 Part 2", font=label_font, padx=5, pady=5, width=25, background='#EEA2AD',
              activebackground='yellow', command=task2part2).place(x=50, y=75)

    task1_window.mainloop()


def task2():
    task2_window = Toplevel(root)
    task2_window.geometry('650x500')
    task2_window.title("Task 2")
    task2_window['background'] = '#00868B'

    def add():
        x1 = []
        x2 = []
        y1 = []
        y2 = []
        addition = []

        file1name = filedialog.askopenfilename(title='select first file.')
        with open(file1name, 'r') as f:
            for i, line in enumerate(f):
                if i >= 3:
                    index1, index2 = line.split()
                    x1.append(int(index1))
                    y1.append(int(index2))

        file2name = filedialog.askopenfilename(title='select second file.')
        with open(file2name, 'r') as f:
            for i, line in enumerate(f):
                if i >= 3:
                    t, yt = line.split()
                    x2.append(int(t))
                    y2.append(int(yt))

        addition = abs(np.add(y1, y2))
        print(addition)
        # plot 1:
        plt.figure(figsize=(20, 10))
        plt.subplot(1, 3, 1)
        plt.title("original signal 1")
        plt.plot(x1, y1)
        # plot 2:
        plt.subplot(1, 3, 2)
        plt.title("original signal 2")
        plt.plot(x2, y2)

        plt.subplot(1, 3, 3)
        plt.title("result signal")
        plt.plot(x1, addition)

        plt.show()

    def subtract():
        x1 = []
        x2 = []
        y1 = []
        y2 = []
        subtraction = []

        file1name = filedialog.askopenfilename(title='select first file.')
        with open(file1name, 'r') as f:
            for i, line in enumerate(f):
                if i >= 3:
                    index1, index2 = line.split()
                    x1.append(int(index1))
                    y1.append(int(index2))

        file2name = filedialog.askopenfilename(title='select second file.')
        with open(file2name, 'r') as f:
            for i, line in enumerate(f):
                if i >= 3:
                    t, yt = line.split()
                    x2.append(int(t))
                    y2.append(int(yt))

        subtraction = abs(np.subtract(y1, y2))
        print(subtraction)
        # plot 1:
        plt.figure(figsize=(20, 10))
        plt.subplot(1, 3, 1)
        plt.title("original signal 1")
        plt.plot(x1, y1)
        # plot 2:
        plt.subplot(1, 3, 2)
        plt.title("original signal 2")
        plt.plot(x2, y2)

        plt.subplot(1, 3, 3)
        plt.title("result signal")
        plt.plot(x1, subtraction)

        plt.show()

    def multiply():
        x = []
        y = []
        cons = int(multi_entry.get())
        filename = filedialog.askopenfilename(title='select file.')
        with open(filename, 'r') as f:
            for i, line in enumerate(f):
                if i >= 3:
                    index1, index2 = line.split()
                    x.append(int(index1))
                    y.append(int(index2))

        res = [i * cons for i in y]
        print(res)
        plt.figure(figsize=(20, 10))
        plt.subplot(1, 2, 1)
        plt.title("original signal")
        plt.plot(x, y)

        plt.subplot(1, 2, 2)
        plt.title("new signal")
        plt.plot(x, res)

        plt.show()

    def square():
        x = []
        y = []
        res = []
        filename = filedialog.askopenfilename(title='select first file.')
        with open(filename, 'r') as f:
            for i, line in enumerate(f):
                if i >= 3:
                    index1, index2 = line.split()
                    x.append(int(index1))
                    y.append(int(index2))

        for i in range(0, len(y)):
            res.append(np.square(y[i]))

        print(res)
        plt.figure(figsize=(20, 10))
        plt.subplot(1, 2, 1)
        plt.title("original signal")
        plt.plot(x, y)

        plt.subplot(1, 2, 2)
        plt.title("new signal")
        plt.plot(x, res)

        plt.show()

    def shift():
        shifting_value = int(shift_entry.get())
        x = []
        y = []
        res = []
        filename = filedialog.askopenfilename(title='select first file.')
        with open(filename, 'r') as f:
            for i, line in enumerate(f):
                if i >= 3:
                    index1, index2 = line.split()
                    x.append(int(index1))
                    y.append(int(index2))

        for i in range(0, len(x)):
            res.append(x[i] - shifting_value)
        print(res)
        plt.figure(figsize=(20, 10))
        plt.subplot(1, 2, 1)
        plt.title("original signal")
        plt.plot(x, y)

        plt.subplot(1, 2, 2)
        plt.title("new signal")
        plt.plot(res, y)

        plt.show()

    def normalize():
        a = int(a_entry.get())
        b = int(b_entry.get())
        x = []
        y = []
        res = []
        filename = filedialog.askopenfilename(title='select first file.')
        with open(filename, 'r') as f:
            for i, line in enumerate(f):
                if i >= 3:
                    index1, index2 = line.split()
                    x.append(int(index1))
                    y.append(int(index2))
        mini = min(x)
        maxi = max(y)

        for i in range(0, len(y)):
            yout = ((x[i] - mini) / (maxi - mini)) * (b - a) + a
            res.append(yout)
        print(res)

        plt.figure(figsize=(20, 10))
        plt.subplot(1, 2, 1)
        plt.title("original signal")
        plt.plot(x, y)

        plt.subplot(1, 2, 2)
        plt.title("new signal")
        plt.plot(x, res)

        plt.show()

    def accumulation():
        x = []
        y = []
        res = []
        filename = filedialog.askopenfilename(title='select first file.')
        with open(filename, 'r') as f:
            for i, line in enumerate(f):
                if i >= 3:
                    index1, index2 = line.split()
                    x.append(int(index1))
                    y.append(int(index2))
        arr = np.array(y)
        rescum = np.cumsum(arr)
        res = rescum.tolist()
        print(res)

        plt.figure(figsize=(20, 10))
        plt.subplot(1, 2, 1)
        plt.title("original signal")
        plt.plot(x, y)

        plt.subplot(1, 2, 2)
        plt.title("new signal")
        plt.plot(x, res)

        plt.show()

    # tk.Label(task2_window,text="Enter the number of signals",font=label_font).place(x=30,y=25)
    # add_entry = tk.Entry(task2_window,width=10)
    # add_entry.pack()
    # add_entry.place(x=230,y=25)
    tk.Button(task2_window, text="Add signals", font=label_font, padx=5, pady=5, width=25, background='#EEA2AD',
              activebackground='yellow', command=add).place(x=350, y=15)

    tk.Button(task2_window, text="Subtract signals", font=label_font, padx=5, pady=5, width=25, background='#EEA2AD',
              activebackground='yellow', command=subtract).place(x=350, y=75)

    tk.Label(task2_window, text="Enter Constant Value", font=label_font).place(x=30, y=150)
    multi_entry = tk.Entry(task2_window, width=20)
    multi_entry.pack()
    multi_entry.place(x=180, y=150)
    tk.Button(task2_window, text="Multiply signal by constant", font=label_font, padx=5, pady=5, width=25,
              background='#EEA2AD', activebackground='yellow', command=multiply).place(x=350, y=135)

    tk.Button(task2_window, text="Square signal", font=label_font, padx=5, pady=5, width=25, background='#EEA2AD',
              activebackground='yellow', command=square).place(x=350, y=195)

    tk.Label(task2_window, text="Enter shifting Value", font=label_font).place(x=30, y=265)
    shift_entry = tk.Entry(task2_window, width=20)
    shift_entry.pack()
    shift_entry.place(x=180, y=265)
    tk.Button(task2_window, text="Shift a signal", font=label_font, padx=5, pady=5, width=25, background='#EEA2AD',
              activebackground='yellow', command=shift).place(x=350, y=255)

    tk.Label(task2_window, text="Range from", font=label_font).place(x=80, y=325)
    a_entry = tk.Entry(task2_window, width=5)
    a_entry.pack()
    a_entry.place(x=165, y=325)
    tk.Label(task2_window, text="To", font=label_font).place(x=205, y=325)
    b_entry = tk.Entry(task2_window, width=5)
    b_entry.pack()
    b_entry.place(x=235, y=325)
    tk.Button(task2_window, text="Normalize a signal", font=label_font, padx=5, pady=5, width=25, background='#EEA2AD',
              activebackground='yellow', command=normalize).place(x=350, y=315)

    tk.Button(task2_window, text="Accumulation of a signal", font=label_font, padx=5, pady=5, width=25,
              background='#EEA2AD', activebackground='yellow', command=accumulation).place(x=350, y=375)

    task2_window.mainloop()


def QuantizationTest1(file_name, Your_EncodedValues, Your_QuantizedValues):
    expectedEncodedValues = []
    expectedQuantizedValues = []
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L = line.strip()
            if len(L.split(' ')) == 2:
                L = line.split(' ')
                V2 = str(L[0])
                V3 = float(L[1])
                expectedEncodedValues.append(V2)
                expectedQuantizedValues.append(V3)
                line = f.readline()
            else:
                break
    if ((len(Your_EncodedValues) != len(expectedEncodedValues)) or (
            len(Your_QuantizedValues) != len(expectedQuantizedValues))):
        print("QuantizationTest1 Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_EncodedValues)):
        if (Your_EncodedValues[i] != expectedEncodedValues[i]):
            print(
                "QuantizationTest1 Test case failed, your EncodedValues have different EncodedValues from the expected one")
            return
    for i in range(len(expectedQuantizedValues)):
        if abs(Your_QuantizedValues[i] - expectedQuantizedValues[i]) < 0.01:
            continue
        else:
            print(
                "QuantizationTest1 Test case failed, your QuantizedValues have different values from the expected one")
            return
    print("QuantizationTest1 Test case passed successfully")


def QuantizationTest2(file_name, Your_IntervalIndices, Your_EncodedValues, Your_QuantizedValues, Your_SampledError):
    expectedIntervalIndices = []
    expectedEncodedValues = []
    expectedQuantizedValues = []
    expectedSampledError = []
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L = line.strip()
            if len(L.split(' ')) == 4:
                L = line.split(' ')
                V1 = int(L[0])
                V2 = str(L[1])
                V3 = float(L[2])
                V4 = float(L[3])
                expectedIntervalIndices.append(V1)
                expectedEncodedValues.append(V2)
                expectedQuantizedValues.append(V3)
                expectedSampledError.append(V4)
                line = f.readline()
            else:
                break
    if (len(Your_IntervalIndices) != len(expectedIntervalIndices)
            or len(Your_EncodedValues) != len(expectedEncodedValues)
            or len(Your_QuantizedValues) != len(expectedQuantizedValues)
            or len(Your_SampledError) != len(expectedSampledError)):
        print("QuantizationTest2 Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_IntervalIndices)):
        if (Your_IntervalIndices[i] != expectedIntervalIndices[i]):
            print("QuantizationTest2 Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(Your_EncodedValues)):
        if (Your_EncodedValues[i] != expectedEncodedValues[i]):
            print(
                "QuantizationTest2 Test case failed, your EncodedValues have different EncodedValues from the expected one")
            return

    for i in range(len(expectedQuantizedValues)):
        if abs(Your_QuantizedValues[i] - expectedQuantizedValues[i]) < 0.01:
            continue
        else:
            print(
                "QuantizationTest2 Test case failed, your QuantizedValues have different values from the expected one")
            return
    for i in range(len(expectedSampledError)):
        if abs(Your_SampledError[i] - expectedSampledError[i]) < 0.01:
            continue
        else:
            print("QuantizationTest2 Test case failed, your SampledError have different values from the expected one")
            return
    print("QuantizationTest2 Test case passed successfully")


def task3():
    task3_window = Toplevel(root)
    task3_window.title("Task3")
    task3_window.geometry("400x400")
    task3_window['background'] = '#00868B'

    def Quantize():
        data = []
        selected_choice = combo.get()
        selected_number = int(num.get())

        filename = filedialog.askopenfilename(title='select a file.')
        with open(filename, 'r') as f:
            for i, line in enumerate(f):
                if i >= 3:
                    t, yt = line.split(' ')
                    data.append(float(yt))

        mini = min(data)
        maxi = max(data)
        numOfBits = 0
        numOfLevels = 0

        if (selected_choice == 'Number of Levels'):
            numOfBits = int(np.log2(selected_number))
            numOfLevels = selected_number
        elif (selected_choice == 'Number of Bits'):
            numOfBits = selected_number
            numOfLevels = pow(2, selected_number)

        print("number of bits = ", numOfBits)
        print("number of levels = ", numOfLevels)

        intervals = []
        delta = (maxi - mini) / numOfLevels
        index = 1
        print("min = ", mini, ", max = ", maxi, ", DELTA = ", delta)
        for i in range(0, numOfLevels):
            intervals.append([i + 1, round(mini, 2), round(mini + delta, 2)])
            mini += delta

        print("intervals list = ", intervals)

        mid_points = []
        for i in intervals:
            # print(i[0],i[1])
            mid_point = round((i[1] + i[2]) / 2, 3)
            mid_points.append(mid_point)
        print("mid_points list = ", mid_points)

        list = []
        for i in data:
            # print("current value = ",i)
            for interval in intervals:
                if (interval[1] <= i <= interval[2]):
                    list.append(interval[0])
                    break;
        print("list = ", list)

        quantized_list = []
        for i in list:
            index = i - 1
            q = mid_points[index]
            quantized_list.append(q)
        print("quantized_list = ", quantized_list)

        encoded_list = []
        for i in list:
            encoded_list.append(bin(i - 1)[2:].zfill(numOfBits))
        print("encoded list = ", encoded_list)

        if (selected_choice == 'Number of Levels'):
            sampling_error = []
            sampling_error = np.subtract(quantized_list, data)
            print("sampling_error = ", sampling_error)
            QuantizationTest2("Quan2_Out.txt", list, encoded_list, quantized_list, sampling_error)
        else:
            QuantizationTest1('Quan1_Out.txt', encoded_list, quantized_list)

    tk.Label(task3_window, text="Select ", font=label_font).place(x=40, y=40)
    combo = ttk.Combobox(task3_window, values=["Number of Bits", "Number of Levels"], font=label_font)
    combo.pack()
    combo.place(x=100, y=40)
    combo.current(0)
    tk.Label(task3_window, text="Enter the Number ", font=label_font).place(x=40, y=80)
    num = tk.Entry(task3_window, width=5)
    num.pack()
    num.place(x=175, y=80)

    b = tk.Button(task3_window, text="Quantize", background='#EEA2AD', activebackground='yellow', font=label_font,
                  command=Quantize)
    b.pack()
    b.place(x=150, y=200)

    task3_window.mainloop()


def SignalComapreAmplitude(SignalInput=[], SignalOutput=[]):
    if len(SignalInput) != len(SignalInput):
        print("case1")
        return False
    else:
        for i in range(len(SignalInput)):
            if abs(SignalInput[i] - SignalOutput[i]) > 0.001:
                print("case2")
                return False
            elif SignalInput[i] != SignalOutput[i]:
                print("case3")
                return False
        return True


def SignalComaprePhaseShift(SignalInput=[], SignalOutput=[]):
    if len(SignalInput) != len(SignalInput):
        return False
    else:
        for i in range(len(SignalInput)):
            A = round(SignalInput[i])
            B = round(SignalOutput[i])
            if abs(A - B) > 0.0001:
                return False
            elif A != B:
                return False
        return True


def plotstem(x, amp, phase, xlabel, ylabel1, ylabel2, type):
    plt.figure(figsize=(10, 10))
    plt.subplot(2, 2, 1)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel1)
    plt.stem(x, amp)

    plt.subplot(2, 2, 2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel2)
    plt.stem(x, phase)
    plt.show()


def plot(x, amp, phase, xlabel, ylabel1, ylabel2):
    plt.figure(figsize=(10, 4))
    plt.subplot(2, 2, 1)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel1)
    plt.plot(x, amp)

    plt.subplot(2, 2, 2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel2)
    plt.plot(x, phase)
    plt.show()


def plot_old_and_new(x1, x2, y1, y2, xlabel1, ylabel1, xlabel2, ylabel2):
    plt.figure(figsize=(10, 10))
    plt.subplot(2, 2, 1)
    plt.xlabel(xlabel1)
    plt.ylabel(ylabel1)
    plt.plot(x1, y1)

    plt.subplot(2, 2, 2)
    plt.xlabel(xlabel2)
    plt.ylabel(ylabel2)
    plt.plot(x2, y2)
    plt.show()


def dft(data):
    N = len(data)
    x_k = []
    sum = 0
    for k in range(0, N):
        for n in range(0, N):
            sum += data[n] * np.exp((-np.pi * 2j * k * n) / N)
        x_k.append(sum)
        sum = 0
    return x_k


def idft(amplitude, phase_shift):
    real = []
    imagine = []
    output = []
    for i in range(len(amplitude)):
        real.append(amplitude[i] * np.cos(phase_shift[i]))
        imagine.append(amplitude[i] * np.sin(phase_shift[i]))
    N = len(amplitude)
    sum = 0
    x_n = []
    for i in range(N):
        x_n.append(complex(real[i], imagine[i]))
    # print("x[n] = ",x_n)
    for n in range(0, N):
        for k in range(0, N):
            sum += (x_n[k] * np.exp((np.pi * 2j * k * n) / N)) / N
        output.append(sum)
        sum = 0
    final_IDFT = []
    final_IDFT_DC = []
    index = []
    k = 1
    for i in output:
        # print(round(i.real,0))
        index.append(k)
        final_IDFT.append(round(i.real))
        final_IDFT_DC.append(round(i.real, 3))
        k += 1

    return final_IDFT, final_IDFT_DC, index


def task4():
    task4_window = Toplevel(root)
    task4_window.title("Task4")
    task4_window.geometry("400x400")
    task4_window['background'] = '#00868B'

    x_frequency = []

    def DFT_OR_IDFT():
        selected_choice = combo.get()
        # //////////////////////////////////  DFT  ///////////////////////////////////
        if selected_choice == 'DFT':
            x, data = loadfile(float)
            Amplitude = []
            phase = []
            amp = []
            o_phase = []
            sampling_frequency = int(freq.get())
            Ts = 1 / sampling_frequency
            N = len(data)
            x_k = dft(data)
            for i in x_k:
                Amplitude.append(round(np.sqrt((i.real) ** 2 + (i.imag) ** 2), 12))
                phase.append(float(math.atan2(i.imag, i.real)))
            out_amplitude, out_phase = readfile('Output_Signal_DFT_A,Phase.txt', str)

            for i in out_amplitude:
                if i[-1] == 'f':
                    i = i.rstrip(i[-1])
                amp.append(round(float(i), 12))
            for i in out_phase:
                if i[-1] == 'f':
                    i = i.rstrip(i[-1])
                o_phase.append(round(float(i), 12))

            print(SignalComapreAmplitude(Amplitude, amp))
            print(SignalComaprePhaseShift(phase, o_phase))

            writeToFile(amp, phase, "fileToModify")

            Omiga = (2 / np.pi) / (N * Ts)
            o = Omiga
            for i in range(0, N):
                x_frequency.append(round(o, 3))
                o += Omiga

            plotstem(x_frequency, amp, o_phase, "Frequency", "Amplitude", "Phase Shift")

        # ////////////////////////////////  IDFT  ////////////////////////////////////
        elif selected_choice == 'IDFT':
            amplitude, phase_shift = readIDFTInputFIle(str)
            print(amplitude)
            print(phase_shift)
            N = len(amplitude)
            final_IDFT, f_idft_for_DC, index = idft(amplitude, phase_shift)
            x, y = readfile("Output_Signal_IDFT.txt", int)
            print(SignalComapreAmplitude(final_IDFT, y))
            writeIDFTFile(index, final_IDFT, "IDFT_output_File", N)

    def mod():
        Index = int(index.get())
        new_amp = float(ampli.get())
        new_phase = float(ph.get())
        list1, list2 = readfiledirectly()
        list1[Index] = new_amp
        list2[Index] = new_phase
        writeToFile(list1, list2, "new_Amplitude_PhaseShift_File")

    # //////////////////////////////  GUI   ////////////////////////////////
    apply_button = tk.Button(task4_window, text="Apply ", font=label_font, activebackground='yellow',
                             background='#EEA2AD',
                             command=DFT_OR_IDFT)
    apply_button.pack()
    apply_button.place(x=40, y=40)

    combo = ttk.Combobox(task4_window, values=["DFT", "IDFT"], font=label_font)
    combo.pack()
    combo.place(x=100, y=40)
    combo.current(0)

    tk.Label(task4_window, text="Enter the Sampling frequency ", font=label_font).place(x=40, y=80)
    freq = tk.Entry(task4_window, width=5)
    freq.pack()
    freq.place(x=250, y=80)

    # Separator object
    separator = ttk.Separator(task4_window, orient='horizontal')
    separator.place(relx=0, rely=0.289, relwidth=2)

    tk.Label(task4_window, text="Index", font=label_font).place(x=40, y=125)
    index = tk.Entry(task4_window, width=5)
    index.pack()
    index.place(x=150, y=125)

    tk.Label(task4_window, text="Amplitude ", font=label_font).place(x=40, y=155)
    ampli = tk.Entry(task4_window, width=5)
    ampli.pack()
    ampli.place(x=150, y=155)

    mod_button = tk.Button(task4_window, text="Apply Modification", font=label_font, activebackground='yellow',
                           background='#EEA2AD', command=mod)
    mod_button.pack()
    mod_button.place(x=210, y=155)

    tk.Label(task4_window, text="Phase Shift ", font=label_font).place(x=40, y=185)
    ph = tk.Entry(task4_window, width=5)
    ph.pack()
    ph.place(x=150, y=185)

    task4_window.mainloop()


def SignalSamplesAreEqual(file_name, samples):
    """
    this function takes two inputs the file that has the expected results and your results.
    file_name : this parameter corresponds to the file path that has the expected output
    samples: this parameter corresponds to your results
    return: this function returns Test case passed successfully if your results is similar to the expected output.
    """
    expected_indices = []
    expected_samples = []
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L = line.strip()
            if len(L.split(' ')) == 2:
                L = line.split(' ')
                V1 = int(L[0])
                V2 = float(L[1])
                expected_indices.append(V1)
                expected_samples.append(V2)
                line = f.readline()
            else:
                break

    if len(expected_samples) != len(samples):
        print("Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(expected_samples)):
        if abs(samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Test case failed, your signal have different values from the expected one")
            return
    print("Test case passed successfully")


def task5():
    task5_window = Toplevel(root)
    task5_window.geometry('400x400')
    task5_window.title("Task 5")
    task5_window['background'] = "#00868B"

    def compute_DCT():
        m = int(mentry.get())
        x, data = loadfile(float)
        print("data = ", data)
        res = []
        indexlist = []
        sum = 0
        N = len(data)
        for k in range(0, N):
            for n in range(0, N):
                s = data[n] * np.cos((np.pi / (4 * N)) * (2 * n - 1) * (2 * k - 1))
                sum += s
            res.append(sum * np.sqrt(2 / N))
            sum = 0
            indexlist.append(k)
        # print("result = ", res)
        # print("indexlist = ",indexlist)
        print(SignalSamplesAreEqual("DCT_output.txt", res))
        removed = len(res) - m
        res = res[:-removed]
        indexlist = indexlist[:-removed]
        # print("res after removing unwanted values = ",res)
        writeDCTFile("DCT", m, res, indexlist)

    def remove_DC_component():
        x, data = loadfile(float)
        print(data)
        length = len(data)

        avg = sum(data) / length
        print("Average = ", avg)

        result = []
        for i in data:
            result.append(round(i - avg, 3))

        print("result= ", result)
        print(SignalSamplesAreEqual("DC_component_output.txt", result))

    # tk.Label(task5_window,text="",font=label_font).place(x= 170,y=100)
    mentry = tk.Entry(task5_window, width=5)
    mentry.pack()
    mentry.place(x=250, y=105)
    compute_button = tk.Button(task5_window, text="Compute DCT with m equal to", width=25, font=label_font,
                               background='#EEA2AD', activebackground='yellow', command=compute_DCT)
    compute_button.pack()
    compute_button.place(x=30, y=100)

    compute_button = tk.Button(task5_window, text="Remove DC Component", width=25, font=label_font,
                               background='#EEA2AD',
                               activebackground='yellow', command=remove_DC_component)
    compute_button.pack()
    compute_button.place(x=30, y=150)

    task5_window.mainloop()


def Shift_Fold_Signal(file_name, Your_indices, Your_samples):
    expected_indices = []
    expected_samples = []
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L = line.strip()
            if len(L.split(' ')) == 2:
                L = line.split(' ')
                V1 = int(L[0])
                V2 = float(L[1])
                expected_indices.append(V1)
                expected_samples.append(V2)
                line = f.readline()
            else:
                break
    print("Current Output Test file is: ")
    print(file_name)
    print("\n")
    if (len(expected_samples) != len(Your_samples)) and (len(expected_indices) != len(Your_indices)):
        print("Shift_Fold_Signal Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if (Your_indices[i] != expected_indices[i]):
            print("Shift_Fold_Signal Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Shift_Fold_Signal Test case failed, your signal have different values from the expected one")
            return
    print("Shift_Fold_Signal Test case passed successfully")


def DerivativeSignal():
    InputSignal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                   53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
                   78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    expectedOutput_first = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1]
    expectedOutput_second = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0]

    """
    Write your Code here:
    Start
    """

    FirstDrev = []
    SecondDrev = []
    ### 1st
    for i in range(1, len(InputSignal)):
        if i == 0:
            FirstDrev.append(InputSignal[i] - 0)
        else:
            FirstDrev.append(InputSignal[i] - InputSignal[i - 1])
    #### 2nd
    for i in range(2, len(InputSignal)):
        if i == 0:
            SecondDrev.append(0 + InputSignal[i + 1] - (2 * InputSignal[i]))
        elif i == len(InputSignal) - 1:
            SecondDrev.append(InputSignal[i - 1] + (len(InputSignal) + 1) - (2 * InputSignal[i]))
        else:
            SecondDrev.append(InputSignal[i - 1] - (2 * InputSignal[i]) + InputSignal[i + 1])
    """
    End
    """

    """
    Testing your Code
    """
    if ((len(FirstDrev) != len(expectedOutput_first)) or (len(SecondDrev) != len(expectedOutput_second))):
        print("mismatch in length")
        return
    first = second = True
    for i in range(len(expectedOutput_first)):
        if abs(FirstDrev[i] - expectedOutput_first[i]) < 0.01:
            continue
        else:
            first = false
            print("1st derivative wrong")
            return
    for i in range(len(expectedOutput_second)):
        if abs(SecondDrev[i] - expectedOutput_second[i]) < 0.01:
            continue
        else:
            second = False
            print("2nd derivative wrong")
            return
    if (first and second):
        print("Derivative Test case passed successfully")
    else:
        print("Derivative Test case ailed")

    return InputSignal, FirstDrev, SecondDrev


def task6():
    task6_window = Toplevel(root)
    task6_window.geometry('400x400')
    task6_window.title("Task 6")
    task6_window['background'] = "#00868B"

    def remove_DC_Component():
        x, data = loadfile(float)
        x_k = dft(data)
        # print("x_k = ", x_k)
        Amplitude = []
        phase = []
        for i in x_k:
            Amplitude.append(round(np.sqrt((i.real) ** 2 + (i.imag) ** 2), 12))
            phase.append(float(math.atan2(i.imag, i.real)))
        Amplitude[0] = 0
        phase[0] = 0
        final_IDFT, final_IDFT_DC, index = idft(Amplitude, phase)
        print("final_IDFT = ", final_IDFT_DC)
        SignalSamplesAreEqual("DC_component_output.txt", final_IDFT_DC)

    def fold():
        x, data = loadfileneg()
        y = []
        for i in range(1, len(data) + 1):
            y.append(data[-i])
        plot(x, data, y, "x", "original signal", "folded signal")

    def delay_or_advance():
        x, data = loadfileneg()
        shifting_value = int(shiftEntry.get())
        res = []
        for i in range(0, len(x)):
            res.append(x[i] - shifting_value)
        # print(res)

        if shifting_value > 0:
            print(SignalSamplesAreEqual('output shifting by add 500.txt', res))
            plotx(x, res, data, "original signal", "advanced signal", "signal")
        elif shifting_value < 0:
            print(SignalSamplesAreEqual('output shifting by minus 500.txt', res))
            plotx(x, res, data, "original signal", "delayed signal", "signal")

    def delay_or_advance_folding_signal():
        x, data = loadfileneg()
        newy = []
        for i in range(1, len(data) + 1):
            newy.append(data[-i])
        da_value = int(daEntry.get())
        newx = []
        for i in range(0, len(x)):
            newx.append(x[i] + da_value)
        # print("new x = ",newx)
        # print("new y = ",newy)
        if da_value >= 0:
            print(Shift_Fold_Signal("Output_ShifFoldedby500.txt", newx, newy))
            plot_old_and_new(x, newy, data, newy, "original signal", "Amplitude", "advanced folded signal", "Amplitude")
        elif da_value < 0:
            print(Shift_Fold_Signal("Output_ShiftFoldedby-500.txt", newx, newy))
            plot_old_and_new(x, newy, data, newy, "original signal", "Amplitude", "delayed folded signal", "Amplitude")

    def smooth():
        window_size = int(windowSizeEntry.get())
        x, data = loadfileneg()
        moving_average_list = []
        i = 0
        while i < len(data) - window_size + 1:
            moving_average_list.append(round(np.sum(data[i:i + window_size]) / window_size))
            i += 1

        print("moving average list =", moving_average_list)
        if (window_size == 3):
            print(SignalSamplesAreEqual("OutMovAvgTest1.txt", moving_average_list))
        elif (window_size == 5):
            print(SignalSamplesAreEqual("OutMovAvgTest2.txt", moving_average_list))

    def sharpen():
        x, f, s = DerivativeSignal()

    ################################# GUI ##################################

    fold_button = tk.Button(task6_window, text="Fold a signal", width=25, font=label_font, background='#EEA2AD',
                            activebackground='yellow', command=fold)
    fold_button.pack()
    fold_button.place(x=90, y=20)

    shiftEntry = tk.Entry(task6_window, width=5)
    shiftEntry.pack()
    shiftEntry.place(x=310, y=65)
    shift_button = tk.Button(task6_window, text="delay or advance signal", width=25, font=label_font,
                             background='#EEA2AD',
                             activebackground='yellow', command=delay_or_advance)
    shift_button.pack()
    shift_button.place(x=90, y=60)

    daEntry = tk.Entry(task6_window, width=5)
    daEntry.pack()
    daEntry.place(x=310, y=105)
    da_button = tk.Button(task6_window, text="delay or advance folded signal", width=25, font=label_font,
                          background='#EEA2AD', activebackground='yellow', command=delay_or_advance_folding_signal)
    da_button.pack()
    da_button.place(x=90, y=100)

    windowSizeEntry = tk.Entry(task6_window, width=5)
    windowSizeEntry.pack()
    windowSizeEntry.place(x=310, y=145)
    smooth_button = tk.Button(task6_window, text="Compute moving average with window size = ", width=35,
                              font=label_font,
                              background='#EEA2AD', activebackground='yellow', command=smooth)
    smooth_button.pack()
    smooth_button.place(x=15, y=140)

    D_button = tk.Button(task6_window, text="Compute 1st and 2nd Derivative", width=25, font=label_font,
                         background='#EEA2AD',
                         activebackground='yellow', command=sharpen)
    D_button.pack()
    D_button.place(x=90, y=180)

    DC_button = tk.Button(task6_window, text="Remove_DC_Component", width=25, font=label_font, background='#EEA2AD',
                          activebackground='yellow', command=remove_DC_Component)
    DC_button.pack()
    DC_button.place(x=90, y=220)

    task6_window.mainloop()


def ConvTest(Your_indices, Your_samples):
    """
    Test inputs
    InputIndicesSignal1 =[-2, -1, 0, 1]
    InputSamplesSignal1 = [1, 2, 1, 1 ]

    InputIndicesSignal2=[0, 1, 2, 3, 4, 5 ]
    InputSamplesSignal2 = [ 1, -1, 0, 0, 1, 1 ]
    """

    expected_indices = [-2, -1, 0, 1, 2, 3, 4, 5, 6]
    expected_samples = [1, 1, -1, 0, 0, 3, 3, 2, 1]

    if (len(expected_samples) != len(Your_samples)) and (len(expected_indices) != len(Your_indices)):
        print("Conv Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if (Your_indices[i] != expected_indices[i]):
            print("Conv Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Conv Test case failed, your signal have different values from the expected one")
            return
    print("Conv Test case passed successfully")


def task7():
    task7_window = Toplevel(root)
    task7_window.title("Task 7 ")
    task7_window.geometry('300x150')
    task7_window['background'] = "#00868B"

    def Convolution():
        index1, x = loadfile(int)
        index2, h = loadfile(int)
        firstIndex = index1[0]
        indices = []
        M = len(x)
        N = len(h)
        L = M + N - 1
        y = [0] * L
        print("y: ", y)
        # Convolution
        for n in range(L):
            indices.append(firstIndex)
            mx = max(0, n - N + 1)
            mn = min(M, n + 1)
            print("range", (mx, mn))
            for k in range(mx, mn):
                y[n] += x[k] * h[n - k]
            firstIndex += 1
            print("Y[n] = ", y[n])
        print("indices = ", indices)
        print("convList = ", y)
        print(ConvTest(indices, y))

    ############################  GUI ####################
    C_button = tk.Button(task7_window, text="Convolve two Signals", width=25, font=label_font, background='#EEA2AD',
                         activebackground='yellow', command=Convolution)
    C_button.pack()
    C_button.place(x=60, y=50)
    task7_window.mainloop()


def Compare_Signals(file_name, Your_indices, Your_samples):
    expected_indices = []
    expected_samples = []
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L = line.strip()
            if len(L.split(' ')) == 2:
                L = line.split(' ')
                V1 = int(L[0])
                V2 = float(L[1])
                expected_indices.append(V1)
                expected_samples.append(V2)
                line = f.readline()
            else:
                break
    print("Current Output Test file is: ")
    print(file_name)
    print("\n")
    if (len(expected_samples) != len(Your_samples)) and (len(expected_indices) != len(Your_indices)):
        print("Shift_Fold_Signal Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if (Your_indices[i] != expected_indices[i]):
            print("Shift_Fold_Signal Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Correlation Test case failed, your signal have different values from the expected one")
            return
    print("Correlation Test case passed successfully")


def shift_left(lst, n):
    n = n % len(lst)
    return lst[n:] + lst[:n]


def sum_of_squared_numbers(input_list):
    summ = 0
    for i in input_list:
        s = (i ** 2)
        summ += s
    return summ


def task8():
    task8_window = Toplevel(root)
    task8_window.title("Task 8 ")
    task8_window.geometry('370x150')
    task8_window['background'] = "#00868B"

    def compute_corr():
        index1, x_n1 = loadfile(int)
        index2, x_n2 = loadfile(int)
        N = len(x_n1)
        listOfShiftedLists = []
        for i in range(N):
            shifted_list = shift_left(x_n2, i)
            listOfShiftedLists.append(shifted_list)
        print(listOfShiftedLists)
        r12List = []
        for i in listOfShiftedLists:
            summ = 0
            index = 0
            print("current i: ", i)
            for j in i:
                m = j * x_n1[index]
                summ += m
                index += 1
            r12List.append(summ / N)
        print("r12 :", r12List)
        s1 = sum_of_squared_numbers(x_n1)
        s2 = sum_of_squared_numbers(x_n2)
        p = np.sqrt(s1 * s2) * (1 / N)
        print("summation Of List 1:", s1)
        print("summation Of List 2:", s2)
        print("equation p:", p)
        normalized_cross_correlation = []
        for i in r12List:
            p12 = i / p
            normalized_cross_correlation.append(round(p12, 7))
        print("normalized_cross_correlation: ", normalized_cross_correlation)
        print(Compare_Signals("CorrOutput.txt", index1, normalized_cross_correlation))

    Comp_button = tk.Button(task8_window, text="Compute normalized cross correlation for 2 signals", width=40,
                            font=label_font, background='#EEA2AD',
                            activebackground='yellow', command=compute_corr)
    Comp_button.pack()
    Comp_button.place(x=20, y=50)

    task8_window.mainloop()


def append_zeros(lst, n):
    lst_of_zeros = []
    new_lst = []
    for i in range(n):
        lst_of_zeros.append(0)
    new_lst = lst + lst_of_zeros
    return new_lst


def ConvTest_practical(Your_indices, Your_samples):
    """
    Test inputs
    InputIndicesSignal1 =[-2, -1, 0, 1]
    InputSamplesSignal1 = [1, 2, 1, 1 ]

    InputIndicesSignal2=[0, 1, 2, 3, 4, 5 ]
    InputSamplesSignal2 = [ 1, -1, 0, 0, 1, 1 ]
    """

    expected_indices = [-2, -1, 0, 1, 2, 3, 4, 5, 6]
    expected_samples = [1, 1, -1, 0, 0, 3, 3, 2, 1]

    if (len(expected_samples) != len(Your_samples)) and (len(expected_indices) != len(Your_indices)):
        print("Conv Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if (Your_indices[i] != expected_indices[i]):
            print("Conv Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Conv Test case failed, your signal have different values from the expected one")
            return
    print("Conv Test case passed successfully")


def FastConvolution():
    x1, y1 = loadfile(int)
    x2, y2 = loadfile(int)
    index = x1[0]
    indices = []
    N1 = len(y1)
    N2 = len(y2)
    length_of_signal = N1 + N2 - 1
    for i in range(length_of_signal):
        indices.append(index)
        index += 1;
    Y1 = append_zeros(y1, length_of_signal - N1)
    Y2 = append_zeros(y2, length_of_signal - N2)
    y1_dft = dft(Y1)
    y2_dft = dft(Y2)
    res_dft = np.multiply(y1_dft, y2_dft)
    Amplitude = []
    phase = []
    for i in res_dft:
        Amplitude.append(round(np.sqrt((i.real) ** 2 + (i.imag) ** 2), 12))
        phase.append(float(math.atan2(i.imag, i.real)))
    final_IDFT, final_IDFT_DC, index = idft(Amplitude, phase)
    print("final_res: ", final_IDFT_DC)
    print(ConvTest_practical(indices, final_IDFT_DC))


def Compare_Signals(file_name, Your_indices, Your_samples):
    expected_indices = []
    expected_samples = []
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L = line.strip()
            if len(L.split(' ')) == 2:
                L = line.split(' ')
                V1 = int(L[0])
                V2 = float(L[1])
                expected_indices.append(V1)
                expected_samples.append(V2)
                line = f.readline()
            else:
                break
    print("Current Output Test file is: ")
    print(file_name)
    print("\n")
    if (len(expected_samples) != len(Your_samples)) and (len(expected_indices) != len(Your_indices)):
        print("Shift_Fold_Signal Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if (Your_indices[i] != expected_indices[i]):
            print("Shift_Fold_Signal Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Correlation Test case failed, your signal have different values from the expected one")
            return
    print("Correlation Test case passed successfully")


def conjugate_signal(dft_signal):
    lst = []
    for i in dft_signal:
        lst.append(i.real - i.imag * 1j)
    return lst


def FastCorrelation(choice):
    if choice == "Cross":
        x1, y1 = loadfile(int)
        x2, y2 = loadfile(int)
        N = len(y1)
        y1_dft = dft(y1)
        y2_dft = dft(y2)
        print("dft_signal1: ", y1_dft)
        # conjugate of signal 1
        conj_signal1 = conjugate_signal(y1_dft)
        print("conj_signal1: ", conj_signal1)

        res_dft = np.multiply(conj_signal1, y2_dft)
        Amplitude = []
        phase = []
        for i in res_dft:
            Amplitude.append(round(np.sqrt((i.real) ** 2 + (i.imag) ** 2), 12))
            phase.append(float(math.atan2(i.imag, i.real)))
        final_IDFT, final_IDFT_DC, index = idft(Amplitude, phase)
        print("res: ", final_IDFT_DC)
        res = []
        for i in final_IDFT_DC:
            res.append(i / N)
        print("final_res: ", res)
        print(Compare_Signals("Corr_Output_practical.txt", x1, res))

    elif choice == "Auto":
        x1, y1 = loadfile(int)
        N = len(y1)
        y1_dft = dft(y1)
        print("dft_signal1: ", y1_dft)
        # conjugate of signal 1
        conj_signal1 = conjugate_signal(y1_dft)
        print("conj_signal1: ", conj_signal1)
        res_dft = np.multiply(conj_signal1, y1_dft)
        Amplitude = []
        phase = []
        for i in res_dft:
            Amplitude.append(round(np.sqrt((i.real) ** 2 + (i.imag) ** 2), 12))
            phase.append(float(math.atan2(i.imag, i.real)))
        final_IDFT, final_IDFT_DC, index = idft(Amplitude, phase)
        print("res: ", final_IDFT_DC)
        res = []
        for i in final_IDFT_DC:
            res.append(i / N)
        print("final_res: ", res)


def practical_task():
    practical_task_window = Toplevel(root)
    practical_task_window.title("practical_task")
    practical_task_window.geometry('300x180')
    practical_task_window['background'] = "#00868B"

    Conv_button = tk.Button(practical_task_window, text="Fast Convolution", width=20, font=label_font,
                            background='#EEA2AD',
                            activebackground='yellow', command=FastConvolution)
    Conv_button.pack()
    Conv_button.place(x=60, y=40)

    combo = ttk.Combobox(practical_task_window, values=["Auto", "Cross"], font=label_font)
    combo.pack()
    combo.place(x=60, y=90)
    combo.current(0)

    Corr_button = tk.Button(practical_task_window, text="Fast Correlation", width=20, font=label_font,
                            background='#EEA2AD',
                            activebackground='yellow', command=lambda:FastCorrelation(combo.get()))
    Corr_button.pack()
    Corr_button.place(x=60, y=120)
    practical_task_window.mainloop()


######################## main window #######################
root = tk.Tk()
root.geometry('300x480')
root.title("Main Window")
root['background'] = '#00868B'

label_font = font.Font(slant='italic', weight='bold', size=10)
tk.Button(text="Task 1", font=label_font, padx=5, pady=5, width=20, background='#EEA2AD',
          activebackground='yellow',
          command=task1).place(x=60, y=20)
tk.Button(text="Task 2", font=label_font, padx=5, pady=5, width=20, activebackground='yellow', background='#EEA2AD',
          command=task2).place(x=60, y=70)
tk.Button(text="Task 3", font=label_font, padx=5, pady=5, width=20, activebackground='yellow', background='#EEA2AD',
          command=task3).place(x=60, y=120)
tk.Button(text="Task 4", font=label_font, padx=5, pady=5, width=20, activebackground='yellow', background='#EEA2AD',
          command=task4).place(x=60, y=170)
tk.Button(text="Task 5", font=label_font, padx=5, pady=5, width=20, activebackground='yellow', background='#EEA2AD',
          command=task5).place(x=60, y=220)
tk.Button(text="Task 6", font=label_font, padx=5, pady=5, width=20, activebackground='yellow', background='#EEA2AD',
          command=task6).place(x=60, y=270)
tk.Button(text="Task 7", font=label_font, padx=5, pady=5, width=20, activebackground='yellow', background='#EEA2AD',
          command=task7).place(x=60, y=320)
tk.Button(text="Task 8", font=label_font, padx=5, pady=5, width=20, activebackground='yellow', background='#EEA2AD',
          command=task8).place(x=60, y=370)
tk.Button(text="Practical Task", font=label_font, padx=5, pady=5, width=20, activebackground='yellow',
          background='#EEA2AD',
          command=practical_task).place(x=60, y=420)
root.mainloop()
