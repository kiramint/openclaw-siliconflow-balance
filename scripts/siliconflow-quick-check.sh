#!/bin/bash
# SiliconFlow余额快速查询脚本
# 直接从OpenClaw配置读取API密钥并查询余额

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="${SCRIPT_DIR}/siliconflow-balance-query.py"

# 检查Python脚本是否存在
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "❌ Python脚本不存在: $PYTHON_SCRIPT"
    exit 1
fi

# 设置代理（如果需要）
if [ -n "$HTTPS_PROXY" ] || [ -n "$HTTP_PROXY" ]; then
    echo "🔗 检测到代理设置"
    
    # 传递给Python环境
    export https_proxy="${HTTPS_PROXY:-$HTTP_PROXY}"
    export http_proxy="${HTTP_PROXY:-$HTTPS_PROXY}"
fi

# 运行Python脚本
python3 "$PYTHON_SCRIPT"

exit $?