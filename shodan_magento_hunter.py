import shodan
import concurrent.futures

def get_magento_addr(result):
    ip = result['ip_str']
    ports = result.get('ports', [])
    if ports:
        ports_str = ', '.join(map(str, ports))
        return f"http://{ip}:{ports_str}"
    else:
        return f"http://{ip}"

def search_magento_sites(api, max_addresses):
    try:
        query = 'X-Magento-Vary'
        results = api.search(query, limit=max_addresses)
        file_path = 'magento_ip.txt'
        
        ip_list = []
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(get_magento_addr, result) for result in results['matches']]
            
            for future in concurrent.futures.as_completed(futures):
                ip_list.append(future.result())
        
        with open(file_path, 'w') as file:
            file.write('\n'.join(ip_list))
        
        print(f"Адреса собраны и файл {file_path} успешно создан")
        
    except shodan.APIError as e:
        print(f"Ошибка Shodan API: {e}")

if __name__ == '__main__':
    max_addresses = int(input("Введите максимальное количество адресов (не более 500): "))
    max_addresses = min(max_addresses, 500)
    SHODAN_API_KEY = 'YOUR_API_KEY'
    api = shodan.Shodan(SHODAN_API_KEY)
    search_magento_sites(api, max_addresses)