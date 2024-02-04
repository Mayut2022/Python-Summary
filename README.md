# 基础知识
> "Powershell"、"Cmd"（命令提示符）和"Bash"是不同操作系统上的**命令行工具或脚本解释器**，它们用于与计算机系统进行交互、执行命令和运行脚本。（在一定程度上，可以将 Powershell 和 Cmd（命令提示符）与 Spyder 和 PyCharm 之间进行类比，大致类似，但具体的命令不太一样）
**Powershell:**
Powershell 是由 Microsoft 开发的强大的脚本语言和命令行壳层。它主要用于 Windows 操作系统，提供了一套用于系统管理和任务自动化的命令和脚本。Powershell 具有丰富的功能，支持对象管道、脚本编写、任务自动化、远程管理等。它在 Windows 中的角色类似于 Bash 在 Unix/Linux 系统中的角色。
**Cmd (命令提示符):**
Cmd 是 Windows 操作系统上的默认命令行解释器。它提供了基本的命令行环境，允许用户输入和执行命令，以及运行批处理脚本（.bat 文件）。Cmd 在简单任务和脚本中有用，但它的功能相对有限。
**Bash:**
Bash（Bourne Again SHell）是一种 Unix/Linux 系统上的命令行解释器和脚本语言。它是 Bourne Shell 的增强版，提供了强大的命令行工具和脚本编写功能。Bash 在许多 Unix 和 Linux 系统上是默认的命令行解释器，也可用于 Windows，例如通过 Windows Subsystem for Linux（WSL）。  

> **git命令可以在powershell cmd bash 上同时使用吗？**  
> 是的，Git 命令是跨平台的，可以在 Windows 的 Powershell、Cmd（命令提示符），以及 Unix/Linux 系统的 Bash 上同时使用。Git 提供了统一的命令集，因此你可以在不同的命令行环境中使用相同的 Git 命令。


# 基本信息
## username and email
> **南京404机房电脑**  
> user.name=MaYutong
> user.email=ma_yu_t@163.com

> **ThinkPad**  
> user.name=myt
> user.email=1034472773@qq.com

```bash
# 更改用户名和邮箱
git config --global user.name "Your New Username"
git config --global user.email "your.new.email@example.com"
```

