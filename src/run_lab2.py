from spatial import PointSet

pointset = PointSet.from_csv("data/points.csv")
print(f"Loaded {pointset.count()} points.")