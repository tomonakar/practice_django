# プロジェクトの開始方法
1. gitクローン
2. 仮想環境構築
3. vscode の場合は仮想環境のインタプリタを選択
4. djangoインストール

```
# python インストール
brew install pyenv
cat << 'EOS' >> ~/.bash_profile
export PYENV_ROOT=/usr/local/var/pyenv
if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi
EOS
source ~/.bash_profile

pyenv install -l
pyenv install <x.x.x>
pyenv global <x.x.x>
pyenv versions

# 仮想環境構築
python3 -m venv env
source env/bin/activate

# Djangoインストール
pip install django

# requirements.txtからインストール
pip install -r requirements.txt
```