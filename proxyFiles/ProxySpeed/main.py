import requests

proxy_list = []


proxyPath = input("Enter proxy file: ")
timeout_seconds = int(input("Timeout: "))

with open(f'{proxyPath}', 'r') as proxyFile:
    for proxy in proxyFile:
        proxy_list.append(proxy.strip())


# List of proxy servers to test


# Function to check the speed of a proxy
def check_proxy_speed(proxy_url):
    try:
        print("hallo")
        # Create a session with the proxy
        session = requests.Session()
        session.proxies = {'http': proxy_url, 'https': proxy_url}

        # Send a test request and measure response time
        response = session.get('https://www.example.com', timeout=timeout_seconds)
        response_time = response.elapsed.total_seconds()

        # You can adjust this threshold as needed
        if response_time < timeout_seconds:  # Check if response time is less than 2 seconds
            return True
        else:
            return False

    except requests.exceptions.RequestException:
        # Handle any errors that may occur during the request
        return False

# Loop through the proxy list and check their speeds
fast_proxies = []

for proxy in proxy_list:
    if check_proxy_speed(proxy):
        fast_proxies.append(proxy)

# Print the fast proxies
print("Fast Proxies:")
for proxy in fast_proxies:
    print(proxy)
