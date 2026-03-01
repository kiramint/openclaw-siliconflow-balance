# SiliconFlow API Documentation Reference

## Overview

SiliconFlow (硅基流动) is a Chinese AI model service provider that offers various AI models through a OpenAI-compatible API interface.

## API Endpoints

### User Information Endpoint
```
GET https://api.siliconflow.cn/v1/user/info
```

**Headers:**
```
Authorization: Bearer {api_key}
Content-Type: application/json
```

**Response Format:**
```json
{
  "status": true,
  "message": "success",
  "data": {
    "id": "r0uqp80km0",
    "name": "个人",
    "email": "user@example.com",
    "balance": "7.3972",
    "chargeBalance": "15.2505", 
    "totalBalance": "22.6478",
    "status": "active"
  }
}
```

**Field Descriptions:**

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | User account ID |
| `name` | string | Account display name |
| `email` | string | Registered email address |
| `balance` | string | Available balance (可用余额) in CNY |
| `chargeBalance` | string | Recharge balance (充值余额) in CNY |
| `totalBalance` | string | Total balance (总余额) = balance + chargeBalance |
| `status` | string | Account status: "active", "suspended", etc. |

## Authentication

SiliconFlow uses Bearer token authentication. The API key can be obtained from:

1. SiliconFlow Console: https://siliconflow.cn
2. Create or view API keys in the account settings
3. API keys typically start with `sk-` prefix

## Rate Limits

- Unknown rate limits, but generally generous for balance checking
- Recommended: Query balance no more than once per minute
- For production monitoring: Once every 5-10 minutes is sufficient

## Error Responses

### Common HTTP Status Codes

| Code | Meaning | Solution |
|------|---------|----------|
| 200 | Success | Normal response |
| 401 | Unauthorized | Invalid or expired API key |
| 403 | Forbidden | Insufficient permissions |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Server Error | SiliconFlow service issue |

### Error Response Format
```json
{
  "status": false,
  "message": "Error description here",
  "data": null
}
```

## Pricing Information

SiliconFlow charges based on token usage. Different models have different pricing:

| Model | Input (per 1K tokens) | Output (per 1K tokens) |
|-------|---------------------|----------------------|
| DeepSeek-V3.2 | ~¥0.001 | ~¥0.002 |
| Qwen2.5 | ~¥0.0005 | ~¥0.001 |
| Llama3.1 | ~¥0.0008 | ~¥0.0015 |

*Note: Prices are approximate and subject to change. Check SiliconFlow website for current pricing.*

## Integration Notes

1. **Proxy Required in China**: Mainland China users may need to use a proxy to access the API
2. **SSL Certificates**: Some environments may have SSL certificate verification issues
3. **Currency**: All balances are in Chinese Yuan (CNY, 元)
4. **Precision**: Balances are returned as strings with 4 decimal places

## Monitoring Recommendations

1. **Warning Threshold**: Alert when total balance < ¥50
2. **Critical Threshold**: Alert when total balance < ¥10  
3. **Recharge Recommendation**: Consider recharging when balance < ¥20
4. **Usage Tracking**: Monitor balance changes to estimate monthly costs

## Support Resources

- Official Website: https://siliconflow.cn
- Documentation: https://docs.siliconflow.cn
- Console: https://console.siliconflow.cn
- Support: support@siliconflow.cn