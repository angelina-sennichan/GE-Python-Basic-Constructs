def merge_configs(*configs):
    merged = {}
    for config in configs:
        merged.update(config)
    return merged

config1 = {"timeout": 10}
config2 = {"timeout": 20, "debug": True}
result = merge_configs(config1, config2)
print(result)
