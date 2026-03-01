#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SiliconFlow Balance Query Tool for OpenClaw
直接从OpenClaw配置读取API密钥并查询余额
"""

import json
import os
import urllib.request
import urllib.error
import sys
from datetime import datetime

def get_openclaw_config():
    """读取OpenClaw配置文件"""
    config_path = os.path.expanduser('~/.openclaw/openclaw.json')
    if not os.path.exists(config_path):
        print(f"❌ 未找到OpenClaw配置文件: {config_path}")
        return None
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        return config
    except Exception as e:
        print(f"❌ 读取配置文件失败: {e}")
        return None

def get_siliconflow_api_key(config):
    """从配置中提取SiliconFlow API密钥"""
    try:
        providers = config.get('models', {}).get('providers', {})
        
        for provider_name, provider_config in providers.items():
            if 'siliconflow' in provider_name.lower():
                api_key = provider_config.get('apiKey')
                if api_key:
                    return api_key
        
        print("❌ 未找到SiliconFlow API密钥配置")
        return None
    except Exception as e:
        print(f"❌ 提取API密钥失败: {e}")
        return None

def query_balance(api_key, proxy=None):
    """查询SiliconFlow余额"""
    url = "https://api.siliconflow.cn/v1/user/info"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # 设置代理
    if proxy:
        proxy_support = urllib.request.ProxyHandler({'https': proxy, 'http': proxy})
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            data = response.read().decode("utf-8")
            result = json.loads(data)
            
            if result.get("status") == True:
                return result.get("data", {})
            else:
                print(f"❌ API返回错误: {result.get('message', '未知错误')}")
                return None
                
    except urllib.error.URLError as e:
        print(f"❌ 网络请求错误: {e}")
        if "CERTIFICATE_VERIFY_FAILED" in str(e):
            print("💡 证书验证失败，尝试添加SSL证书验证豁免")
            import ssl
            ssl._create_default_https_context = ssl._create_unverified_context
            # 重试一次
            return query_balance(api_key, proxy)
        return None
    except Exception as e:
        print(f"❌ 请求异常: {e}")
        return None

def format_balance_output(balance_info):
    """格式化余额信息输出"""
    if not balance_info:
        return "❌ 未获取到余额信息"
    
    output = []
    output.append("=" * 60)
    output.append(f"硅基流动(SiliconFlow)账户余额查询")
    output.append(f"查询时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    output.append("=" * 60)
    
    # 基本信息
    if "id" in balance_info:
        output.append(f"账户ID: {balance_info['id']}")
    if "name" in balance_info:
        output.append(f"账户名称: {balance_info['name']}")
    if "email" in balance_info and balance_info['email']:
        output.append(f"邮箱: {balance_info['email']}")
    
    output.append("-" * 60)
    
    # 余额信息
    if "balance" in balance_info:
        balance = float(balance_info['balance']) if balance_info['balance'] else 0.0
        output.append(f"💎 可用余额: {balance_info['balance']} 元")
    if "chargeBalance" in balance_info:
        charge = float(balance_info['chargeBalance']) if balance_info['chargeBalance'] else 0.0
        output.append(f"💰 充值余额: {balance_info['chargeBalance']} 元")
    if "totalBalance" in balance_info:
        total_str = balance_info['totalBalance']
        total = float(total_str) if total_str else 0.0
        output.append(f"📊 总余额: {total_str} 元")
        
        # 余额状态提示
        if total < 10:
            output.append("⚠️ 余额不足，请及时充值")
        elif total < 50:
            output.append("💡 余额较低，建议关注")
        else:
            output.append("✅ 余额充足")
    
    output.append("=" * 60)
    return "\n".join(output)

def main():
    """主函数"""
    print("🔍 正在查询SiliconFlow余额...")
    
    # 1. 读取配置
    config = get_openclaw_config()
    if not config:
        sys.exit(1)
    
    # 2. 获取API密钥
    api_key = get_siliconflow_api_key(config)
    if not api_key:
        sys.exit(1)
    
    print(f"✅ 已从OpenClaw配置获取API密钥（前8位: {api_key[:8]}...）")
    
    # 3. 设置代理（可选）
    proxy = None
    # 可以从环境变量读取代理
    proxy_env = os.environ.get('https_proxy') or os.environ.get('HTTPS_PROXY') or os.environ.get('http_proxy') or os.environ.get('HTTP_PROXY')
    if proxy_env:
        proxy = proxy_env
        print(f"🔗 使用代理: {proxy}")
    
    # 4. 查询余额
    print("📡 正在请求API...")
    balance_info = query_balance(api_key, proxy)
    
    # 5. 输出结果
    if balance_info:
        output = format_balance_output(balance_info)
        print(output)
        
        # 保存结果到文件
        try:
            result_file = os.path.join(os.getcwd(), 'siliconflow_balance_result.txt')
            with open(result_file, 'w', encoding='utf-8') as f:
                f.write(output)
            print(f"💾 结果已保存到: {result_file}")
        except:
            pass
        
        return 0
    else:
        print("❌ 查询失败，请检查网络或API密钥")
        return 1

if __name__ == "__main__":
    sys.exit(main())