# Push message action

This action can push messages to specified users through different servers.

# Available server

- [x] QYWX(企业微信)
- [ ] webhook

# Usage

```yaml
steps:
  - name: Push message
    uses: maxiaowei0216/push-message@v0.1
    env:
      QYWX_CORP_ID: ${{ secrets.QYWX_CORP_ID }}
      QYWX_CORP_SECRET: ${{ secrets.QYWX_CORP_SECRET }}
      QYWX_AGENT_ID: 1000001
      QYWX_TO_USER: '@all'
    with:
      server: QYWX
      message: "Hello world"
```

## QYWX

各变量的获取方式可参考：[https://developer.work.weixin.qq.com/document/path/90665](https://developer.work.weixin.qq.com/document/path/90665)

使用企业微信推送消息，需要指定如下**环境变量**

| 环境变量 | 说明                |
|---|-------------------|
|QYWX_CORP_ID| 企业ID              |
|QYWX_CORP_SECRET| 	应用的凭证密钥          |
|QYWX_AGENT_ID| 应用ID              |
|QYWX_TO_USER| 接收者的用户帐号列表，默认`@all` |