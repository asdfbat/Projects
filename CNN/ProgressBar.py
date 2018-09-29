import time
import sys
import subprocess

class ProgressBar:
    def __init__(self, total, update_freq):
        self.total = total
        self.update_freq = update_freq
        rows, colomns = subprocess.check_output(['stty', 'size']).split()  # terminal size.
        self.rows = int(rows.decode("utf-8"))
        self.colomns = int(colomns.decode("utf-8"))
        self.bar_width = (self.colomns - 12)
    def update_progress_bar(self, progress):
        sys.stdout.write("\b"*(self.bar_width+12))
        current_bars = ((progress*self.bar_width) + self.total//2 )//self.total
        sys.stdout.write(" %5.1f%%" %(float(progress)/(self.total)*100))
        sys.stdout.write("  [%s]" % (" "*self.bar_width))
        sys.stdout.flush()
        sys.stdout.write("\b"*(self.bar_width+1))
        sys.stdout.write(":"*current_bars)
        sys.stdout.flush()
        if (self.total - progress) < self.update_freq:
            sys.stdout.write("\n")

if __name__ == "__main__":
    import time
    from ProgressBar import ProgressBar

    N = 345345
    update_freq = N//100

    start_time1 = time.clock()
    for i in range(N+1):
        x = N/(i-2.5)
    end_time1 = time.clock()

    bar = ProgressBar(N, update_freq)
    start_time2 = time.clock()
    for i in range(N+1):
        x = N/(i-2.5)
        if i%update_freq == 0:
            bar.update_progress_bar(i)
    end_time2 = time.clock()

    print("%d loops.\nNo bar = %.6f seconds\nWith bar = %.6f seconds" % (N, (end_time1-start_time1), (end_time2-start_time2)))
