# 导入 web3.py 模块
import csv
from web3 import Web3
from eth_utils import to_bytes
# 导入 python-mnemonic 模块
from mnemonic import Mnemonic

# 创建一个 web3.py 实例
w3 = Web3()
# 创建一个 Mnemonic 实例，指定使用中文单词表,改成english就是英文助记词
mnemo = Mnemonic("chinese_simplified")

# 定义一个函数，用来生成以太坊钱包并返回助记词、私钥和地址
def generate_wallet():
    # 生成一个符合 BIP39 规范的助记词（12个单词）
    mnemonic = mnemo.generate(strength=128)
    print(mnemonic)
    # 通过助记词和空密码生成种子
    seed = mnemo.to_seed(mnemonic, passphrase="")
    print(seed)
    # 通过种子生成账户对象（使用第一个派生路径）
    w3.eth.account.enable_unaudited_hdwallet_features()
    account1 = w3.eth.account.from_mnemonic(mnemonic, account_path="m/44'/60'/0'/0/0")
    print(account1.address)
    # 获取账户的私钥
    private_key = account1.key.hex()
    # 获取账户的地址
    address = account1.address
    # 返回一个字典，包含助记词、私钥和地址
    wallet_info=(mnemonic,private_key,address)
#    return {"mnemonic": mnemonic, "private_key": private_key, "address": address}
    return wallet_info
# 定义一个列表，用来存储批量生成的钱包信息
wallets = []

# 定义一个变量，表示要生成的钱包数量（可以根据需要修改）
n = 10

# 循环 n 次，调用 generate_wallet 函数，并把返回的字典添加到 wallets 列表中
for i in range(n):
    wallet = generate_wallet()
    wallets.append(wallet)
with open('eth_wallets.csv', 'w', newline='') as f:
    # 创建一个csv写入对象
    writer = csv.writer(f)
# 写入表头
    writer.writerow(['mnemonic', 'Private Key','Address'])
# 写入所有的钱包信息
    writer.writerows(wallets)

print('所有的钱包信息已经保存到eth_wallets.csv文件中')
# 打印 wallets 列表（也保存到文件csv中）
print(wallets)