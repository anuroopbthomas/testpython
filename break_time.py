import webbrowser as yt
import time
total_breaks = 3
break_count = 0

print("This program started on: "+time.ctime())
while (break_count < total_breaks):
    time.sleep(30*60)
    yt.open("https://www.youtube.com/watch?v=MdG4f5Y3ugk")
    break_count = break_count + 1
