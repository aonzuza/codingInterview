from collections import deque;


def max_of_subarray(lst,k):

    index_queue = deque();

    for index in range(k):

        while index_queue and lst[index] >= lst[index_queue[-1]]:
            index_queue.pop();

        index_queue.append(index);

    print(index_queue);

    for index in range(k,len(lst)):

        print(lst[index_queue[0]]);

        while index_queue and  index_queue[0] <= index - k:
            index_queue.popleft();

        while index_queue and lst[index_queue[-1]] <= lst[index]:
            index_queue.pop();

        index_queue.append(index);

    print(lst[index_queue[0]]);




lst = [10,5,2,7,8,20];

max_of_subarray(lst,3);
