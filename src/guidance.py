import math
from entities import Missile, Target


def calculate_heading(missile: Missile, target: Target) -> float:
    """Calculate new heading angle for missile based on target position"""
    dx = target.predicted_x - missile.x
    dy = target.predicted_y - missile.y
    desired_heading = math.degrees(math.atan2(dy, dx))

    # Smooth the heading change (proportional navigation)
    heading_difference = desired_heading - missile.heading
    # Normalize the angle to -180 to 180
    if heading_difference > 180:
        heading_difference -= 360
    elif heading_difference < -180:
        heading_difference += 360

    # Limit the rate of turn
    max_turn_rate = 30  # degrees per step
    if abs(heading_difference) > max_turn_rate:
        if heading_difference > 0:
            heading_difference = max_turn_rate
        else:
            heading_difference = -max_turn_rate

    return missile.heading + heading_difference


def update_missile_position(missile: Missile, new_heading: float, time_step: float):
    """Update missile position based on heading and speed"""
    # Update heading
    missile.heading = new_heading

    # Convert heading to radians for position calculation
    heading_rad = math.radians(new_heading)

    # Calculate new position
    new_x = missile.x + missile.speed * math.cos(heading_rad) * time_step
    new_y = missile.y + missile.speed * math.sin(heading_rad) * time_step

    # Slow down when near target
    missile.update_position(new_x, new_y)