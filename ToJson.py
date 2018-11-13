
# coding: utf-8

# In[23]:


name = "Min Chen"
strong_name = "<strong>" + name + "</strong>"
i = 0;
with open(r'C:\Users\yuqiao\Desktop\publications.txt','r',encoding='ISO-8859-15') as f_read:
    line = f_read.readline()
    while line:
        id = line.split("\t")[0]
        content = line.split("\t")[1].replace("\"","\\\"").replace(name,strong_name).replace("\n","")
        print(id)
        print(content)
        with open(r'C:\Users\yuqiao\Desktop\publications.json','a',encoding='ISO-8859-15') as f_write:
            if i== 0:
                f_write.write("[\n{\"id\":")
            else :
                f_write.write(",\n{\"id\":")
            f_write.write(id)
            f_write.write(",\n\"content\":\"")
            f_write.write(content)
            f_write.write("\"\n}")
            i = i+1;
        line = f_read.readline()
    with open(r'C:\Users\yuqiao\Desktop\publications.json','a',encoding='ISO-8859-15') as f_write:
        f_write.write("\n]")
        
     

