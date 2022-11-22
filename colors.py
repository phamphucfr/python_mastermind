class Colors:
 
    """Classe Colors pour gérer la coloration des texts dans le Terminal"""

    reset = "\033[0m"
    bold = "\033[01m"
    disable = "\033[02m"
    underline = "\033[04m"
    reverse = "\033[07m"
    strikethrough = "\033[09m"
    invisible = "\033[08m"
 
    dict_colors = {'BK':'2;0;0;0m', 'GY':'2;95;95;95m', 'W':'2;255;255;255m', 'R':'2;255;0;0m', 
                   'G':'2;0;255;0m', 'B':'2;0;0;255m', 'Y':'2;255;255;0m', 'P':'2;255;0;255m', 'O':'2;255;175;0m' }

    def fg(self, letter:str, text:str) -> str:
        ansi_color = self.dict_colors[letter]   
        return f"\033[38;{ansi_color} {text}"
    
    def bg(self, letter:str, text:str) -> str:
        ansi_color = self.dict_colors[letter]             
        return f"\033[48;{ansi_color} {text}"

    
    def colorize_list(self,guess:list) -> str:
        colorized_guess_code = ""
                
        for g in guess:
            colorized_guess_code += self.fg(g,g) + " "
        
        final_colorized_str = f"{self.bold} {colorized_guess_code} {self.reset}"
        
        return final_colorized_str
    

    
    
