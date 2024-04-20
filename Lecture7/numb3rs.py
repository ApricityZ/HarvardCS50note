import re


def main():
    print(validate(input("IPv4 Adress: ")))


# def validate(ip):
#     pattern = r"25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?"
#     # if matches := re.search(f'^({pattern}\.){3}({pattern}?)$',ip.strip()):
#     if matches := re.search(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ip.strip()):
#         return True
#     else:return False

def validate(ip):
    pattern = r"25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?"
    if matches := re.search(f"^({pattern}\.){3}{pattern}$", ip):
        return True
    else:
        return False



if __name__=='__main__':
    main()