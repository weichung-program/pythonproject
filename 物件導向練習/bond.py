"""請撰寫一個 Asset 類別，具備以下內容：

屬性（Attributes）：
name：資產名稱
cost：資產成本
salvage_value：殘值（資產使用完畢後的預估價值）
useful_life：使用年限（以年計）
方法（Methods）：
annual_depreciation()：使用直線法計算每年折舊金額，公式：(成本 - 殘值) / 使用年限，並回傳折舊金額。
print_asset()：回傳格式化的字串，格式如下：
Asset: {name}
Cost: {cost}
Salvage Value: {salvage_value}
Useful Life: {useful_life} years
Annual Depreciation: {每年折舊金額}"""
class Asset:
    def __init__(self,name,cost,salvage_value,useful_life):
        self.name=name
        self.cost=cost
        self.salvage_value=salvage_value
        self.useful_life=useful_life
    def annual_depreciation(self):
        depreciation=(self.cost-self.salvage_value)/self.useful_life
        return depreciation
    def print_asset(self):
        depreciation=self.annual_depreciation()
        return (f"Asset: {self.name}\n"
                f"Cost: {self.cost}\n"
                f"Salvage Value: {self.salvage_value}\n"
                f"Useful Life: {self.useful_life} years\n"
                f"Annual Depreciation: {depreciation}")
	
asset = Asset("Machine", 10000, 2000, 4)
print(asset.annual_depreciation())
	
asset = Asset("Truck", 50000, 5000, 5)
print(asset.print_asset())