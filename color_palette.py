from dataclasses import dataclass

@dataclass(frozen=True)
class Palette:
    BACKGROUND : str    
    PRIMARY : str        
    SECONDARY : str     
    ACCENT : str         
    TIMER : str         
    TEXT : str           
    BORDER : str 

LIGHT_PALETTE = Palette(
    BACKGROUND = "#F8F9FA",    
    PRIMARY = "#E8F4F8",         
    SECONDARY = "#FFF2E8",       
    ACCENT = "#F0E8FF",         
    TIMER = "#FFE8E8",         
    TEXT = "#2D3748",            
    BORDER = "#CBD5E0"          
)

DARK_PALETTE = Palette(
    BACKGROUND = "#1A202C",     
    PRIMARY = "#2D3748",       
    SECONDARY = "#4A5568",      
    ACCENT = "#553C9A",          
    TIMER = "#744210",          
    TEXT = "#F7FAFC",            
    BORDER = "#4A5568"         
)
