------------- Отличия для Debian 10.5
Создать 64 разрядную виртуальную машину м скачать debian по ссылке
https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-10.5.0-amd64-xfce-CD-1.iso
------------- Отличия для Debian 9
Скачать debian с сайта
    https://www.debian.org/CD/http-ftp/
или сразу
    https://cdimage.debian.org/debian-cd/current/i386/iso-cd/debian-9.5.0-i386-xfce-CD-1.iso

-------------Л/Р 1
!!!Для debian 11.0 задавать:
Graphics Install
Russian
Российская Федерация
Русская
Alt+Shift
Имя компьютера = Ваша фамилия латиницей
Имя домена не задавать
Пароль суперпользователя = root
Имя пользователя = user
Имя учётной записи = user
Пароль пользователя = user
Москва+00
Авто - использовать весь диск
SCSI...
Все файлы в одном разделе
Закончить разметку
Да
Сканировать дополнительный носитель = нет
Российская Федерация
deb.debian.org
Прокси = не задавать
Участвовать в опросе = нет
Устанавливать только Стандартные системные утилиты. Флажки снимаются мышью или пробелом!!!
*Примечание: Во второй лаб.работе репозиторий будет задан. При редактировании файла sources.list просто допишите вторую # в первой строке (для тренировки)
Установить GRUB на первичный диск = да
/dev/sda

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
Перед установкой пакета xfce4-panel установить пакет dbus-x11
Если контекстное меню (в какой то версии) не работает.
Перезагрузить виртуальную машину средствами VirtualBox и продолжить работу

Вместо leafpad устанавливать и использовать mousepad
Если установили по совету из методички пакет «lxde», то его надо удалить командой
	apt-get remove lxde gpicview lxappearance lxde-core lxde-common lxinput lxmusic lxpanel lxsession lxsession-edit lxshortcut lxterminal xarchiver xscreensaver

Сборка leafpad из исходников:
wget http://deb.debian.org/debian/pool/main/l/leafpad/leafpad_0.8.18.1.orig.tar.gz
или через w3m http://deb.debian.org/debian/pool скачать этот файл
tar -xf leafpad_0.8.18.1.orig.tar.gz
apt-get install build-essential
apt-get install intltool
apt-get install libgtk2.0-dev
cd leafpad_0.8.18.1
./configure
make
make install-strip

Фон рабочего стола можно скачать с промощью w3m
затем редактируем файл конфигурации:
nano /root/.ideskrc
Задать 
Background.Source: /root
Backgroung.file=СКАЧАННЫЙ_ФАЙЛ.jpg
!!!Не забудьте удалить пробел после имени файла

Чтобы активизировать смену раскладки клавиатуры надо добавить в autostart команду:
setxkbmap -layout us,ru -option grp:alt_shift_toggle

-------------Л/Р 5
Если не удаётся создать файловую систему FAT32 (нет mkfs.vfat) надо дать команду
apt-get install dosfstools

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
