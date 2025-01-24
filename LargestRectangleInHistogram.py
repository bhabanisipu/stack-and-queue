def largestRectangle(arr):
    n = len(arr)
    maxa = 0
    st = []
    for i in range(n):
        while(st and arr[st[-1]]>arr[i]):
            ele = st[-1]
            height = arr[ele]
            st.pop()
            nse = i 
            if(len(st) == 0):
                pse = -1
            else:
                pse = st[-1]
            maxa = max(maxa,(nse-pse-1)*height)
            
        st.append(i)
    while(st):
        ele = st[-1]
        st.pop()
        height = arr[ele]
        nse = n
        if(st):
            pse = st[-1]
        else:
            pse = -1
        maxa = max(maxa,(nse-pse-1)*height)
    return maxa