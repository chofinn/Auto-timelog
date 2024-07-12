# Auto timelog
## How to use
### 修改 example.json
1. 填入自己的 user_id
2. 將 `example.json` 改名成 `config.json`
### 執行
直接點 `run.bat` 或自己執行 python 檔

## config.json
```
"routine": [
      [["LabProject", 13, 17]],
      [["LabProject", 11, 12], ["LabProject", 13, 17]],
      [["LabProject", 10, 12], ["LabProject", 13, 17]],
      [["LabProject", 10, 12], ["LabProject", 13, 16]],
      [],
      [],
      []
  ], 
```
- "routine" 裡面 7 個 list 對應星期一到日

```
["LabProject", 13, 17]
```
- 第一個是 activity 名稱 (必須是你帳號裡面已存在的)
- 第二跟三個是開始和結束的時間 (24 小時制)
- 目前還無法記跨日
    - ex: 只能記 22~23, 不能 22~24 or 22~1
### routine
可以把每周同樣的時間放在這裡
### custom
可以修改 json 檔後將一周的紀錄一次記上
### comment
可以把所有 activity 暫放在這，要記 custom 時可以複製貼上
### config
設定資料
- user_id
    - timelog 的 user id (必填)
