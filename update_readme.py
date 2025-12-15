"""
从 list.yaml 生成 LIST.md 文件
Generate LIST.md file from list.yaml
"""

import re


def parse_yaml(yaml_file):
    """解析 YAML 文件，返回条目列表"""
    items = []
    with open(yaml_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 匹配 YAML 条目：- id: 数字\n  name: 名称
    pattern = r'- id: (\d+)\s+name: (.+)'
    matches = re.findall(pattern, content)
    
    for item_id, name in matches:
        items.append({
            'id': int(item_id),
            'name': name.strip()
        })
    
    return items


def generate_list_md(items, output_file):
    """生成 LIST.md 文件"""
    lines = []
    
    # 标题
    lines.append("# 数据集清单 / Dataset Index")
    lines.append("")
    
    # SUM统计
    lines.append(f"**SUM = {len(items)}**")
    lines.append("")
    
    # 下载链接
    lines.append("您可点击右侧链接处下载全部数据集 [[DOWNLOAD ALL]](https://pan.quark.cn/s/97ed18e0aacd?pwd=f6rV)")
    lines.append("")
    lines.append("You can download the complete dataset by clicking the link on the right [[DOWNLOAD ALL]](https://pan.quark.cn/s/97ed18e0aacd?pwd=f6rV)")
    lines.append("")
    
    # 清单标题
    lines.append("## 清单 / List")
    lines.append("")
    
    # 表格标题
    lines.append("| 序号<br>No. | 名称<br>Name |")
    lines.append("|------|------|")
    
    # 数据行
    for item in items:
        lines.append(f"| {item['id']} | {item['name']} |")
    
    # 写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    print(f"Successfully generated {output_file} with {len(items)} items")


if __name__ == '__main__':
    # 读取 list.yaml
    items = parse_yaml('list.yaml')
    
    # 生成 LIST.md
    generate_list_md(items, 'LIST.md')

