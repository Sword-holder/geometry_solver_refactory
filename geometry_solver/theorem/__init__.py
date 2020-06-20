from geometry_solver.theorem.theorem import Theorem
from geometry_solver.theorem.triangle_angle_sum import TriangleAngleSum
from geometry_solver.theorem.line_length_sum import LineLengthSum
from geometry_solver.theorem.common_vertex_angle_sum import CommonVertexAngleSum
from geometry_solver.theorem.supplementary_angle_sum import SupplementaryAngleSum
from geometry_solver.theorem.perpendicular_angle import PerpendicularAngle
from geometry_solver.theorem.opposite_vertical_angle_equality import OppositeVertivalAngleEquality
from geometry_solver.theorem.triangle_circumference import TriangleCircumference
from geometry_solver.theorem.triangle_area import TriangleArea

valid_theorem = [
    TriangleAngleSum,
    LineLengthSum,
    CommonVertexAngleSum,
    SupplementaryAngleSum,
    PerpendicularAngle,
    OppositeVertivalAngleEquality,
    TriangleCircumference,
    TriangleArea
]
