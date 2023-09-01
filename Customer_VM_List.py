# Script to get Customer Code from the VM

customer_code = 0

with open('All_VM_list.txt', 'r') as vm_list:
    for VM_Name in vm_list:
        splited_VM_Name = VM_Name.split("-")
        for splitted_vm_part in splited_VM_Name:
            if len(splitted_vm_part) == 4:
                if splitted_vm_part.isdigit():
                    customer_code = splitted_vm_part
        print(f"{VM_Name.split()[0]},{customer_code}")
        customer_code = 0