---
name: siliconflow-balance
description: Query SiliconFlow API balance directly from OpenClaw configuration. Activate when user wants to check SiliconFlow API usage, remaining balance, or account status.
metadata:
  openclaw:
    emoji: "💎"
    os: ["darwin", "linux"]
    requires:
      bins: ["python3"]
    install:
      - id: "pip-deps"
        kind: "pip"
        packages: ["requests"]
        label: "Install Python requests library"
---

# SiliconFlow Balance Query Skill

This skill provides tools to query SiliconFlow API balance directly from OpenClaw configuration. It automatically extracts the API key from OpenClaw's `openclaw.json` configuration file and queries the SiliconFlow user info endpoint.

## When to Use

- User asks to check SiliconFlow API balance
- User wants to monitor API usage costs
- User needs to check account status (available balance, recharge balance, total balance)
- User wants to set up periodic balance checks

## Quick Start

### 1. Using the bundled scripts

The skill includes two ready-to-use scripts:

```bash
# Method 1: Use the integrated Python script
python scripts/siliconflow-balance-query.py

# Method 2: Use the shell wrapper (auto-sets proxy if needed)
./scripts/siliconflow-quick-check.sh
```

### 2. Manual Query (if you need to debug)

```bash
# Export proxy if needed
export HTTPS_PROXY=http://127.0.0.1:7890

# Run the query
python scripts/siliconflow-balance-query.py
```

## How It Works

1. **Automatic Configuration Reading**: The script reads `~/.openclaw/openclaw.json` to find SiliconFlow API configuration
2. **Direct Connection**: SiliconFlow API is accessed directly without proxy (accessible from Mainland China)
3. **Balance Display**: Shows available balance, recharge balance, and total balance with status indicators

## Output Example

```
============================================================
硅基流动(SiliconFlow)账户余额查询
查询时间: 2026-03-01 13:40:17
============================================================
账户ID: r0uqp80km0
账户名称: 个人
------------------------------------------------------------
💎 可用余额: 7.3972 元
💰 充值余额: 15.2505 元
📊 总余额: 22.6478 元
💡 余额较低，建议关注
============================================================
```

## Balance Status Indicators

- **✅ 余额充足**: Total balance ≥ 50元
- **💡 余额较低**: Total balance < 50元 but ≥ 10元  
- **⚠️ 余额不足**: Total balance < 10元

## Integration with OpenClaw

This skill works seamlessly with OpenClaw because:

1. Uses the same API key already configured in OpenClaw
2. Respects proxy settings when needed
3. Outputs are formatted for easy reading in chat interfaces
4. Can be triggered via OpenClaw's skill matching system

## Troubleshooting

### Common Issues

1. **Network Connection Error**
   - SiliconFlow API should be directly accessible from Mainland China
   - If you're outside China, ensure you have proper network access

2. **API Key Not Found**
   - Ensure OpenClaw is configured with SiliconFlow provider
   - Check `~/.openclaw/openclaw.json` exists and contains valid configuration

3. **Certificate Verification Error**
   - The script includes SSL certificate verification bypass for development environments
   - Not recommended for production use

## References

See `references/api-docs.md` for SiliconFlow API documentation.

## Maintenance

- Keep the API endpoint URL updated if SiliconFlow changes it
- Monitor for changes in the API response format
- Update balance thresholds based on typical usage patterns