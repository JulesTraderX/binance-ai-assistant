@echo off
rem OpenClaw Gateway (v2026.3.2)
set "TMPDIR=C:\Users\DIGYAG~1\AppData\Local\Temp"
set "PATH=C:\Program Files (x86)\Common Files\Intel\Shared Libraries\redist\intel64_win\compiler;C:\Program Files (x86)\Common Files\Oracle\Java\java8path;C:\Program Files (x86)\Common Files\Oracle\Java\javapath;C:\Program Files (x86)\Common Files\Intel\Shared Libraries\redist\intel64\compiler;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;C:\Program Files\nodejs\;C:\Program Files\Git\cmd;C:\ProgramData\chocolatey\bin;C:\Program Files (x86)\GnuWin32\bin;C:\Program Files\Redis\;C:\Users\Digy Agency\AppData\Local\Programs\Python\Python313\Scripts\;C:\Users\Digy Agency\AppData\Local\Programs\Python\Python313\;C:\Users\Digy Agency\AppData\Local\Microsoft\WindowsApps;C:\Users\Digy Agency\AppData\Local\Programs\Microsoft VS Code\bin;C:\Users\Digy Agency\AppData\Roaming\npm;C:\Program Files\PostgreSQL\17\bin"
set "OPENCLAW_GATEWAY_PORT=18789"
set "OPENCLAW_GATEWAY_TOKEN=076986fe0d7a6fb61bf6a27c02a1f50be4f8fe378cffdc72"
set "OPENCLAW_SYSTEMD_UNIT=openclaw-gateway.service"
set "OPENCLAW_SERVICE_MARKER=openclaw"
set "OPENCLAW_SERVICE_KIND=gateway"
set "OPENCLAW_SERVICE_VERSION=2026.3.2"
"C:\Program Files\nodejs\node.exe" "C:\Users\Digy Agency\AppData\Roaming\npm\node_modules\openclaw\dist\index.js" gateway --port 18789
