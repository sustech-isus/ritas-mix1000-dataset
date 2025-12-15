# 统计数据集收集信息
import re
from collections import Counter


def extract_env_type(name: str) -> str | None:
    """
    从数据集名称中提取环境类型
    
    Args:
        name: 数据集名称，格式如 EnvNight_WeatherHeavyRain_CaseForceCutin
        
    Returns:
        环境类型字符串（Night/Noon/Sunset），如果没有则返回 None
    """
    match = re.match(r'Env([^_]+)', name)
    if match:
        return match.group(1)
    return None


def extract_weather_type(name: str) -> str | None:
    """
    从数据集名称中提取天气类型
    
    Args:
        name: 数据集名称，格式如 EnvNight_WeatherHeavyRain_CaseForceCutin
        
    Returns:
        天气类型字符串，如果没有天气因子则返回 None
    """
    match = re.search(r'Weather([^_]+)', name)
    if match:
        return match.group(1)
    return None


def extract_road_type(name: str) -> str | None:
    """
    从数据集名称中提取道路类型
    
    Args:
        name: 数据集名称，格式如 EnvNight_RoadFlodding_CaseForceCutin
        
    Returns:
        道路类型字符串，如果没有道路因子则返回 None
    """
    match = re.search(r'Road([^_]+)', name)
    if match:
        return match.group(1)
    return None


def parse_yaml_file(filepath: str) -> list[dict]:
    """
    解析简单的 YAML 文件，提取 id 和 name 字段
    
    Args:
        filepath: YAML 文件路径
        
    Returns:
        包含 id 和 name 的字典列表
    """
    data = []
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r'- id: (\d+)\s+name: (.+)'
    matches = re.findall(pattern, content)
    
    for id_str, name in matches:
        data.append({'id': int(id_str), 'name': name.strip()})
    
    return data


def main():
    data = parse_yaml_file('list.yaml')
    
    weather_types = []
    sensor_datasets = []
    case_datasets = []
    total_count = len(data)
    
    for item in data:
        name = item.get('name', '')
        env_type = extract_env_type(name)
        weather_type = extract_weather_type(name)
        road_type = extract_road_type(name)
        
        if env_type and weather_type:
            if road_type:
                weather_type_full = f'Env{env_type}_Weather{weather_type}_Road{road_type}'
            else:
                weather_type_full = f'Env{env_type}_Weather{weather_type}'
            weather_types.append(weather_type_full)
        elif env_type and road_type:
            weather_type_full = f'Env{env_type}_Road{road_type}'
            weather_types.append(weather_type_full)
        
        if re.search(r'(Camera|Lidar|Sensor)', name):
            sensor_datasets.append(name)
        
        if re.search(r'Case[A-Z]', name):
            case_datasets.append(name)
    
    weather_counter = Counter(weather_types)
    
    print("=" * 60)
    print(f"Total datasets: {total_count:,}")
    print("=" * 60)
    
    print(f"\nWeather factor categories:")
    print(f"  Total weather datasets: {len(weather_types):,}")
    print(f"  Total sensor datasets:  {len(sensor_datasets):,}")
    print(f"  Total case datasets:   {len(case_datasets):,}")
    
    print(f"\n{'─' * 60}")
    print(f"Weather type breakdown:")
    print(f"{'─' * 60}")
    print(f"Total weather type categories: {len(weather_counter)}")
    print()
    for weather_type, count in sorted(weather_counter.items()):
        print(f"  {weather_type:<50} {count:>5}")
    
    harzed_weather_counter = {
        weather_type: count 
        for weather_type, count in weather_counter.items() 
        if 'WeatherSoftRain' not in weather_type
    }
    
    print(f"\n{'─' * 60}")
    print(f"Harzed Weather type breakdown:")
    print(f"{'─' * 60}")
    print(f"Total harzed weather type categories: {len(harzed_weather_counter)}")
    print()
    for weather_type, count in sorted(harzed_weather_counter.items()):
        print(f"  {weather_type:<50} {count:>5}")


if __name__ == '__main__':
    main()