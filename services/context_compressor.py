def compress(memory):
    compressed = []
    
    for m in memory:
        # Safeguard against None values and grab the "raw" field
        raw = m.get("raw", "") if m else ""
        compressed.append(raw[:120])
        
    return compressed