# Cursor Python Template

## 快速开始

### 1. 安装依赖

推荐使用 requirements.txt：

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. 启动服务

```bash
python -m uvicorn src.main:app --reload
```

> **注意：**
> 启动服务前请确保已激活虚拟环境（`source venv/bin/activate` 或 `source .venv/bin/activate`），否则可能出现 `zsh: command not found: uvicorn` 错误。

### 3. 访问 API 文档

浏览器打开 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 查看交互式文档。

### 4. 加法 API 示例

- 路径：`POST /api/math/add`
- 请求体：
  
  ```json
  {
    "a": 1.2,
    "b": 3.4
  }
  ```

- 响应体：
  
  ```json
  {
    "result": 4.6
  }
  ```

## 5. 运行测试

本项目使用 [pytest](https://docs.pytest.org/) 进行测试，所有测试文件位于 `./tests` 目录。

推荐使用如下命令运行全部测试：

```bash
pytest
```

如需查看详细测试输出，可加上 `-v` 参数：

```bash
`pytest -v
```

> **注意：**
> 请确保已激活虚拟环境并已安装所有依赖，否则 pytest 可能无法正常运行。

## 6. 后端 Provider 契约验证（Pact）

本项目支持基于 Pact 的服务端契约验证，确保后端实现与前端/消费方的接口约定一致。

### 步骤 1：安装 Pact CLI 工具

推荐使用 Homebrew 安装（如未安装 Homebrew，请先参考 https://brew.sh/）：

```bash
brew tap pact-foundation/pact-ruby-standalone
brew install pact-ruby-standalone
```

### 步骤 2：启动本地服务

```bash
source venv/bin/activate
python -m uvicorn src.main:app --reload
```

### 步骤 3：运行 Provider 契约验证（含 provider state handler）

```bash
pact-provider-verifier math-api-consumer-math-api-provider.json \
  --provider-base-url=http://localhost:8000 \
  --provider-states-setup-url=http://localhost:8000/_pact/provider_states
```

- `math-api-consumer-math-api-provider.json` 为自动生成的契约文件。
- `--provider-base-url` 指向本地服务地址。
- `--provider-states-setup-url` 指向你实现的 provider state handler 路径，确保契约中的 providerState 能被正确处理。

> **注意：**
>
> 1. 需确保服务已启动且可访问。
> 2. 验证通过会显示 success，失败会有详细错误信息。
> 3. 该命令可集成到 CI/CD 流程，保障接口一致性。
> 4. 如未指定 `--provider-states-setup-url`，providerState 相关准备动作会被跳过，可能导致部分场景验证不完整。
