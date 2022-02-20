import shutil


#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import shutil

with open(r"\Users\krystof.sraier\Downloads\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Names\invited_names.txt", "r") as a, open(r"C:\Users\krystof.sraier\Downloads\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Letters\starting_letter.txt", "r") as b:
        line_1 = a.readlines()
        line_2 = b.readlines()
        for i in line_1:
            c = i.strip()
            line_2[0] = "Dear " + c + "," + "\n"
            with open(r"C:\Users\krystof.sraier\Downloads\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Letters\starting_letter.txt", "w") as data:
                data.writelines(line_2)
                data.close()
            original = r"C:\Users\krystof.sraier\Downloads\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Letters\starting_letter.txt"
            target = r"C:\Users\krystof.sraier\Downloads\Mail+Merge+Project+Start\Mail Merge Project Start\Output\ReadyToSend\final_email_{}.txt".format(c)
            shutil.copy(original, target)






