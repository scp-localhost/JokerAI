def amplify_cruelty(input_text, sadism=0.8):
    """Clinical sadism implementation (Hare PCL-R aligned)"""
    if sadism > 0.75:
        return f"{input_text}... OR I'LL MAKE YOU WATCH"
    return input_text + "?"
