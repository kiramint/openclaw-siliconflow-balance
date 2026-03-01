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

echo "注意: SiliconFlow API直接连接，不使用代理（中国大陆可直连）"
echo "----------------------------------------------"

# 明确不设置代理，让Python脚本直接连接SiliconFlow
# 清除可能存在的代理环境变量，确保直接连接
unset https_proxy
unset http_proxy
unset HTTPS_PROXY
unset HTTP_PROXY

# 运行Python脚本
python3 "$PYTHON_SCRIPT"

exit $?