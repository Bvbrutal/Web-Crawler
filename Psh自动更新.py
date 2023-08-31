import re
from ftplib import FTP
import os

from colorama import Fore


def rename():
    path_deal = r"D:\pycharm project\Bvbrutal_gitpage\source\_posts"
    listdir = os.listdir(path_deal)
    for i in listdir:
        try:
            t = re.sub('\s[a-z0-9]{32}', '', i)
            os.rename(path_deal + f"/{i}", path_deal + f"/{t}")
            print(t)
        except:
            print(i, "rename出错了！")
            continue

def delete_remote_folder(ftp, remote_folder_path):
    # 列出远程文件夹中的所有文件和子文件夹
    file_list = ftp.nlst(remote_folder_path)
    file_list = [file for file in file_list if not file.endswith('.') and not file.endswith('..')]

    # 遍历远程文件列表并删除每个文件
    for remote_item in file_list:
        try:
            try:
                if ftp.nlst(remote_item):  # 如果是文件夹，则递归删除
                    delete_remote_folder(ftp, remote_item)
            except :
                ftp.delete(remote_item)
            print(f"{Fore.BLUE}{remote_item}{Fore.RESET} 文件已经从服务器删除！")
        except Exception as e:
            print(f"{Fore.BLUE}{remote_item}{Fore.RESET} 删除失败！: {e}")

    # 删除当前文件夹
    try:
        ftp.rmd(remote_folder_path)
        print(f"{Fore.GREEN}{remote_folder_path}{Fore.RESET} 文件夹已经从服务器删除！")
    except Exception as e:
        print(f"{Fore.GREEN}{remote_folder_path}{Fore.RESET} 删除失败！: {e}")

def join_with_forward_slash(*args):
    return '/'.join(args)

def upload_folder(ftp, local_folder_path, remote_folder_path):
    # 列出本地文件夹中的所有文件和子文件夹
    for item in os.listdir(local_folder_path):
        local_item_path = join_with_forward_slash(local_folder_path, item)
        remote_item_path = join_with_forward_slash(remote_folder_path, item)

        # 如果是文件，则上传
        if os.path.isfile(local_item_path):
            try:
                with open(local_item_path, 'rb') as file:
                    ftp.storbinary(f'STOR {remote_item_path}', file)
                print(f"{Fore.BLUE}{remote_item_path}{Fore.RESET} 文件上传到服务器成功！")
            except Exception as e:
                print(f"{Fore.BLUE}{remote_item_path}{Fore.RESET} 文件上传失败！: {e}")
        # 如果是文件夹，则递归调用upload_folder函数
        elif os.path.isdir(local_item_path):
            try:
                ftp.mkd(remote_item_path)  # 创建远程子文件夹
                print(f"{Fore.GREEN}{remote_item_path}{Fore.RESET} 文件夹上传到服务器成功！")
            except Exception as e:
                print(f"{Fore.GREEN}{remote_item_path}{Fore.RESET} 文件夹上传失败！: {e}")
            else:upload_folder(ftp, local_item_path, remote_item_path)

def main():
    # FTP服务器的地址、用户名和密码
    ftp_host = '81.71.101.143'
    ftp_user = 'pshxx_cc'
    ftp_password = '567reW4PwXjnmi6X'

    # 要上传的本地文件夹路径和远程文件夹路径
    local_folder_path = 'D:/pycharm project/Bvbrutal_gitpage/public'
    remote_folder_path = ''

    # 格式化名称
    rename()
    # 连接到FTP服务器
    ftp = FTP(ftp_host)
    ftp.login(ftp_user, ftp_password)
    print("-" * 20 + " 上传开始 " + "-" * 20)
    try:
        # 删除远程全部文件夹及其中的所有文件
        delete_remote_folder(ftp, remote_folder_path)
        # 全部上传文件夹
        upload_folder(ftp, local_folder_path, remote_folder_path)
        print("-" * 20 + " 上传成功 " + "-" * 20)
    except Exception as e:
        print("-" * 20 + " 上传失败 " + "-" * 20)
        print(f"An error occurred: {e}")
    finally:
        # 关闭FTP连接
        ftp.quit()

# 重命名和修改内容
import os
import re
import datetime

def deal_content(path_deal):
    current_time=datetime.datetime.now()
    path_deal=path_deal
    listdir=os.listdir(path_deal)
    for i in listdir:
        try:
            text=i
            pattern='\s[a-z0-9]{32}'
            matches = re.findall(pattern, text)
            if matches:
                text=text.replace(matches[0],'')
                title=os.path.splitext(os.path.basename(text))[0]
                current_time = current_time-datetime.timedelta(days=1)
                formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
                re1=f"---\ntitle: {title}\ndate: {formatted_time}\ncover: \ntags: \ncategories: \n---\n"
                print(re1)
                os.rename(path_deal+f"/{i}", path_deal+f"/{text}")
                print("-----文件{}重命名成功！-------".format(i))
                if os.path.isfile(path_deal+f"/{text}"):
                    with open(path_deal+f"/{text}", 'r+',encoding='utf-8') as file:
                        content = file.read()
                        pattern_1=f'\((.*{matches[0].strip()}.*\/)'
                        matches_1 = re.findall(pattern_1, content)
                        if matches_1:
                            print(matches_1[0])
                            content=content.replace(matches_1[0].strip(),'')
                        # 将文件指针移到开头
                        file.seek(0)
                        file.write(re1+content)
                        # 如果新内容较短，可能需要截断文件
                        file.truncate()
                        print("-----文件{}内容修改成功！-------".format(i))
            else:
                if os.path.isfile(path_deal+f"/{i}"):
                    title=os.path.splitext(os.path.basename(i))[0]
                    current_time = current_time-datetime.timedelta(days=1)
                    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
                    re1=f"---\ntitle: {title}\ndate: {formatted_time}\ncover: \ntags: \ncategories: \n---\n\n"
                    print(re1)
                    with open(path_deal+f"/{i}", 'r+',encoding='utf-8') as file:
                        content = file.read()
                        pattern_1='\((.*[a-z0-9]{32}.*\/)'
                        matches_1 = re.findall(pattern_1, content)
                        if matches_1:
                            print(matches_1[0])
                            content=content.replace(matches_1[0].strip(),'')
                        # 将文件指针移到开头
                        file.seek(0)
                        file.write(re1+content)
                        # 如果新内容较短，可能需要截断文件
                        file.truncate()
                        print("-----文件{}内容修改成功！-------".format(i))
        except Exception as e:
            print("-----{}出错了！------".format(i))
            print("捕获原始错误：", type(e).__name__)
            print("原始错误信息：", e)
            continue
import shutil
def remove_file(list_dir):
    for file in list_dir:
        file_name=os.path.basename(file)
        source_path=r"C:\Users\Polo\Downloads\post"+ "/" + file_name
        destination_path = r"D:\pycharm project\Bvbrutal_gitpage\source\_posts"+ "/" + file_name
        shutil.move(source_path, destination_path)#todo: maybe have some improvement but useless so work by your hands


if __name__ == '__main__':
    # path_deal=r'C:\Users\Polo\Downloads\post'
    # deal_content(path_deal)
    main()
