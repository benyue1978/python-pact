# FastAPI 数学运算 API 文档

## 1. API 结构与接口文档

### 路由设计

所有运算接口均为 POST，路径统一为 `/api/math/{operation}`，operation 可为 `add`、`subtract`、`multiply`、`divide`。

#### 1.1 通用请求体（JSON）
```json
{
  "a": 1.0,
  "b": 2.0
}
```
- `a`：第一个操作数（float，必填）
- `b`：第二个操作数（float，必填）

#### 1.2 通用响应体（JSON）
```json
{
  "result": 3.0
}
```
- `result`：运算结果（float）

#### 1.3 错误响应体
```json
{
  "detail": "错误描述"
}
```
- `detail`：错误信息（如参数缺失、除零错误等）

### 路由列表

| 方法 | 路径                | 描述   | 请求体字段 | 响应体字段 | 备注         |
|------|--------------------|--------|------------|------------|--------------|
| POST | /api/math/add      | 加法   | a, b       | result     |              |
| POST | /api/math/subtract | 减法   | a, b       | result     |              |
| POST | /api/math/multiply | 乘法   | a, b       | result     |              |
| POST | /api/math/divide   | 除法   | a, b       | result     | 除数为0报错  |

### OpenAPI 示例（YAML）
```yaml
paths:
  /api/math/add:
    post:
      summary: 加法运算
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/MathRequest'
      responses:
        '200':
          description: 运算成功
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MathResponse'
        '400':
          description: 错误请求
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
  # 其它运算接口同理
components:
  schemas:
    MathRequest:
      type: object
      properties:
        a:
          type: number
        b:
          type: number
      required:
        - a
        - b
    MathResponse:
      type: object
      properties:
        result:
          type: number
    ErrorResponse:
      type: object
      properties:
        detail:
          type: string
```

### 说明
- 所有接口均返回 JSON。
- 错误情况（如参数缺失、类型错误、除零等）返回 400 状态码及错误描述。
- 后续可扩展更多运算类型或批量运算。

---

## 2. 实现说明

### 2.1 加法 API 实现说明
- 路径：POST /api/math/add
- 请求体：{"a": float, "b": float}
- 响应体：{"result": float}
- 已在 src/api/math.py 中实现，包含类型注解、docstring 和错误处理
- 已在 main.py 注册路由

### 2.2 加法 API 测试与覆盖率
- 已使用 pytest 编写加法 API 单元测试，测试文件：tests/test_math.py
- 测试包含类型注解和 docstring，符合最佳实践
- 已集成 pytest-cov，支持代码覆盖率统计
- 运行命令：
  ```bash
  source venv/bin/activate
  pytest --cov=src tests/
  ```
- 当前覆盖率约 90%，未覆盖部分为异常分支
- 可通过 pytest-cov 生成详细覆盖率报告 