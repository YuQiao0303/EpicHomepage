import re
#reg=r'\s+[^(href)]*=\"[^<>]+\"'
reg = r'\b(?!(?:href|src))\w+=(["\']).+?\1'
with open(r'input.txt','r',encoding='ISO-8859-15') as f_read:
    html= f_read.read()
    result = re.sub(reg,"",html)  #remove the original style
    
    result = re.sub(r'<\s*table\s*>','<table class="table14_3">',result) #modify the class of table
    #result = re.sub(r'<\s*table\s*>','<table class="table14_3">',result) #modify the class of table
    
    print(result)
    with open(r'output.txt','w',encoding='ISO-8859-15') as f_write:            
        f_write.write(result)
            
