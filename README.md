
### 说明
1. 安装 pyyaml：`pip install pyyaml`
2. 执行 read_setting.py，读取yaml文件中的内容

### 使用 virtualenv/venv 和 pip 管理虚拟环境：
1. 进入项目的根目录，创建虚拟环境：`virtualenv --python=python3 venv`或`python3 -m venv ./venv`（venv不用安装，不过需要python3.3以上）
2. 进入虚拟环境：`source venv/bin/activate`
3. 安装依赖：`pip install -r requirements.txt`
4. 安装新包后，执行这个命令将包名和包版本信息写入 requirements.txt：`pip freeze > requirements.txt`

### 资料
资料 | 网址
--- | ---
官方文档 | https://pyyaml.org/wiki/PyYAMLDocumentation