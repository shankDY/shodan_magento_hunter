# Shodan Magento Hunter

"Shodan Magento Hunter" позволяет составить список адресов сайтов с Magento

## Зависимости

Для корректной работы инструмента установите необходимые зависимости с помощью следующей команды:

```bash
pip install -r requirements.txt
```

## Использование

1. Получите API-ключ для Shodan и внесите его в переменную `SHODAN_API_KEY` в файле `shodan_magento_hunter.py`.
2. Запустите инструмент:

```bash
python shodan_magento_hunter.py
```

Инструмент выполнит поиск Magento-сайтов через Shodan и сохранит список IP-адресов в файле `magento_ip.txt`.

