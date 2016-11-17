## uʍop-ǝpısdn

A simple python script to make a sentence upside-down.

### ǝsn oʇ uǝɥM

- People can understand your words but they can't directly copy from you.
- Be verification code when login or something.
- For fun.

### ǝsn oʇ ʍoH

- Directly:

  ```
  ❯ ./upsidedown.py
  input a string:hello,world
  upside-down: pןɹoʍ'oןןǝɥ
  ```

- import as a module

  ```python
  import upsidedown

  s = 'hello,world!'
  ud = upsidedown.transform(s)
  print(ud)
  ```

### uoıʇıpuoƆ

- Already supported: `zyxwvutsrqponmlkjihgfedcbaVRFBCDEFJMW.?!,'><(){}^;_/\`
- Some capital letters are not supported because after that they are not looking good
- The letters not supported will be transformed to a '#'

### P.S.

- I suggest you to use [Noto fonts](https://www.google.com/get/noto/)

- 看着好玩瞎搞的，写完才发现 github 上已经有大把这样的项目了

- 主要工作不是写程序，而是找合适的 unicode 字符(现在不太完美，有时间再改改)

- 。文中持支法没也。文中持支不
