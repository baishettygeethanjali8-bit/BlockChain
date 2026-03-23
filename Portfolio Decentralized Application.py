import tkinter as tk
from tkinter import messagebox
from web3 import Web3
from web3.providers.eth_tester import EthereumTesterProvider
from solcx import compile_source, install_solc

# install solidity compiler
install_solc("0.8.0")

# Solidity contract
contract_source_code = '''
pragma solidity ^0.8.0;

contract Portfolio {

    string public name;
    string public role;
    string public skills;

    constructor() {
        name = "Divya";
        role = "CSE Student";
        skills = "Java, Blockchain";
    }

    function updatePortfolio(string memory _name, string memory _role, string memory _skills) public {
        name = _name;
        role = _role;
        skills = _skills;
    }

    function getPortfolio() public view returns(string memory, string memory, string memory){
        return (name, role, skills);
    }
}
'''

# compile contract
compiled_sol = compile_source(contract_source_code, solc_version="0.8.0")
contract_id, contract_interface = compiled_sol.popitem()

# connect to local blockchain
w3 = Web3(EthereumTesterProvider())
w3.eth.default_account = w3.eth.accounts[0]

# deploy contract
Portfolio = w3.eth.contract(
    abi=contract_interface['abi'],
    bytecode=contract_interface['bin']
)

tx_hash = Portfolio.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

contract = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=contract_interface['abi']
)

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Portfolio DApp")
root.geometry("450x350")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Role").pack()
role_entry = tk.Entry(root, width=40)
role_entry.pack()

tk.Label(root, text="Skills").pack()
skills_entry = tk.Entry(root, width=40)
skills_entry.pack()

output = tk.Text(root, height=6, width=50)
output.pack(pady=10)

def load_data():
    name, role, skills = contract.functions.getPortfolio().call()

    name_entry.delete(0, tk.END)
    role_entry.delete(0, tk.END)
    skills_entry.delete(0, tk.END)

    name_entry.insert(0, name)
    role_entry.insert(0, role)
    skills_entry.insert(0, skills)

    output.insert(tk.END, "Portfolio loaded from blockchain\n")

def update_data():
    name = name_entry.get()
    role = role_entry.get()
    skills = skills_entry.get()

    tx = contract.functions.updatePortfolio(name, role, skills).transact()
    receipt = w3.eth.wait_for_transaction_receipt(tx)

    output.insert(tk.END, f"Updated!\nTx Hash: {receipt.transactionHash.hex()}\n\n")

    messagebox.showinfo("Success", "Portfolio Updated")

tk.Button(root, text="Load Portfolio", command=load_data).pack(pady=5)
tk.Button(root, text="Update Portfolio", command=update_data).pack(pady=5)

load_data()

root.mainloop()