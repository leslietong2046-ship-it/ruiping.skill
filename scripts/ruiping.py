#!/usr/bin/env python3
"""
锐评生成器 - 命令行工具
用法: python demo.py "事件描述" 或 python demo.py --file news.txt
"""

import argparse
import sys
import re
from datetime import datetime
from pathlib import Path


class RuiPingGenerator:
    """锐评生成器类"""
    
    def __init__(self):
        self.template = """📌 【锐评】{title}

一句话结论：{conclusion}

▌为什么重要
{why_important}

▌对谁有影响
{impact}

▌该怎么做
{action}

▌一句话锐评
{final_comment}
"""
    
    def extract_keywords(self, event: str) -> list:
        """从事件描述中提取关键词"""
        # 移除常见动词和语气词，保留名词和关键概念
        stopwords = ['的', '了', '是', '在', '又', '很', '非常', '这个', '那个', '最近', '今天', '昨天']
        words = re.findall(r'[\u4e00-\u9fa5a-zA-Z0-9]+', event)
        return [w for w in words if w not in stopwords and len(w) > 1]
    
    def generate_title(self, event: str) -> str:
        """生成锐评标题"""
        keywords = self.extract_keywords(event)
        if len(keywords) >= 2:
            return f"{keywords[0]}：{keywords[1]}背后的问题"
        return event
    
    def generate_conclusion(self, event: str) -> str:
        """生成一句话结论"""
        keywords = self.extract_keywords(event)
        if not keywords:
            return "这事没那么简单。"
        
        # 基于关键词生成犀利结论
        size = len(keywords)
        if size >= 2:
            return f"表面是{keywords[0]}，实质是{keywords[1]}的博弈。"
        return f"这事值得关注。"
    
    def generate_why_important(self, event: str) -> str:
        """生成为什么重要"""
        keywords = self.extract_keywords(event)
        event_short = event[:20] + "..." if len(event) > 20 else event
        
        lines = [
            f"- {event_short}这件事，不是孤立事件",
            "- 背后往往有多方利益博弈",
            "- 处理不好会影响一批人"
        ]
        return "\n".join(lines)
    
    def generate_impact(self, event: str) -> str:
        """生成对谁有影响"""
        keywords = self.extract_keywords(event)
        subject = keywords[0] if keywords else "相关方"
        
        lines = [
            f"- {subject}：直接影响最大，需要立即应对",
            "- 上下游关联方：间接受波及，观望为主",
            "- 普通用户/消费者：看热闹但迟早被影响"
        ]
        return "\n".join(lines)
    
    def generate_action(self, event: str) -> str:
        """生成该怎么做"""
        return """- 第一时间搞清楚来龙去脉，别被标题党带节奏
- 评估对自己的影响范围和程度
- 该行动的别拖，该观望的别慌"""
    
    def generate_final_comment(self, event: str) -> str:
        """生成一句话锐评"""
        keywords = self.extract_keywords(event)
        if not keywords:
            return "有些事，看透不说透，才是好朋友。"
        
        return f"{keywords[0] if keywords else '这事'}嘛，从来都是当局者迷，旁观者也不敢说清。"
    
    def generate(self, event: str) -> str:
        """生成完整锐评"""
        title = self.generate_title(event)
        conclusion = self.generate_conclusion(event)
        why_important = self.generate_why_important(event)
        impact = self.generate_impact(event)
        action = self.generate_action(event)
        final_comment = self.generate_final_comment(event)
        
        return self.template.format(
            title=title,
            conclusion=conclusion,
            why_important=why_important,
            impact=impact,
            action=action,
            final_comment=final_comment
        )


def read_input(source: str) -> str:
    """读取输入内容"""
    path = Path(source)
    if path.exists() and path.is_file():
        try:
            return path.read_text(encoding='utf-8').strip()
        except UnicodeDecodeError:
            try:
                return path.read_text(encoding='gbk').strip()
            except Exception as e:
                raise ValueError(f"无法读取文件: {e}")
    return source


def save_output(content: str, output_path: str = None) -> str:
    """保存输出到文件"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    default_path = f"ruiping_{timestamp}.md"
    save_path = output_path or default_path
    
    try:
        Path(save_path).write_text(content, encoding='utf-8')
        return save_path
    except Exception as e:
        raise ValueError(f"无法保存文件: {e}")


def main():
    parser = argparse.ArgumentParser(
        description='锐评生成器 - 一键生成犀利评论',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python demo.py "特斯拉又降价了"
  python demo.py --file news.txt
  python demo.py "OpenAI发布新模型" -o ai_review.md
        """
    )
    
    parser.add_argument(
        'event',
        nargs='?',
        help='要锐评的事件描述'
    )
    parser.add_argument(
        '-f', '--file',
        help='从文件读取事件描述'
    )
    parser.add_argument(
        '-o', '--output',
        help='输出文件路径（可选，默认保存为 ruiping_时间戳.md）'
    )
    parser.add_argument(
        '-s', '--stdout-only',
        action='store_true',
        help='仅输出到stdout，不保存文件'
    )
    
    args = parser.parse_args()
    
    # 获取事件描述
    if args.file:
        try:
            event = read_input(args.file)
        except ValueError as e:
            print(f"错误: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.event:
        event = args.event
    else:
        print("错误: 请提供事件描述或使用 --file 指定文件", file=sys.stderr)
        print("使用 --help 查看帮助", file=sys.stderr)
        sys.exit(1)
    
    if not event:
        print("错误: 事件描述不能为空", file=sys.stderr)
        sys.exit(1)
    
    # 生成锐评
    generator = RuiPingGenerator()
    try:
        result = generator.generate(event)
    except Exception as e:
        print(f"错误: 生成锐评失败: {e}", file=sys.stderr)
        sys.exit(1)
    
    # 输出结果
    print(result)
    
    # 保存文件
    if not args.stdout_only:
        try:
            saved_path = save_output(result, args.output)
            print(f"\n[已保存到: {saved_path}]", file=sys.stderr)
        except ValueError as e:
            print(f"警告: {e}", file=sys.stderr)


if __name__ == '__main__':
    main()
