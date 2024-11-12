import requests

def fetch_and_filter():
    url = 'https://raw.githubusercontent.com/yuanzl77/IPTV/refs/heads/main/live.txt,https://fanmingming.com/txt?url=https://live.fanmingming.com/tv/m3u/ipv6.m3u'
    
    # 获取文件内容
    response = requests.get(url)
    content = response.text
    
    # 过滤掉包含 "ipv6" 的行
    filtered_lines = [line for line in content.splitlines() if 'ipv4' not in line.lower()]
    
    # 保存到新文件
    with open('live_ipv4.txt', 'w') as file:
        file.write('\n'.join(filtered_lines))

if __name__ == "__main__":
    fetch_and_filter()