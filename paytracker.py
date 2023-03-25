# import time
# from stopwatch import Stopwatch
# from threading import Timer
# import streamlit as st
#
#
# salary = int(st.text_input('Enter your Salary'))
#
# pay_per_hour = salary/12/2/80
#
# pay_per_second = pay_per_hour/3600
#
# paycheck_so_far = 0
# stopwatch = Stopwatch(2)
#
# placeholder = st.empty()
#
# """
# Track Your Pay By the Second!
# """
#
# # start = time.time()
# while True:
#     # stopwatch.start()
#     paycheck_so_far += pay_per_second*0.1
#     with placeholder.container():
#         st.write(f"time {stopwatch}, pay: {round(paycheck_so_far,2)}")
#         # st.write(f"time {start - time.}, pay: {round(paycheck_so_far, 2)}")
#     time.sleep(0.1)

from employee import Employee
import threading
import time

if __name__ == "__main__":
    john = Employee('john', 120000)
    threading.Thread(target=john.start).start()

    michael = Employee('michael', 180000)
    threading.Thread(target=michael.start).start()

    count = 0
    while True:
        if count % 60 == 0:
            print(f'john\'s pay {john.pay()}')
            print(f'michael\'s pay {michael.pay()}')
        count += 1
        time.sleep(1)



