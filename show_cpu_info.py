import subprocess
# file: show_cpu_info.py
# calls the
p1 = subprocess.Popen(["cat", "/proc/cpuinfo"], stdout=subprocess.PIPE)
output,err = p1.communicate()
#print output
j=output.count("processor")
print j, "Processors found"
print "Siblings list:"
prefix="/sys/devices/system/cpu/cpu"
suffix="/topology/thread_siblings_list"
for i in range( output.count("processor") ):
    pathstr= prefix + str(i) + suffix
    #print pathstr
    #print i
    p2=subprocess.Popen(["cat",pathstr], stdout=subprocess.PIPE)
    siblings,err = p2.communicate()
    print siblings.split("\n")[0]
