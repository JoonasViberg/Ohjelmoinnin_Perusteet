import math
from svgwrite import Drawing, cm, rgb
from svgwrite.shapes import Rect, Circle, Polygon
from typing import Optional, List, Tuple

def drawSquare(PDwg: Drawing, left: float, top: float, sideLength: float, color: str, strokeColor: str) -> None:
    PDwg.add(Rect(
        insert=(f'{left}px', f'{top}px'), 
        size=(f'{sideLength}px', f'{sideLength}px'),
        fill=color,
        stroke=strokeColor,
        stroke_width='2'
    ))
    return None

def drawCircle(PDwg: Drawing, centerX: float, centerY: float, radius: float, color: str, stroke: str) -> None:
    PDwg.add(Circle(
        center=(f'{centerX}px', f'{centerY}px'),
        r=f'{radius}px',
        fill=color,
        stroke=stroke,
        stroke_width='2'
    ))
    return None

def drawHexagon(PDwg: Drawing, centerX: float, centerY: float, apothem: float, fill_color: str, stroke_color: str) -> None:
    """Calculates corner points and draws a regular hexagon."""
    
    # 1. Calculate Circumradius (R) from Apothem (a)
    # R = a / cos(30 degrees) where cos(30) = sqrt(3)/2
    circumradius = apothem / math.cos(math.radians(30))
    
    # Starting angle (Top Right corner)
    start_angle_deg = 30
    
    # The corner points list
    points: List[Tuple[int, int]] = []

    # Calculate 6 points, rotating 60 degrees (math.radians(60)) each time
    for i in range(6):
        angle_deg = start_angle_deg + (i * 60)
        angle_rad = math.radians(angle_deg)
        
        # Calculate X and Y coordinates relative to the center
        # X = Xc + R * cos(theta)
        # Y = Yc - R * sin(theta) (Y axis points down in SVG)
        
        X = centerX + circumradius * math.cos(angle_rad)
        Y = centerY - circumradius * math.sin(angle_rad)
        
        # Round the values into integers before applying to the polygon
        points.append((round(X), round(Y)))

    # 2. Draw the Polygon
    PDwg.add(Polygon(
        points=points,
        fill=fill_color,
        stroke=stroke_color,
        stroke_width='2'
    ))
    return None

def saveSvg(PDwg: Drawing, PFilename: Optional[str] = None) -> None:
    """Prompts for filename and confirms saving the SVG. Accepts optional PFilename for testing."""
    
    if PFilename:
        filename = PFilename
        confirm = 'y'
    else:
        filename = input("Insert filename: ")
        print(f'Saving file to "{filename}"')
        confirm = input("Proceed (y/n)?: ").strip().lower()
    
    if confirm == 'y':
        try:
            PDwg.saveas(filename, pretty=True, indent=2)
            if not PFilename:
                print("Vector saved successfully!")
        except Exception as e:
            print(f"Error saving SVG: {e}")
    elif not PFilename:
        print("Save operation cancelled.")
        
    return None