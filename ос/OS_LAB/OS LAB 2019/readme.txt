    Отличия от методички для Debian 9
-------------Л/Р 1
Скачать debian с сайта
    https://www.debian.org/CD/http-ftp/
или сразу
    https://cdimage.debian.org/debian-cd/current/i386/iso-cd/debian-9.5.0-i386-xfce-CD-1.iso
---debian---
root/root
user/user

Зеркало архива не использовать, Если возникает ошибка (в дистрибутиве i386) использовать mirror.yandex.ru 
Устанавливать только Стандартные системные утилиты. Флажки снимаются пробелом!!!

Windows не Устанавливать
-------------Л/Р 2
дайте команду xx
Если выводятся "квадратики" вместо русских букв, дайте команду
nano /lib/systemd/system/console-setup.service
изменить строку 
    ExecStart=/lib/console-setup/console-setup.sh
на
    ExecStart=/bin/setupcon
Нажмите
    <Ctrl>+X
    Y
    <Enter>
и перезагрузитесь командой
    reboot
    
vi /etc/apt/sources.list
deb http://ftp.debian.org/debian/ stretch main
apt-get update
apt-get install psmisc net-tools w3m

Если проблемы с сетью, проверить файлы:
    namo /etc/resolv.conf
должно быть
    nameserver 8.8.8.8
Перечитать настройки сети:
    ifdown eth1
    ifup eth1

В дальнейшем, если нет команды - найти пакет командой
    apt-cache search КОМАНДА
и установить его 
    apt-get install ПАКЕТ
-------------Л/Р 3
Если контекстное меню (в какой то версии) не работает.
Перезагрузить виртуальную машину средствами VirtualBox и продолжить работу

Вместо leafpad устанавливать и использовать mousepad или установить leafpad в составе огромного пакета «lxde»
Перед установкой пакета xfce4-panel установить пакет dbus-x11
    
-------------Л/Р 7
на windows7+ установить Telnet Client:
    pkgmgr /iu:"TelnetClient"

Если проблемы с сетью (из за лабораторных по сетям) создать в VirtualBox 
файл>>Настройки>>Сеть>>Виртуальные сети хоста>>Контекстное меню>>Добавить виртуальну сеть(vboxnet1)>>Изменить>>DHCP Сервер>>Включить>>OK>>OK
Выбрать Виртуальную машину>>Настроить>>Сеть>>Адаптер 2>>выбрать vboxnet1>>OK>>OK

Проверить настройки Debian
    namo /etc/network/interfaces
Должно быть
    allow-hotplug eth0
    iface eth0 inet dhcp

    allow-hotplug eth1
    iface eth1 inet dhcp
Рестартовать
    reboot
