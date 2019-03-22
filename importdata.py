import os

def gci(filepath):
#遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath,fi)            
        if os.path.isdir(fi_d):
            filexlsxs = os.listdir(fi_d)
            for x in filexlsxs:
                low_files=os.path.splitext(os.path.join(fi_d,x))
                filename,types=low_files
                if(types == ".csv"):
                    break   
        else:
            print(os.path.join(filepath,fi_d))

gci(R"D:\Documents\政府经济\2019.3.22")