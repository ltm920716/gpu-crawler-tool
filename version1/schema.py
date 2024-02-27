gpu_info = []
gpu = {}
gpu["name"] = None
gpu["gpu"] = None
gpu["scale"] = None
gpu["gpu_ram"] = None
gpu["vcpus"] = None
gpu["cpu_info"] = None
gpu["ram"] = None
gpu['storage'] = None
gpu['bandwidth'] = None
gpu['regions'] = [None]
gpu['hour_price'] = None
gpu['month_price'] = None
gpu['year_price'] = None
gpu['is_available'] = True
gpu['account'] = None
gpu['os'] = None
gpu['public_network'] = None
gpu['private_network'] = None
            
gpu_info.append(gpu)

return {
            "website": response.url,
            "platform": "Latitude.sh",
            "gpus": gpu_info
        }