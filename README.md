# OpenClaw SiliconFlow Balance Skill

OpenClaw skill for querying SiliconFlow API balance directly from OpenClaw configuration.

## Features

- ✅ **Automatic configuration reading** - Extracts API key from OpenClaw's `openclaw.json`
- ✅ **Proxy support** - Works behind proxies (common in China)
- ✅ **Beautiful formatting** - Clear, human-readable output with emoji indicators
- ✅ **Balance status alerts** - Warns when balance is low
- ✅ **Zero configuration** - Uses existing OpenClaw setup

## Installation

### As an OpenClaw Skill

1. Copy the skill directory to your OpenClaw skills folder:
   ```bash
   cp -r siliconflow-balance /path/to/openclaw/skills/
   ```

2. OpenClaw will automatically detect and make the skill available

### Manual Installation

1. Ensure Python 3.6+ is installed
2. Install required dependencies:
   ```bash
   pip install requests
   ```

## Usage

### Quick Check (Bash wrapper)
```bash
./scripts/siliconflow-quick-check.sh
```

### Python Script
```bash
python scripts/siliconflow-balance-query.py
```

### Direct Connection (中国大陆可直连)
```bash
python scripts/siliconflow-balance-query.py
```

## Sample Output

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

| Status | Threshold | Emoji | Recommendation |
|--------|-----------|-------|----------------|
| Sufficient | ≥ ¥50 | ✅ | Balance is healthy |
| Low | < ¥50 | 💡 | Consider monitoring |
| Insufficient | < ¥10 | ⚠️ | Recharge recommended |

## How It Works

1. Reads OpenClaw configuration from `~/.openclaw/openclaw.json`
2. Extracts SiliconFlow API key from the configuration
3. Queries SiliconFlow API endpoint: `https://api.siliconflow.cn/v1/user/info`
4. Parses and formats the response
5. Provides balance status based on thresholds

## Requirements

- OpenClaw with SiliconFlow provider configured
- Python 3.6+
- `requests` library (optional, for manual installation)
- Network access to `api.siliconflow.cn`

## Skill Integration

This skill follows OpenClaw's skill structure:

- `SKILL.md` - Main skill documentation and metadata
- `scripts/` - Executable scripts
- `references/` - API documentation and references
- `assets/` - Supporting files (currently empty)

## License

MIT

## Author

Created for Kira Mint's OpenClaw assistant

## Contributing

Feel free to submit issues and pull requests for improvements.