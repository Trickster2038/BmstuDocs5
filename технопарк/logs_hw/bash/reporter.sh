#/bin/bash!

printf "Отчет по логу: \n\n" > report.txt

echo "Всего запросов:" >> report.txt
wc -l access.log | awk '{print $1}' >> report.txt

printf "\nЧисло запросов (по типу):\n" >> report.txt
printf "[ тип | число запросов ]\n" >> report.txt
awk '{if(length($6)<10)print $6}' access.log | cut -c 2- | sort |uniq -c | awk '{print $2 " - " $1}' >> report.txt

printf "\nЧисло нестандартных запросов (по типу):\n" >> report.txt
printf "[ тип | число запросов ]\n" >> report.txt
awk '{if(length($6)>=10)print $6}' access.log | cut -c 2- | sort |uniq -c | awk '{print $2 " - " $1}' >> report.txt

printf "\nТоп 10 самых частых запросов:\n" >> report.txt
printf "[ число запросов | url ]\n" >> report.txt
awk '{print $7}' access.log | sort | uniq -c | sort -nrk1 | head -10 >> report.txt

printf "\nТоп 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой:\n" >> report.txt
printf "[ IP | url | код ответа | размер ]\n" >> report.txt
awk '{if(match($9,'/4../')) print $1 " " $6 " " $7 " " $8 " " $9 " " $10}' access.log | sort -nrk6 | head -5 >> report.txt

printf "\nТоп 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой:\n" >> report.txt
printf "[ IP | число запросов ]\n" >> report.txt
awk '{if(match($9,'/5../')) print $1}' access.log | sort | uniq -c | sort -nrk1 | awk '{print $2 " - " $1}' | head -5 >> report.txt
