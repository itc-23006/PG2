def is_valid_chess_dictionary(chess_dict):

    valid_positions = [f"{file}{rank}" for file in "abcdefgh" for rank in "12345678"]
    
    valid_pieces = {'wK', 'wQ', 'wR', 'wB', 'wN', 'wP', 'bK', 'bQ', 'bR', 'bB', 'bN', 'bP'}
    
    for position, piece in chess_dict.items():
        if position not in valid_positions:
            print(f"無効な位置: {position}")
            return False
        
        if piece not in valid_pieces:
            print(f"無効な駒の表現: {piece}")
            return False
    
    return True

chess_dict = {
    'a1': 'wR', 'h1': 'wR', 'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP', 
    'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP', 'e1': 'wK', 'd1': 'wQ',
    'b1': 'wN', 'g1': 'wN', 'c1': 'wB', 'f1': 'wB',
    'a8': 'bR', 'h8': 'bR', 'a7': 'bP', 'b7': 'bP', 'c7': 'bP', 'd7': 'bP', 
    'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP', 'e8': 'bK', 'd8': 'bQ',
    'b8': 'bN', 'g8': 'bN', 'c8': 'bB', 'f8': 'bB'
}

print(is_valid_chess_dictionary(chess_dict))