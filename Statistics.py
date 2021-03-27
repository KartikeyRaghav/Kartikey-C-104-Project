from collections import Counter
import csv

def mean(data):
    return sum(data)/len(data)

def median(data):
    number = len(data)
    index = number // 2
    if number % 2 :
        return data[index]
    else:
        return sum(data[index-1:index+1])/2

def mode(data):
    count = Counter(data)
    temp = {
        '75-85':0,
        '85-95':0,
        '95-105':0,
        '105-115':0,
        '115-125':0,
        '125-135':0,
        '135-145':0,
        '145-155':0,
        '155-165':0,
        '165-175':0,
    }
    for weight, occurence in count.items():
        if 75 < weight < 85:
            temp['75-85'] += occurence
        elif 85 < weight < 95:
            temp['85-95'] += occurence
        elif 95 < weight < 105:
            temp['95-105'] += occurence
        elif 105 < weight < 115:
            temp['105-115'] += occurence
        elif 115 < weight < 125:
            temp['115-125'] += occurence
        elif 125 < weight < 135:
            temp['125-135'] += occurence
        elif 135 < weight < 145:
            temp['135-145'] += occurence
        elif 145 < weight < 155:
            temp['145-155'] += occurence
        elif 155 < weight < 165:
            temp['155-165'] += occurence
        elif 165 < weight < 175:
            temp['165-175'] += occurence
    mode_range, mode_occurence = 0,0
    for range, occurence in temp.items():
        if occurence > mode_occurence:
            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
        mode = float((mode_range[0] + mode_range[1]) / 2)
    return mode

if __name__ == '__main__':
    with open('HeightWeight.csv', newline='') as f:
        reader = csv.reader(f)
        file_data = list(reader)
        file_data.pop(0)
        new_data = []
        for i in range(len(file_data)):
            data = file_data[i][2]
            new_data.append(float(data))
        sorted_data = sorted(new_data)
        mean = mean(new_data)
        median = median(sorted_data)
        mode = mode(sorted_data)
        print(f'Mean is: {mean}\nMedian is: {median}\nMode is: {mode}')