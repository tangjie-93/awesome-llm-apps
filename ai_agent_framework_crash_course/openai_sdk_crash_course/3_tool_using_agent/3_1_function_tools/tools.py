from agents import function_tool


@function_tool
def add_numbers(a: float, b: float) -> float:
    """计算两个数的和。"""
    return a + b


@function_tool
def multiply_numbers(a: float, b: float) -> float:
    """计算两个数的乘积。"""
    return a * b


@function_tool
def get_weather(city: str) -> str:
    """获取指定城市的模拟天气信息，用于演示无外部依赖的函数工具。"""
    return f"The weather in {city} is sunny with 72°F"


@function_tool
def convert_temperature(temperature: float, from_unit: str, to_unit: str) -> str:
    """在摄氏度和华氏度之间转换温度。"""
    source_unit = from_unit.lower()
    target_unit = to_unit.lower()

    if source_unit == "celsius" and target_unit == "fahrenheit":
        result = (temperature * 9 / 5) + 32
        return f"{temperature}°C = {result:.1f}°F"
    if source_unit == "fahrenheit" and target_unit == "celsius":
        result = (temperature - 32) * 5 / 9
        return f"{temperature}°F = {result:.1f}°C"
    return "Unsupported temperature conversion"
