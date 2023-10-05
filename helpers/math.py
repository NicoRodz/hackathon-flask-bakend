class MathHelper:

    @classmethod
    def _group_by_type(cls, data_array):
        grouped = {"width": [], "height": [], "depth": []}
        for data in data_array:
            if data["type"] == "width":
                grouped["width"].append(data["width"])
            elif data["type"] == "depth":
                grouped["depth"].append(data["width"])

            grouped["height"].append(data["height"])

        return grouped

    @classmethod
    def _get_statistics(cls, measurements):
        statistics = {
            "width": {
                "min": float(min(measurements["width"])),
                "max": float(max(measurements["width"])),
                "avg": float(sum(measurements["width"]) / len(measurements["width"]))
            },
            "depth": {
                "min": float(min(measurements["depth"])),
                "max": float(max(measurements["depth"])),
                "avg": float(sum(measurements["depth"]) / len(measurements["depth"]))
            },
            "height": {
                "min": float(min(measurements["height"])),
                "max": float(max(measurements["height"])),
                "avg": float(sum(measurements["height"]) / len(measurements["height"]))
            }
        }

        return statistics

    @classmethod
    def get_cube_measurements(cls, measure_results_array):
        grouped = cls._group_by_type(measure_results_array)
        return cls._get_statistics(grouped)
